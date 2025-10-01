import streamlit as st
import random
from quiz_data import QA_DATA # Import the question data structure

# --- Configuration ---
st.set_page_config(layout="centered", page_title="AI Concepts Quiz App")

# --- Initialize Session State ---
def initialize_session_state():
    """Sets up initial state variables for the application."""
    if 'page' not in st.session_state:
        st.session_state.page = "setup" # setup, quiz, results
    if 'selected_chapters' not in st.session_state:
        st.session_state.selected_chapters = []
    if 'question_count' not in st.session_state:
        st.session_state.question_count = 10
    if 'quiz_questions' not in st.session_state:
        st.session_state.quiz_questions = []
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}
    if 'last_selection' not in st.session_state:
        st.session_state.last_selection = None

# --- Callback Functions ---

def start_quiz(selected_chapters, question_count):
    """
    Called when the 'Start Quiz' button is pressed.
    Gathers questions, shuffles them, and transitions to the quiz page.
    """
    if not selected_chapters:
        st.error("Please select at least one chapter.")
        return

    # 1. Gather all questions from selected chapters
    all_questions = []
    for chapter in selected_chapters:
        all_questions.extend(QA_DATA.get(chapter, []))

    if not all_questions:
        st.error("No questions found for the selected chapters.")
        return

    # 2. Select the specified number of questions randomly
    # Ensure we don't try to sample more questions than available
    count = min(question_count, len(all_questions))
    st.session_state.quiz_questions = random.sample(all_questions, count)

    # 3. Reset quiz state and transition to quiz page
    st.session_state.current_index = 0
    st.session_state.user_answers = {}
    st.session_state.quiz_length = len(st.session_state.quiz_questions)
    st.session_state.selected_chapters = selected_chapters
    st.session_state.page = "quiz"

def record_answer():
    """
    Records the user's selected answer and updates the current index.
    Called by the 'Next Question' or 'Show Results' button.
    """
    current_q_index = st.session_state.current_index
    
    # Check if the user selected an answer for the current question
    if st.session_state.last_selection is None:
        st.warning("Please select an answer before proceeding.")
        return
        
    # Record the answer
    st.session_state.user_answers[current_q_index] = st.session_state.last_selection

    # Clear the selection for the next question
    st.session_state.last_selection = None
    
    # 1. Move to the next question OR
    if current_q_index < st.session_state.quiz_length - 1:
        st.session_state.current_index += 1
    # 2. Transition to the results page
    else:
        st.session_state.page = "results"

def restart_quiz():
    """Resets the application back to the setup page."""
    initialize_session_state()
    st.session_state.page = "setup"
    st.session_state.current_index = 0

# --- UI Rendering Functions ---

def render_setup_page():
    """Renders the chapter selection and quiz length setup UI."""
    st.title("🧠 AI Concepts Quiz App")
    st.markdown("---")

    all_chapters = list(QA_DATA.keys())
    
    # Chapter selection checkboxes
    st.subheader("1. Select Chapters")
    chapters_selection = st.multiselect(
        "Choose one or more chapters to include in your quiz:",
        options=all_chapters,
        default=st.session_state.selected_chapters,
        key="setup_chapter_select"
    )

    # Question count slider
    max_questions = sum(len(QA_DATA.get(c, [])) for c in chapters_selection)
    
    st.subheader(f"2. Choose Quiz Length (Max: {max_questions})")
    
    # Set default slider value based on previous session state or a sensible default
    initial_count = st.session_state.question_count
    if initial_count > max_questions and max_questions > 0:
         initial_count = max_questions
    elif max_questions == 0:
         initial_count = 0

    question_count = st.slider(
        "Number of questions:",
        min_value=1,
        max_value=max_questions if max_questions > 0 else 1,
        value=initial_count,
        step=1,
        key="setup_count_slider",
        disabled=(max_questions == 0)
    )
    
    st.markdown("---")
    
    # Start button
    st.button(
        "Start Quiz",
        on_click=start_quiz,
        args=(chapters_selection, question_count),
        use_container_width=True,
        type="primary"
    )


