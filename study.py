import streamlit as st
import random
import json
import os
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
    if 'quiz_mode' not in st.session_state:
        st.session_state.quiz_mode = 'End-of-Quiz' # 'End-of-Quiz' or 'Immediate-Feedback'
    if 'show_feedback' not in st.session_state:
        st.session_state.show_feedback = False
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'attempted' not in st.session_state:
        st.session_state.attempted = 0
    if 'adaptive_mode' not in st.session_state:
        st.session_state.adaptive_mode = False
# --- Callback Functions ---

# --- Adaptive Mode JSON File Utilities ---
WRONG_QUESTIONS_FILE = "wrong_questions.json"

def load_wrong_questions():
    if not os.path.exists(WRONG_QUESTIONS_FILE):
        return {}
    with open(WRONG_QUESTIONS_FILE, "r") as f:
        try:
            return json.load(f)
        except Exception:
            return {}

def save_wrong_questions(data):
    with open(WRONG_QUESTIONS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_wrong_question(chapter, question_data):
    data = load_wrong_questions()
    if chapter not in data:
        data[chapter] = []
    # Avoid duplicates
    if not any(q["question"] == question_data["question"] for q in data[chapter]):
        data[chapter].append(question_data)
        save_wrong_questions(data)

def remove_wrong_question(chapter, question_data):
    data = load_wrong_questions()
    if chapter in data:
        data[chapter] = [q for q in data[chapter] if q["question"] != question_data["question"]]
        if not data[chapter]:
            del data[chapter]
        save_wrong_questions(data)


# --- Callback Functions ---

def start_quiz(selected_chapters, question_count, quiz_mode):
    """
    Called when the 'Start Quiz' button is pressed.
    Gathers questions, shuffles them, and transitions to the quiz page.
    """
    if not selected_chapters:
        st.error("Please select at least one chapter.")
        return

    # Gather all questions from selected chapters
    all_questions = []
    for chapter in selected_chapters:
        all_questions.extend(QA_DATA.get(chapter, []))

    if not all_questions:
        st.error("No questions found for the selected chapters.")
        return

    # --- Adaptive Mode: Pull from wrong_questions.json first ---
    quiz_questions = []
    if st.session_state.adaptive_mode:
        wrong_data = load_wrong_questions()
        # Pull wrong questions for selected chapters
        for chapter in selected_chapters:
            quiz_questions.extend(wrong_data.get(chapter, []))
        # Remove duplicates from all_questions
        wrong_questions_set = set(q["question"] for q in quiz_questions)
        remaining_questions = [q for q in all_questions if q["question"] not in wrong_questions_set]
        # Fill up to question_count
        count = min(question_count, len(quiz_questions) + len(remaining_questions))
        quiz_questions = quiz_questions[:question_count]
        if len(quiz_questions) < count:
            quiz_questions += random.sample(remaining_questions, count - len(quiz_questions))
    else:
        count = min(question_count, len(all_questions))
        quiz_questions = random.sample(all_questions, count)

    st.session_state.quiz_questions = quiz_questions
    st.session_state.current_index = 0
    st.session_state.user_answers = {}
    st.session_state.quiz_length = len(st.session_state.quiz_questions)
    st.session_state.selected_chapters = selected_chapters
    st.session_state.quiz_mode = quiz_mode
    st.session_state.show_feedback = False
    st.session_state.score = 0
    st.session_state.attempted = 0
    st.session_state.page = "quiz"

def record_answer():
    """Records the user's selected answer and shows feedback (if immediate mode)."""
    current_q_index = st.session_state.current_index
    # Check if the user selected an answer
    if st.session_state.last_selection is None:
        st.warning("Please select an answer before proceeding.")
        return
    # Record the answer
    st.session_state.user_answers[current_q_index] = st.session_state.last_selection

    # --- Adaptive Mode: Update wrong_questions.json ---
    current_q = st.session_state.quiz_questions[current_q_index]
    # Find chapter for current question
    chapter = None
    for ch in st.session_state.selected_chapters:
        if any(q["question"] == current_q["question"] for q in QA_DATA.get(ch, [])):
            chapter = ch
            break
    is_correct = (st.session_state.last_selection == current_q["correct_answer"])
    if chapter:
        if not is_correct:
            add_wrong_question(chapter, current_q)
        else:
            remove_wrong_question(chapter, current_q)

    if st.session_state.quiz_mode == 'Immediate-Feedback':
        # Show feedback for the current question
        st.session_state.show_feedback = True
        # Update score immediately for display purposes
        # Only update the score if it hasn't been attempted yet (to prevent re-scoring)
        if current_q_index not in st.session_state.attempted_questions:
            st.session_state.attempted_questions[current_q_index] = True
            st.session_state.attempted += 1
            if is_correct:
                st.session_state.score += 1
    else:
        # End-of-Quiz mode: just advance to the next question/results
        advance_question()

def advance_question():
    """Advances the current index or moves to the results page."""
    current_q_index = st.session_state.current_index
    quiz_length = st.session_state.quiz_length
    
    # Clear feedback and selection for the next question
    st.session_state.show_feedback = False
    st.session_state.last_selection = None

    if current_q_index < quiz_length - 1:
        st.session_state.current_index += 1
    else:
        st.session_state.page = "results"


def restart_quiz():
    """Resets the application back to the setup page."""
    initialize_session_state()
    st.session_state.page = "setup"
    st.session_state.current_index = 0
    st.session_state.attempted_questions = {} # Reset specific tracking for immediate mode

# --- UI Rendering Functions ---

def render_setup_page():
    """Renders the chapter selection, quiz length, and mode setup UI."""
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

    # Adaptive Mode toggle
    st.subheader("2. Adaptive Mode")
    adaptive_mode = st.checkbox(
        "Enable Adaptive Mode (focus on questions you got wrong)",
        value=st.session_state.adaptive_mode,
        key="setup_adaptive_mode"
    )
    st.session_state.adaptive_mode = adaptive_mode

    # Quiz Mode selection
    st.subheader("3. Select Quiz Mode")
    quiz_mode = st.radio(
        "How do you want to receive feedback?",
        options=['End-of-Quiz', 'Immediate-Feedback'],
        index=0 if st.session_state.quiz_mode == 'End-of-Quiz' else 1,
        key="setup_quiz_mode",
        help="End-of-Quiz: Results shown only after the last question. Immediate-Feedback: Results shown right after you answer each question."
    )

    # Question count slider
    if adaptive_mode:
        wrong_data = load_wrong_questions()
        wrong_count = sum(len(wrong_data.get(c, [])) for c in chapters_selection)
        main_count = sum(len(QA_DATA.get(c, [])) for c in chapters_selection)
        max_questions = min(main_count, wrong_count + main_count)
    else:
        max_questions = sum(len(QA_DATA.get(c, [])) for c in chapters_selection)

    st.subheader(f"4. Choose Quiz Length (Max: {max_questions})")

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
        args=(chapters_selection, question_count, quiz_mode),
        use_container_width=True,
        type="primary"
    )


