"""
Data structure to store Questions and Answers, organized by chapter for Multiple Choice Quizzing.

The structure is a dictionary where:
- Keys are the Chapter names (strings).
- Values are a list of dictionaries, where each inner dictionary
  represents a single question.
- Each question dictionary includes 'options' (list of strings) and 'correct_answer' (string).
"""

QA_DATA = {
    "Chapter 1 - Artificial Intelligence": [
        {
            "question": "Who is considered the 'Father of Artificial Intelligence'?",
            "options": ["Alan Turing", "John McCarthy", "Herbert Simon", "Marvin Minsky"],
            "correct_answer": "John McCarthy"
        },
        {
            "question": "Which is an example of Reactive AI?",
            "options": ["IBM Watson", "Deep Blue", "Siri", "AlphaGo"],
            "correct_answer": "Deep Blue"
        },
        {
            "question": "Which of the following is a Learning-based System?",
            "options": ["Rule-based chatbot", "Netflix recommendations", "ELIZA", "Traffic light controller"],
            "correct_answer": "Netflix recommendations"
        },
        {
            "question": "Which AI type aspires to understand emotions?",
            "options": ["Theory of Mind", "Self-Aware AI", "Limited Memory", "Reactive Machines"],
            "correct_answer": "Theory of Mind"
        },
        {
            "question": "Which measure tells us how many actual positives were identified?",
            "options": ["Precision", "Recall", "Accuracy", "F1-Score"],
            "correct_answer": "Recall"
        },
        {
            "question": "A Loss Function is used to:",
            "options": ["Update weights", "Measure prediction error", "Store past data", "Reduce noise in inputs"],
            "correct_answer": "Measure prediction error"
        },
        {
            "question": "A chatbot with fixed responses is an example of:",
            "options": ["Rule-based AI", "Learning AI", "Adaptive AI", "Self-aware AI"],
            "correct_answer": "Rule-based AI"
        },
        {
            "question": "What problem does overfitting create?",
            "options": [
                "The model fails to learn anything from the data.",
                "The model performs well on training data but poorly on unseen data.",
                "The training process takes too long.",
                "The model is too simple to capture patterns."
            ],
            "correct_answer": "The model performs well on training data but poorly on unseen data."
        },
        {
            "question": "AI that operates within its programmed scope is called [...] AI.",
            "options": ["Strong (General)", "Self-Aware", "Narrow (Weak)", "Limited Memory"],
            "correct_answer": "Narrow (Weak)"
        },
        {
            "question": "One full pass through a dataset is called an [...] .",
            "options": ["Iteration", "Step", "Epoch", "Batch"],
            "correct_answer": "Epoch"
        },
        {
            "question": "A self-driving car is an example of [...] memory AI.",
            "options": ["Reactive", "Limited", "Theory of Mind", "Self-Aware"],
            "correct_answer": "Limited"
        },
        {
            "question": "In the analogy, an algorithm is like a [...] .",
            "options": ["Ingredient", "Toolbox", "Recipe", "Oven"],
            "correct_answer": "Recipe"
        },
        {
            "question": "[...] is used to update weights in neural networks.",
            "options": ["Forward propagation", "Gradient descent", "Backpropagation", "Normalization"],
            "correct_answer": "Backpropagation"
        },
        {
            "question": "Define Artificial Intelligence in one sentence.",
            "options": [
                "AI is the study of how computers interact with databases.",
                "AI is the science of creating machines capable of performing cognitive functions like learning, reasoning, and decision-making.",
                "AI is a set of rules used to automate simple tasks.",
                "AI is the process of generating new data from old data."
            ],
            "correct_answer": "AI is the science of creating machines capable of performing cognitive functions like learning, reasoning, and decision-making."
        },
    ],
    "Chapter 2 - Foundations of AI": [
        {
            "question": "Which of the following best describes Deep Learning?",
            "options": ["Decision trees with few layers", "Neural networks with many layers", "A separate field from AI", "Rule-based expert systems"],
            "correct_answer": "Neural networks with many layers"
        },
        {
            "question": "Which is a correct hierarchy?",
            "options": ["AI $\\subset$ ML $\\subset$ DL", "DL $\\subset$ ML $\\subset$ AI", "ML $\\subset$ AI $\\subset$ DL", "AI $\\subset$ DL $\\subset$ ML"],
            "correct_answer": "DL $\\subset$ ML $\\subset$ AI"
        },
        {
            "question": "Which agent acts only on current percepts?",
            "options": ["Model-based reflex", "Goal-based", "Simple reflex", "Utility-based"],
            "correct_answer": "Simple reflex"
        },
        {
            "question": "PEAS stands for:",
            "options": ["Performance, Environment, Actions, Sensors", "Performance, Environment, Actuators, Sensors", "Planning, Execution, Actions, Sensors", "Performance, Estimation, Analysis, Simulation"],
            "correct_answer": "Performance, Environment, Actuators, Sensors"
        },
        {
            "question": "In the PEAS framework, cameras on a self-driving car are:",
            "options": ["Sensors", "Actuators", "Performance measure", "Environment"],
            "correct_answer": "Sensors"
        },
        {
            "question": "A GPS system that finds the shortest path is an example of:",
            "options": ["Reflex agent", "Goal-based agent", "Utility-based agent", "Omniscient agent"],
            "correct_answer": "Goal-based agent"
        },
        {
            "question": "What is the main difference between goal-based and utility-based agents?",
            "options": [
                "Utility-based agents are faster than goal-based agents.",
                "Goal-based agents only work in deterministic environments.",
                "Goal-based agents aim to achieve a target condition, while utility-based agents optimize overall success with trade-offs.",
                "Utility-based agents use machine learning, goal-based agents use rules."
            ],
            "correct_answer": "Goal-based agents aim to achieve a target condition, while utility-based agents optimize overall success with trade-offs."
        },
        {
            "question": "Why is omniscience impossible in real-world agents?",
            "options": [
                "The environment changes too quickly.",
                "Agents cannot know exact outcomes of all actions; they act with limited information.",
                "Computational resources are always limited.",
                "Omniscience is only relevant for model-based agents."
            ],
            "correct_answer": "Agents cannot know exact outcomes of all actions; they act with limited information."
        },
        {
            "question": "Name two ethical principles in data collection.",
            "options": [
                "Efficiency and speed.",
                "Informed consent and privacy/confidentiality.",
                "Model-bias reduction and high accuracy.",
                "Centralization and storage security."
            ],
            "correct_answer": "Informed consent and privacy/confidentiality."
        },
    ],
    "Chapter 3 - Search Algorithms in AI": [
        {
            "question": "In AI, a problem is formally defined by:",
            "options": ["Initial state, Goal state, Actions, Path cost", "Data, Model, Evaluation", "Training, Testing, Deployment", "Input, Output, Feedback"],
            "correct_answer": "Initial state, Goal state, Actions, Path cost"
        },
        {
            "question": "The transition model in problem-solving specifies:",
            "options": ["Optimal path", "Rules of state change after actions", "Goal satisfaction test", "Path cost function"],
            "correct_answer": "Rules of state change after actions"
        },
        {
            "question": "Which component of a node helps reconstruct the solution path?",
            "options": ["State", "Parent pointer", "Path cost", "Action"],
            "correct_answer": "Parent pointer"
        },
        {
            "question": "Which data structure is used in Depth-First Search (DFS)?",
            "options": ["Queue", "Stack", "Priority queue", "Hash table"],
            "correct_answer": "Stack"
        },
        {
            "question": "Which data structure is used in Breadth-First Search (BFS)?",
            "options": ["Stack", "Queue", "Hash map", "Binary heap"],
            "correct_answer": "Queue"
        },
        {
            "question": "Which of the following is true about DFS?",
            "options": ["Always finds shortest path", "Uses stack (LIFO)", "Uses heuristics", "Space-efficient but not complete"],
            "correct_answer": "Uses stack (LIFO)"
        },
        {
            "question": "The cost function $g(n)$ in $A^{*}$ represents the:",
            "options": ["Estimated cost to goal", "Total path cost (estimated)", "Path cost so far", "Heuristic value"],
            "correct_answer": "Path cost so far"
        },
        {
            "question": "Greedy Best-First Search is optimal if the heuristic is admissible. (True/False)",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "If $g(n)=0$ in $A^{*}$, what does it reduce to?",
            "options": ["BFS", "DFS", "GBFS (Greedy Best First Search)", "Iterative Deepening Search"],
            "correct_answer": "GBFS (Greedy Best First Search)"
        },
        {
            "question": "Which search doesn't need domain-specific knowledge?",
            "options": ["$A^{*}$ Search", "Greedy Best First Search", "Uninformed search (BFS or DFS)", "Hill Climbing"],
            "correct_answer": "Uninformed search (BFS or DFS)"
        },
    ],
    "Chapter 4 - Machine Learning": [
        {
            "question": "Machine Learning is best defined as:",
            "options": ["Programming computers with fixed rules", "Giving machines ability to learn without explicit programming", "Simple data entry automation", "Artificial General Intelligence"],
            "correct_answer": "Giving machines ability to learn without explicit programming"
        },
        {
            "question": "In supervised learning, the training data consists of:",
            "options": ["Only inputs without outputs", "Inputs and corresponding labeled outputs", "Random unlabeled examples", "Reinforcement signals"],
            "correct_answer": "Inputs and corresponding labeled outputs"
        },
        {
            "question": "Predicting house prices from historical data is an example of:",
            "options": ["Classification", "Regression", "Clustering", "Reinforcement"],
            "correct_answer": "Regression"
        },
        {
            "question": "Classifying emails as spam or not spam is an example of:",
            "options": ["Regression", "Classification", "Clustering", "Reinforcement"],
            "correct_answer": "Classification"
        },
        {
            "question": "Which algorithm is NOT supervised learning?",
            "options": ["Logistic regression", "K-means", "Decision tree", "k-Nearest Neighbors"],
            "correct_answer": "K-means"
        },
        {
            "question": "In unsupervised learning, the training data consists of:",
            "options": ["Inputs and labeled outputs", "Reinforcement rewards", "Random unlabeled examples", "Expert-curated feature sets"],
            "correct_answer": "Random unlabeled examples"
        },
        {
            "question": "The data points closest to the SVM hyperplane are called:",
            "options": ["Centroids", "Vectors", "Support vectors", "Hyperparameters"],
            "correct_answer": "Support vectors"
        },
        {
            "question": "The tree-like diagram used in hierarchical clustering is called a [...] .",
            "options": ["Decision tree", "Phylogenetic chart", "Dendrogram", "Scatter plot"],
            "correct_answer": "Dendrogram"
        },
        {
            "question": "In association rule mining, Lift(A $\\rightarrow$ B) > 1 means the items have a [...] relationship.",
            "options": ["Negative", "Neutral", "Positive", "Causal"],
            "correct_answer": "Positive"
        },
        {
            "question": "PCA is a dimensionality reduction technique. (True/False)",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
    ],
    "Chapter 5 - Reinforcement Learning": [
        {
            "question": "Reinforcement Learning differs from supervised learning because:",
            "options": ["RL uses labeled data", "RL learns from rewards and penalties", "RL requires no feedback", "RL is unsupervised clustering"],
            "correct_answer": "RL learns from rewards and penalties"
        },
        {
            "question": "Which is NOT a core element of RL?",
            "options": ["Agent", "State", "Reward", "Epoch"],
            "correct_answer": "Epoch"
        },
        {
            "question": "The function mapping states to actions in RL is called:",
            "options": ["Value function", "Reward function", "Policy", "Model"],
            "correct_answer": "Policy"
        },
        {
            "question": "In RL, the immediate feedback signal is:",
            "options": ["Reward", "State", "Action", "Policy"],
            "correct_answer": "Reward"
        },
        {
            "question": "The long-term desirability of states is represented by:",
            "options": ["Reward", "Policy", "Value function", "Model"],
            "correct_answer": "Value function"
        },
        {
            "question": "Which RL component simulates the environment?",
            "options": ["Model", "Policy", "Reward", "Value function"],
            "correct_answer": "Model"
        },
        {
            "question": "Which of these is a model-free method?",
            "options": ["Value iteration", "Q-Learning", "Monte Carlo Tree Search", "Dynamic Programming"],
            "correct_answer": "Q-Learning"
        },
        {
            "question": "Which of these is a model-based method?",
            "options": ["SARSA", "REINFORCE", "Value iteration", "Q-Learning"],
            "correct_answer": "Value iteration"
        },
        {
            "question": "[...]-greedy algorithm balances exploration and exploitation by:",
            "options": [
                "Always choosing best action",
                "Always choosing random action",
                "Choosing random with probability $\\epsilon$",
                "Ignoring randomness"
            ],
            "correct_answer": "Choosing random with probability $\\epsilon$"
        },
        {
            "question": "In Q-learning, Q(s,a) represents:",
            "options": ["Reward function", "State value", "Action-state value", "Policy"],
            "correct_answer": "Action-state value"
        },
        {
            "question": "Reinforcement Learning uses trial and error to learn. (True/False)",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Policy in RL maps rewards to states. (True/False)",
            "options": ["True", "False (it maps states to actions)"],
            "correct_answer": "False (it maps states to actions)"
        },
    ]
}