def render_quiz_page():
    """Renders the current question and answer options."""
    
    # Ensure we don't run this function if data isn't loaded correctly
    if not st.session_state.quiz_questions:
        st.error("Quiz data not initialized. Please go back to setup.")
        st.button("Go to Setup", on_click=restart_quiz)
        return

    current_index = st.session_state.current_index
    quiz_length = st.session_state.quiz_length
    current_q = st.session_state.quiz_questions[current_index]
    
    # --- Header ---
    st.subheader("🧠 AI Concepts Quiz App")
    st.markdown(f"Quizzing on: **{', '.join(st.session_state.selected_chapters)}**")
    st.markdown(f"Question **{current_index + 1}** of **{quiz_length}**")
    st.progress((current_index + 1) / quiz_length)
    st.markdown("---")
    
    # --- Question Display ---
    st.header(f"Question {current_index + 1}")
    st.write(current_q["question"])
    
    # --- Options (Radio Buttons) ---
    
    # Use the question index as the key to ensure the radio button state is unique
    # The value selected is stored automatically by st.radio, we capture it below.
    selection = st.radio(
        "Select your answer:",
        current_q["options"],
        index=None, # Start with no selection
        key=f"q_{current_index}_radio"
    )
    
    # Manually store the selection in session_state immediately after radio changes
    # This prevents the answer from being lost if the user navigates away or refreshes
    st.session_state.last_selection = selection

    st.markdown("---")
    
    # --- Navigation Button ---
    if current_index < quiz_length - 1:
        # Next Question button
        st.button("Next Question", on_click=record_answer, use_container_width=True, type="primary")
    else:
        # Show Results button (Final question)
        # FIX: Changed type="success" to type="primary"
        st.button("Show Results", on_click=record_answer, use_container_width=True, type="primary")


def render_results_page():
    """Calculates and displays the final quiz results."""
    
    st.title("✅ Quiz Complete!")
    st.markdown("---")

    score = 0
    results_breakdown = []
    
    # Calculate score
    for i, question_data in enumerate(st.session_state.quiz_questions):
        user_answer = st.session_state.user_answers.get(i)
        correct_answer = question_data["correct_answer"]
        
        is_correct = (user_answer == correct_answer)
        
        if is_correct:
            score += 1
        
        results_breakdown.append({
            "question": question_data["question"],
            "user_answer": user_answer if user_answer is not None else "No Answer Selected",
            "correct_answer": correct_answer,
            "is_correct": is_correct
        })

    # --- Score Summary ---
    st.subheader("Overall Performance")
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Total Questions", st.session_state.quiz_length)
    col2.metric("Correct Answers", score)
    col3.metric("Score", f"{(score / st.session_state.quiz_length) * 100:.1f}%")

    st.markdown("---")
    
    # --- Detailed Breakdown ---
    st.subheader("Detailed Breakdown")
    for i, result in enumerate(results_breakdown):
        status_icon = "✅" if result["is_correct"] else "❌"
        
        with st.expander(f"{status_icon} Question {i+1}: {result['question'][:70]}..."):
            st.write(f"**Question:** {result['question']}")
            
            if result["is_correct"]:
                st.success(f"**Your Answer:** {result['user_answer']} (Correct)")
            else:
                st.error(f"**Your Answer:** {result['user_answer']}")
                st.info(f"**Correct Answer:** {result['correct_answer']}")

    st.markdown("---")
    
    # Restart Button
    st.button("Start New Quiz", on_click=restart_quiz, use_container_width=True)

# --- Main Application Logic ---

def main():
    initialize_session_state()

    if st.session_state.page == "setup":
        render_setup_page()
    elif st.session_state.page == "quiz":
        render_quiz_page()
    elif st.session_state.page == "results":
        render_results_page()

if __name__ == "__main__":
    # Ensure QA_DATA is defined (by importing from quiz_data.py) before running
    if 'QA_DATA' not in globals():
        st.error("Error: Could not find 'QA_DATA'. Please ensure 'quiz_data.py' is in the same directory and contains the dictionary.")
    else:
        main()