def render_quiz_page():
    """Renders the current question and answer options based on the selected mode."""
    
    if 'attempted_questions' not in st.session_state:
        st.session_state.attempted_questions = {}

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
    
    # Display Score if in Immediate Feedback Mode
    if st.session_state.quiz_mode == 'Immediate-Feedback':
        col1, col2 = st.columns([1, 2])
        col1.metric("Current Score", f"{st.session_state.score} / {st.session_state.attempted}")
        col2.markdown(f"Question **{current_index + 1}** of **{quiz_length}**")
    else:
        st.markdown(f"Question **{current_index + 1}** of **{quiz_length}**")
    
    st.progress((current_index + 1) / quiz_length)
    st.markdown("---")
    
    # --- Question Display ---
    st.header(f"Question {current_index + 1}")
    st.write(current_q["question"])
    
    # --- Options (Radio Buttons) ---
    selection = st.radio(
        "Select your answer:",
        current_q["options"],
        index=None, # Start with no selection
        key=f"q_{current_index}_radio",
        disabled=st.session_state.show_feedback and st.session_state.quiz_mode == 'Immediate-Feedback'
    )
    
    # Manually store the selection
    st.session_state.last_selection = selection

    st.markdown("---")

    # --- Navigation and Feedback Logic ---

    if st.session_state.quiz_mode == 'Immediate-Feedback':
        # --- Immediate Feedback Mode ---
        
        if not st.session_state.show_feedback:
            # Button to submit the answer and check it
            st.button(
                "Submit Answer", 
                on_click=record_answer, 
                use_container_width=True, 
                type="primary",
                disabled=selection is None
            )
        else:
            # Display feedback
            is_correct = (st.session_state.last_selection == current_q["correct_answer"])
            
            if is_correct:
                st.success("✅ Correct! Great job.")
            else:
                st.error("❌ Incorrect.")
                st.info(f"The correct answer was: **{current_q['correct_answer']}**")

            # Button to move to the next question or results
            button_label = "Show Results" if current_index == quiz_length - 1 else "Continue to Next Question"
            
            # Use secondary for continue button in immediate mode
            st.button(
                button_label, 
                on_click=advance_question, 
                use_container_width=True, 
                type="secondary"
            )

    else:
        # --- End-of-Quiz Mode (Original Behavior) ---
        
        # Button to move to the next question or results
        button_label = "Show Results" if current_index == quiz_length - 1 else "Next Question"
        
        st.button(
            button_label,
            on_click=record_answer, # record_answer handles the advancement in this mode
            use_container_width=True,
            type="primary"
        )


def render_results_page():
    """Calculates and displays the final quiz results."""
    
    st.title("✅ Quiz Complete!")
    st.markdown("---")

    score = 0
    results_breakdown = []
    
    # Calculate score (re-calculate in End-of-Quiz mode, or use cached score in Immediate mode)
    if st.session_state.quiz_mode == 'End-of-Quiz':
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
    else: # Immediate-Feedback mode uses pre-calculated score/attempted
        score = st.session_state.score
        total_attempted = st.session_state.attempted
        
        # In Immediate-Feedback mode, rebuild breakdown for review
        for i, question_data in enumerate(st.session_state.quiz_questions):
            user_answer = st.session_state.user_answers.get(i)
            correct_answer = question_data["correct_answer"]
            is_correct = (user_answer == correct_answer)
            
            results_breakdown.append({
                "question": question_data["question"],
                "user_answer": user_answer if user_answer is not None else "No Answer Selected",
                "correct_answer": correct_answer,
                "is_correct": is_correct
            })
    
    quiz_length = len(st.session_state.quiz_questions)

    # --- Score Summary ---
    st.subheader("Overall Performance")
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Total Questions", quiz_length)
    col2.metric("Correct Answers", score)
    col3.metric("Score", f"{(score / quiz_length) * 100:.1f}%" if quiz_length > 0 else "0.0%")

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
    # A simple check to ensure data is likely loaded, though the main error check is in the chat history
    if 'QA_DATA' in globals() or 'QA_DATA' in st.session_state:
        main()
    else:
        # This fallback is unlikely to be hit if 'quiz_data.py' is present
        initialize_session_state() 
        render_setup_page()
