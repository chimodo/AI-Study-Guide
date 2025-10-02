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
            "question": "Who is considered the “Father of Artificial Intelligence”?",
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
            "question": "AI is only used in robotics.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "Data is to AI what experience is to humans.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Self-aware AI currently powers chatbots like ChatGPT.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "Overfitting happens when a model memorizes training data but fails on new data.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Theory of Mind AI can currently detect human frustration.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "Autonomous vehicles use Limited Memory AI.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "__________ coined the term Artificial Intelligence.",
            "options": ["Alan Turing", "Marvin Minsky", "John McCarthy", "Geoffrey Hinton"],
            "correct_answer": "John McCarthy"
        },
        {
            "question": "AI that operates within its programmed scope is called __________ AI.",
            "options": ["Strong (General)", "Narrow (Weak)", "Reactive", "Self-Aware"],
            "correct_answer": "Narrow (Weak)"
        },
        {
            "question": "In training, the difference between prediction and actual result is called __________.",
            "options": ["Gradient", "Feature", "Error (or Loss)", "Bias"],
            "correct_answer": "Error (or Loss)"
        },
        {
            "question": "One full pass through a dataset is called an __________.",
            "options": ["Iteration", "Epoch", "Batch", "Step"],
            "correct_answer": "Epoch"
        },
        {
            "question": "A self-driving car is an example of __________ memory AI.",
            "options": ["Perfect", "Infinite", "Limited", "Reactive"],
            "correct_answer": "Limited"
        },
        {
            "question": "Data is the __________ of AI.",
            "options": ["Brain", "Engine", "Foundation", "Output"],
            "correct_answer": "Foundation"
        },
        {
            "question": "In the analogy, an algorithm is like a __________.",
            "options": ["Ingredient", "Dish", "Recipe", "Cook"],
            "correct_answer": "Recipe"
        },
        {
            "question": "__________ is used to update weights in neural networks.",
            "options": ["Loss Function", "Activation Function", "Backpropagation", "Forward Pass"],
            "correct_answer": "Backpropagation"
        },
        {
            "question": "Define Artificial Intelligence in one sentence.",
            "options": [
                "AI is the process of extracting knowledge from data.",
                "AI is the study of creating expert systems based on human logic.",
                "AI is the science of creating machines capable of performing cognitive functions like learning, reasoning, and decision-making.",
                "AI refers exclusively to robots capable of self-replication."
            ],
            "correct_answer": "AI is the science of creating machines capable of performing cognitive functions like learning, reasoning, and decision-making."
        },
        {
            "question": "Give two real-world applications of AI in healthcare.",
            "options": [
                "Financial fraud detection and customer support.",
                "Medical imaging (tumor detection) and drug discovery.",
                "Weather forecasting and game playing.",
                "Autonomous vehicle navigation and spam filtering."
            ],
            "correct_answer": "Medical imaging (tumor detection) and drug discovery."
        },
        {
            "question": "What problem does overfitting create?",
            "options": [
                "The model is too simple to learn the data.",
                "The model performs well on training data but poorly on unseen data.",
                "The model takes too long to train.",
                "The model requires too much memory."
            ],
            "correct_answer": "The model performs well on training data but poorly on unseen data."
        },
        {
            "question": "Give one example each of Reactive AI and Adaptive AI.",
            "options": [
                "Siri (Reactive), Tesla Autopilot (Adaptive).",
                "Deep Blue (Reactive), AlphaGo (Adaptive).",
                "Netflix (Reactive), Spam Filter (Adaptive).",
                "Traffic light (Reactive), IBM Watson (Adaptive)."
            ],
            "correct_answer": "Deep Blue (Reactive), AlphaGo (Adaptive)."
        }
    ],
    "Chapter 2 - Foundations of AI": [
        # --- Q1-Q41 (Original Multiple Choice) ---
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
            "question": "An AI system using CNNs to recognize images falls under:",
            "options": ["AI only", "Machine Learning", "Deep Learning", "Rule-based AI"],
            "correct_answer": "Deep Learning"
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
            "question": "Which agent chooses actions that maximize a numerical success score?",
            "options": ["Reflex agent", "Model-based agent", "Goal-based agent", "Utility-based agent"],
            "correct_answer": "Utility-based agent"
        },
        {
            "question": "In PEAS, the performance measure for a self-driving car includes:",
            "options": ["Road conditions", "Steering, brakes, accelerator", "Safety, passenger comfort, traffic law compliance", "GPS sensors"],
            "correct_answer": "Safety, passenger comfort, traffic law compliance"
        },
        {
            "question": "Rationality in AI means:",
            "options": ["Always achieving goals", "Choosing the best action given available information", "Knowing exact outcomes of every action", "Never making mistakes"],
            "correct_answer": "Choosing the best action given available information"
        },
        {
            "question": "Which problem representation includes Initial state, Goal state, Actions, and Path cost?",
            "options": ["Rationality model", "PEAS framework", "Problem-solving in AI", "Data validation"],
            "correct_answer": "Problem-solving in AI"
        },
        {
            "question": "Which is NOT an uninformed search strategy?",
            "options": ["BFS", "DFS", "A*", "Uniform Cost Search"],
            "correct_answer": "A*"
        },
        {
            "question": "Which AI approach uses facts and reasoning rules?",
            "options": ["Knowledge-based problem solving", "Search-based problem solving", "CSP solving", "Reinforcement learning"],
            "correct_answer": "Knowledge-based problem solving"
        },
        {
            "question": "A robot vacuum that remembers obstacles is:",
            "options": ["Reflex agent", "Model-based reflex agent", "Utility-based agent", "Goal-based agent"],
            "correct_answer": "Model-based reflex agent"
        },
        {
            "question": "In AI, Path Cost refers to:",
            "options": ["Number of moves/time/resources used to reach goal", "Total nodes explored", "Number of heuristics applied", "Success score"],
            "correct_answer": "Number of moves/time/resources used to reach goal"
        },
        {
            "question": "An omniscient agent is defined as:",
            "options": ["Agent that updates its knowledge", "Agent that knows outcomes of all actions in advance", "Agent that learns heuristics", "Agent that acts only on current percepts"],
            "correct_answer": "Agent that knows outcomes of all actions in advance"
        },
        {
            "question": "Which of these is structured data?",
            "options": ["Social media posts", "Transaction records", "JSON from an API", "Audio recordings"],
            "correct_answer": "Transaction records"
        },
        {
            "question": "Which is unstructured data?",
            "options": ["CSV table", "Tweets and Instagram captions", "JSON logs", "SQL database rows"],
            "correct_answer": "Tweets and Instagram captions"
        },
        {
            "question": "Semi-structured data usually uses:",
            "options": ["Plain text only", "Fixed relational schema", "Tags/keys like JSON or XML", "Audio and video formats"],
            "correct_answer": "Tags/keys like JSON or XML"
        },
        {
            "question": "Which data collection method requires human entry?",
            "options": ["APIs", "Automated sensors", "Manual surveys", "Web scraping"],
            "correct_answer": "Manual surveys"
        },
        {
            "question": "IoT devices collecting temperature are an example of:",
            "options": ["Manual entry", "Automated sensors", "Transactional systems", "CSP data"],
            "correct_answer": "Automated sensors"
        },
        {
            "question": "E-commerce scraping is an example of:",
            "options": ["Transactional data", "Web scraping", "Manual data collection", "Structured table entry"],
            "correct_answer": "Web scraping"
        },
        {
            "question": "POS (Point of Sale) machine data is:",
            "options": ["Manual entry", "Automated sensors", "Transactional systems", "Semi-structured"],
            "correct_answer": "Transactional systems"
        },
        {
            "question": "Which practice ensures consistency and trustworthiness of data?",
            "options": ["Data cleaning", "Data integrity", "Data validation", "Outlier detection"],
            "correct_answer": "Data integrity"
        },
        {
            "question": "Removing duplicates and filling missing values is:",
            "options": ["Data validation", "Data cleaning", "Data consistency", "Data security"],
            "correct_answer": "Data cleaning"
        },
        {
            "question": "Checking emails for correct format is:",
            "options": ["Data cleaning", "Data validation", "Data auditing", "Data structuring"],
            "correct_answer": "Data validation"
        },
        {
            "question": "Which ethical principle ensures participants know how their data will be used?",
            "options": ["Privacy", "Informed consent", "Bias minimization", "Legal compliance"],
            "correct_answer": "Informed consent"
        },
        {
            "question": "The mean of [10, 20, 30] is:",
            "options": ["20", "15", "25", "10"],
            "correct_answer": "20"
        },
        {
            "question": "Median of [5, 10, 20, 40, 50]?",
            "options": ["20", "15", "25", "30"],
            "correct_answer": "20"
        },
        {
            "question": "Mode of [2, 3, 3, 5]?",
            "options": ["2", "3", "5", "None"],
            "correct_answer": "3"
        },
        {
            "question": "Which metric is best for categorical data?",
            "options": ["Mean", "Median", "Mode", "Variance"],
            "correct_answer": "Mode"
        },
        {
            "question": "IQR = Q3 – Q1 measures:",
            "options": ["Central tendency", "Spread of middle 50% of data", "Accuracy of model", "Validation errors"],
            "correct_answer": "Spread of middle 50% of data"
        },
        {
            "question": "A value below Q1–1.5×IQR is:",
            "options": ["Normal value", "Outlier (low)", "Outlier (high)", "Mean"],
            "correct_answer": "Outlier (low)"
        },
        {
            "question": "A value above Q3+1.5×IQR is:",
            "options": ["Median", "Outlier (high)", "Normal range", "Mode"],
            "correct_answer": "Outlier (high)"
        },
        {
            "question": "Example of AI in healthcare:",
            "options": ["Fraud detection", "Medical imaging", "Dynamic pricing", "Sentiment analysis"],
            "correct_answer": "Medical imaging"
        },
        {
            "question": "Example of AI in finance:",
            "options": ["Recommendation systems", "Fraud detection", "Traffic management", "Machine vision"],
            "correct_answer": "Fraud detection"
        },
        {
            "question": "Example of AI in e-commerce:",
            "options": ["Drug discovery", "Chatbots & recommendations", "Route planning", "Image recognition"],
            "correct_answer": "Chatbots & recommendations"
        },
        {
            "question": "Example of AI in marketing:",
            "options": ["Predictive analytics for ad targeting", "Image classification", "Speech-to-text", "Chess playing"],
            "correct_answer": "Predictive analytics for ad targeting"
        },
        {
            "question": "Example of AI in autonomous vehicles:",
            "options": ["Spam filtering", "Route planning & obstacle detection", "Sentiment analysis", "Fraud prevention"],
            "correct_answer": "Route planning & obstacle detection"
        },
        {
            "question": "Which data type is common in NoSQL databases?",
            "options": ["Structured", "Unstructured", "Semi-structured", "Binary"],
            "correct_answer": "Semi-structured"
        },
        {
            "question": "Which process ensures no garbage data enters an AI system?",
            "options": ["Data collection", "Data validation", "Data cleaning", "Data storage"],
            "correct_answer": "Data validation"
        },
        # --- Q42-Q55 (True/False converted to Multiple Choice) ---
        {
            "question": "Deep Learning is a subset of Machine Learning.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Reflex agents act based only on the current percept.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Model-based reflex agents maintain an internal model of the world.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Goal-based agents choose actions to achieve predefined goals.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Utility-based agents only act randomly.",
            "options": ["True", "False (they maximize a utility score)", "True, when in uncertain environments", "False, they are strictly rule-based"],
            "correct_answer": "False (they maximize a utility score)"
        },
        {
            "question": "BFS is a blind search method that guarantees the shortest path.",
            "options": ["True", "False", "Only if all path costs are equal", "Only in an infinite state space"],
            "correct_answer": "True"
        },
        {
            "question": "DFS guarantees the shortest path.",
            "options": ["True", "False", "Only in a finite state space", "Only with a good heuristic"],
            "correct_answer": "False"
        },
        {
            "question": "Greedy Best-First Search combines path cost and heuristic.",
            "options": ["True", "False (that’s A*)", "Only if the heuristic is consistent", "Only if the path cost is zero"],
            "correct_answer": "False (that’s A*)"
        },
        {
            "question": "A* search is an informed search strategy.",
            "options": ["True", "False", "It is only partially informed", "It is an uninformed search"],
            "correct_answer": "True"
        },
        {
            "question": "Problem-solving in AI requires defining initial state, goal state, actions, and path cost.",
            "options": ["True", "False (path cost is optional)"],
            "correct_answer": "True"
        },
        {
            "question": "Exam scheduling with no conflicts is an example of a Constraint Satisfaction Problem.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Structured data is best represented in tables with rows and columns.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Tweets and social media posts are examples of structured data.",
            "options": ["True", "False (they are unstructured)"],
            "correct_answer": "False (they are unstructured)"
        },
        {
            "question": "JSON and XML are examples of semi-structured data.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        # --- Q56-Q71 (Fill in the Blanks converted to Multiple Choice) ---
        {
            "question": "Rational agents choose actions to maximize expected:",
            "options": ["Path cost", "Goal state", "Utility", "Reward"],
            "correct_answer": "Utility"
        },
        {
            "question": "Rationality is not the same as __________, which assumes knowing exact outcomes.",
            "options": ["Adaptivity", "Omniscience", "Completeness", "Optimality"],
            "correct_answer": "Omniscience"
        },
        {
            "question": "BFS explores nodes level by:",
            "options": ["Branch", "Depth", "Cost", "Level"],
            "correct_answer": "Level"
        },
        {
            "question": "DFS explores as far as possible along a __________ before backtracking.",
            "options": ["Node", "Queue", "Branch", "Heuristic"],
            "correct_answer": "Branch"
        },
        {
            "question": "A* combines path cost and __________ to guide search.",
            "options": ["Random factor", "Heuristic estimate", "Iteration", "Utility score"],
            "correct_answer": "Heuristic estimate"
        },
        {
            "question": "In problem-solving, the starting point is called the:",
            "options": ["Final state", "Goal state", "Initial state", "Current node"],
            "correct_answer": "Initial state"
        },
        {
            "question": "The desired outcome in problem-solving is the __________ state.",
            "options": ["Action", "Initial", "Goal", "Transition"],
            "correct_answer": "Goal"
        },
        {
            "question": "The actions available to the agent are called:",
            "options": ["Sensors", "Percepts", "Operators (or Actions)", "Algorithms"],
            "correct_answer": "Operators (or Actions)"
        },
        {
            "question": "The measure of resource usage or effort to reach a goal is the:",
            "options": ["Utility function", "Success metric", "Path cost", "Performance measure"],
            "correct_answer": "Path cost"
        },
        {
            "question": "An exam scheduling problem is an example of a:",
            "options": ["Linear Regression Problem", "Constraint Satisfaction Problem (CSP)", "Reinforcement Learning Problem", "Clustering Problem"],
            "correct_answer": "Constraint Satisfaction Problem (CSP)"
        },
        {
            "question": "Ensuring accuracy, consistency, and trustworthiness of data is called data:",
            "options": ["Cleaning", "Validation", "Integrity", "Minimization"],
            "correct_answer": "Integrity"
        },
        {
            "question": "Detecting and fixing missing values or duplicates is part of data:",
            "options": ["Validation", "Auditing", "Cleaning", "Storage"],
            "correct_answer": "Cleaning"
        },
        {
            "question": "Checking if email addresses follow proper format is an example of data:",
            "options": ["Cleaning", "Validation", "Integrity", "Standardization"],
            "correct_answer": "Validation"
        },
        {
            "question": "Protecting sensitive information by encryption relates to __________ & confidentiality.",
            "options": ["Fairness", "Accountability", "Privacy", "Transparency"],
            "correct_answer": "Privacy"
        },
        {
            "question": "The ethical principle of __________ ensures users know how their data will be used.",
            "options": ["Data Integrity", "Informed consent", "Data Minimization", "Legal Compliance"],
            "correct_answer": "Informed consent"
        },
        {
            "question": "The ethical principle of __________ means collecting only necessary data.",
            "options": ["Data Integrity", "Data Minimization", "Data Validation", "Informed Consent"],
            "correct_answer": "Data Minimization"
        },
        # --- Q72-Q84 (Short Answer converted to Multiple Choice) ---
        {
            "question": "Define an AI agent:",
            "options": [
                "A computer that stores data.",
                "A software program that automates simple tasks.",
                "An entity that perceives its environment via sensors and acts upon it using actuators.",
                "An algorithm used for image recognition."
            ],
            "correct_answer": "An entity that perceives its environment via sensors and acts upon it using actuators."
        },
        {
            "question": "What does rationality mean in AI?",
            "options": [
                "Achieving the goal state every time.",
                "Making the best decision possible with available knowledge to maximize utility.",
                "Using only a model-based reflex approach.",
                "Knowing all future outcomes perfectly."
            ],
            "correct_answer": "Making the best decision possible with available knowledge to maximize utility."
        },
        {
            "question": "What are the four components of the PEAS framework?",
            "options": [
                "Planning, Execution, Actions, Simulation",
                "Percepts, Environment, Algorithms, Solutions",
                "Performance Measure, Environment, Actuators, Sensors",
                "Policy, Environment, Agents, States"
            ],
            "correct_answer": "Performance Measure, Environment, Actuators, Sensors"
        },
        {
            "question": "What is the main difference between goal-based and utility-based agents?",
            "options": [
                "Goal-based agents are faster; utility-based agents are more accurate.",
                "Goal-based agents aim for a target condition; utility-based agents optimize overall success with trade-offs.",
                "Utility-based agents only work in deterministic environments.",
                "Goal-based agents use only uninformed search."
            ],
            "correct_answer": "Goal-based agents aim for a target condition; utility-based agents optimize overall success with trade-offs."
        },
        {
            "question": "Why is omniscience impossible in real-world agents?",
            "options": [
                "Computational resources are too expensive.",
                "Agents cannot know exact outcomes of all actions; they act with limited information.",
                "The agent's sensors are always too weak.",
                "The goal state changes too frequently."
            ],
            "correct_answer": "Agents cannot know exact outcomes of all actions; they act with limited information."
        },
        {
            "question": "What is the initial state in problem-solving?",
            "options": [
                "The final goal reached by the agent.",
                "The first action taken by the agent.",
                "The starting point of a problem before any actions are taken.",
                "A random state in the environment."
            ],
            "correct_answer": "The starting point of a problem before any actions are taken."
        },
        {
            "question": "What is the goal state in problem-solving?",
            "options": [
                "A state with the lowest path cost.",
                "The current state after the last action.",
                "The desired target condition or outcome to be achieved.",
                "Any state that satisfies the transition model."
            ],
            "correct_answer": "The desired target condition or outcome to be achieved."
        },
        {
            "question": "Define path cost in AI problem-solving.",
            "options": [
                "The total number of nodes in the search tree.",
                "A measure of resource usage (time, steps, or expense) to reach the goal state.",
                "The error rate of the heuristic function.",
                "The numerical value of the goal state."
            ],
            "correct_answer": "A measure of resource usage (time, steps, or expense) to reach the goal state."
        },
        {
            "question": "Why is data called the foundation of AI?",
            "options": [
                "Because AI systems are primarily concerned with databases.",
                "Because AI systems learn, validate, and improve based on data quality; poor data leads to poor AI performance.",
                "Because the first AI programs were used for data entry.",
                "Because all AI must be trained on structured data."
            ],
            "correct_answer": "Because AI systems learn, validate, and improve based on data quality; poor data leads to poor AI performance."
        },
        {
            "question": "Define data integrity.",
            "options": [
                "The process of cleaning data errors.",
                "The measure of data file size.",
                "Accuracy, consistency, and trustworthiness of data across its lifecycle.",
                "The speed at which data can be accessed."
            ],
            "correct_answer": "Accuracy, consistency, and trustworthiness of data across its lifecycle."
        },
        {
            "question": "What are common techniques in data cleaning?",
            "options": [
                "Developing new algorithms and models.",
                "Running A* search and BFS.",
                "Handling missing values, removing duplicates, and standardizing formats.",
                "Increasing the number of features."
            ],
            "correct_answer": "Handling missing values, removing duplicates, and standardizing formats."
        },
        {
            "question": "What is data validation?",
            "options": [
                "Checking if data meets predefined rules (e.g., correct email formats, valid date ranges).",
                "Converting unstructured data to structured data.",
                "Securing data from unauthorized access.",
                "Reducing the dimensionality of the dataset."
            ],
            "correct_answer": "Checking if data meets predefined rules (e.g., correct email formats, valid date ranges)."
        },
        {
            "question": "Name two key ethical principles in data collection.",
            "options": [
                "Speed and Efficiency.",
                "Accuracy and Precision.",
                "Completeness and Consistency.",
                "Informed consent and privacy/confidentiality."
            ],
            "correct_answer": "Informed consent and privacy/confidentiality."
        },
    ],

    "Chapter 3 - Search Algorithms in AI": [
        # --- Q1-Q30 (Original Multiple Choice) ---
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
            "question": "Path cost is used to measure:",
            "options": ["Memory usage", "Time complexity", "Resource cost to reach a state", "Number of goal tests"],
            "correct_answer": "Resource cost to reach a state"
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
            "question": "Which of the following is true about BFS?",
            "options": ["May fail in infinite space", "Uses depth limit", "Guarantees shortest path in uniform cost", "Uses heuristic"],
            "correct_answer": "Guarantees shortest path in uniform cost"
        },
        {
            "question": "A blind search that expands nodes without domain-specific knowledge is called:",
            "options": ["Informed search", "Uninformed search", "Heuristic search", "A* search"],
            "correct_answer": "Uninformed search"
        },
        {
            "question": "Which search expands node with minimum heuristic value h(n)?",
            "options": ["BFS", "DFS", "Greedy Best-First Search", "A*"],
            "correct_answer": "Greedy Best-First Search"
        },
        {
            "question": "Which search is most memory-efficient?",
            "options": ["BFS", "DFS", "A*", "GBFS"],
            "correct_answer": "DFS"
        },
        {
            "question": "Which search is complete but not optimal in general graphs?",
            "options": ["BFS", "DFS", "GBFS", "Hill climbing"],
            "correct_answer": "BFS"
        },
        {
            "question": "The explored set in a search prevents:",
            "options": ["Finding optimal paths", "Revisiting nodes", "Using heuristics", "Computing path cost"],
            "correct_answer": "Revisiting nodes"
        },
        {
            "question": "A node in a search tree does NOT include:",
            "options": ["State", "Parent", "Path cost", "Training set"],
            "correct_answer": "Training set"
        },
        {
            "question": "Frontier in search refers to:",
            "options": ["All expanded nodes", "Nodes not yet expanded", "Explored set", "Goal states only"],
            "correct_answer": "Nodes not yet expanded"
        },
        {
            "question": "BFS ensures:",
            "options": ["Completeness and optimality (for unit costs)", "Minimum memory", "Heuristic guidance", "Infinite loops in all cases"],
            "correct_answer": "Completeness and optimality (for unit costs)"
        },
        {
            "question": "Which search is also called “blind search”?",
            "options": ["Uninformed search", "DFS", "BFS", "All of the above"],
            "correct_answer": "All of the above"
        },
        {
            "question": "Greedy Best-First Search uses:",
            "options": ["Path cost only", "Heuristic only", "Path cost + heuristic", "Random expansion"],
            "correct_answer": "Heuristic only"
        },
        {
            "question": "A* search evaluates nodes using:",
            "options": ["h(n)", "g(n)", "f(n) = g(n) + h(n)", "None"],
            "correct_answer": "f(n) = g(n) + h(n)"
        },
        {
            "question": "Heuristic functions in informed search provide:",
            "options": ["Exact cost", "Estimate of cost to goal", "Path reconstruction", "Explored set"],
            "correct_answer": "Estimate of cost to goal"
        },
        {
            "question": "An admissible heuristic is one that:",
            "options": ["Always underestimates or equals true cost", "Overestimates true cost", "Uses no estimate", "Is inconsistent"],
            "correct_answer": "Always underestimates or equals true cost"
        },
        {
            "question": "Which of the following is both complete and optimal with admissible heuristics?",
            "options": ["BFS", "DFS", "Greedy Best-First", "A*"],
            "correct_answer": "A*"
        },
        {
            "question": "Greedy Best-First Search may fail to find optimal paths because:",
            "options": ["It ignores path cost g(n)", "It ignores h(n)", "It doesn’t use explored sets", "It is uninformed"],
            "correct_answer": "It ignores path cost g(n)"
        },
        {
            "question": "Which property makes A* more efficient than BFS?",
            "options": ["Uses heuristics", "Uses stack", "Ignores costs", "Requires no explored set"],
            "correct_answer": "Uses heuristics"
        },
        {
            "question": "In BFS, if branching factor is $b$ and depth is $d$, space complexity is:",
            "options": ["$O(b^d)$", "$O(d)$", "$O(bd)$", "$O(1)$"],
            "correct_answer": "$O(b^d)$"
        },
        {
            "question": "In DFS, space complexity is:",
            "options": ["$O(b^d)$", "$O(bm)$ where $m$=max depth", "$O(1)$", "$O(d)$"],
            "correct_answer": "$O(bm)$ where $m$=max depth"
        },
        {
            "question": "Which is more memory intensive?",
            "options": ["DFS", "BFS", "Both equal", "GBFS"],
            "correct_answer": "BFS"
        },
        {
            "question": "A heuristic that overestimates true cost is:",
            "options": ["Admissible", "Consistent", "Non-admissible", "Perfect"],
            "correct_answer": "Non-admissible"
        },
        {
            "question": "Which algorithm may revisit the same node multiple times if no explored set is used?",
            "options": ["BFS", "DFS", "Uninformed Search", "All of the above"],
            "correct_answer": "All of the above"
        },
        {
            "question": "Which algorithm uses the evaluation function $f(n)=h(n)$?",
            "options": ["BFS", "DFS", "Greedy Best-First Search", "A*"],
            "correct_answer": "Greedy Best-First Search"
        },
        # --- Q31-Q54 (True/False converted to Multiple Choice) ---
        {
            "question": "BFS is both complete and optimal for unit step costs.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Admissible heuristics never overestimate the true cost to the goal.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "A consistent heuristic must satisfy $h(n) \le Cost(n, a, n') + h(n')$.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "If a heuristic is consistent, it is also admissible.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "If a heuristic is admissible, it must also be consistent.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "A* with an admissible heuristic is always optimal.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "DFS can be incomplete in infinite-depth problems.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "BFS explores nodes depth-first before breadth.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "Greedy Best-First Search is guaranteed to be complete in infinite spaces.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "In tree search without an explored set, cycles can cause infinite loops.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "The frontier contains nodes that are already expanded.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "A heuristic is any function that guarantees optimality.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "Greedy Best-First Search ignores the actual cost $g(n)$.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "A* ignores $g(n)$ completely.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "The branching factor is the maximum number of successors from a node.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "A* can fail to be optimal if the heuristic is not admissible.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Greedy Best-First Search is optimal if the heuristic is admissible.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "The cost function $g(n)$ in A* represents the path cost so far.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "A consistent heuristic satisfies the triangle inequality.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "BFS is complete but only optimal if step costs are uniform.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "DFS requires more memory than BFS.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "BFS and DFS both guarantee optimality.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "DFS is guaranteed to find a solution faster than BFS.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "A* guarantees both completeness and optimality with admissible heuristics.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        # --- Q55-Q63 (Short Answer converted to Multiple Choice) ---
        {
            "question": "If $g(n)=0$ in A*, what does it reduce to?",
            "options": ["BFS", "DFS", "Uniform Cost Search", "GBFS (Greedy Best First Search)"],
            "correct_answer": "GBFS (Greedy Best First Search)"
        },
        {
            "question": "Which search doesn’t need domain-specific knowledge?",
            "options": ["A* search", "Greedy Best-First Search", "Informed Search", "Uninformed search (BFS or DFS)"],
            "correct_answer": "Uninformed search (BFS or DFS)"
        },
        {
            "question": "An example of uninformed search is:",
            "options": ["A* with Manhattan heuristic", "BFS on a maze", "Greedy search on a graph", "Hill Climbing"],
            "correct_answer": "BFS on a maze"
        },
        {
            "question": "An example of informed search is:",
            "options": ["DFS without cycle checking", "BFS with unit cost", "A* with Manhattan heuristic", "Uniform Cost Search"],
            "correct_answer": "A* with Manhattan heuristic"
        },
        {
            "question": "Why is heuristic design important?",
            "options": ["It guarantees completeness.", "It ensures memory efficiency.", "Good heuristics reduce the number of nodes expanded.", "It is only required for uninformed search."],
            "correct_answer": "Good heuristics reduce the number of nodes expanded."
        },
        {
            "question": "How does an explored set improve search efficiency?",
            "options": ["It guarantees optimality.", "It prevents re-expansion of already processed nodes.", "It only stores goal states.", "It guides the search using $h(n)$."],
            "correct_answer": "It prevents re-expansion of already processed nodes."
        },
        {
            "question": "What is the 'frontier' in search?",
            "options": ["The set of all nodes in the graph.", "Nodes generated but not yet expanded.", "The set of already expanded nodes.", "The shortest path found so far."],
            "correct_answer": "Nodes generated but not yet expanded."
        },
        {
            "question": "Why does GBFS often expand fewer nodes than BFS?",
            "options": ["It uses a stack structure.", "It ignores the path cost $g(n)$.", "It uses heuristic guidance $h(n)$ to prioritize promising nodes.", "It only works in finite spaces."],
            "correct_answer": "It uses heuristic guidance $h(n)$ to prioritize promising nodes."
        },
        {
            "question": "Which statement accurately compares search algorithms?",
            "options": [
                "DFS is always faster than BFS, but less memory efficient.",
                "GBFS is complete and optimal with any heuristic.",
                "BFS = complete, optimal for unit costs; DFS = memory efficient; GBFS = fast, not optimal; A* = complete & optimal with admissible heuristics.",
                "A* is only complete if its heuristic is non-admissible."
            ],
            "correct_answer": "BFS = complete, optimal for unit costs; DFS = memory efficient; GBFS = fast, not optimal; A* = complete & optimal with admissible heuristics."
        },
    ],
    "Chapter 4 - Machine Learning": [
        # --- Q1-Q38 (Original Multiple Choice) ---
        {
            "question": "Machine Learning is best defined as:",
            "options": ["Programming computers with fixed rules", "Giving machines ability to learn without explicit programming", "Simple data entry automation", "Artificial General Intelligence"],
            "correct_answer": "Giving machines ability to learn without explicit programming"
        },
        {
            "question": "Which of the following is NOT a type of machine learning?",
            "options": ["Supervised learning", "Unsupervised learning", "Reinforcement learning", "Declarative learning"],
            "correct_answer": "Declarative learning"
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
            "question": "Which algorithm is commonly used for classification?",
            "options": ["Linear regression", "Support Vector Machine (SVM)", "K-means clustering", "Principal Component Analysis"],
            "correct_answer": "Support Vector Machine (SVM)"
        },
        {
            "question": "Which algorithm is NOT supervised learning?",
            "options": ["Logistic regression", "K-means", "Decision tree", "k-Nearest Neighbors"],
            "correct_answer": "K-means"
        },
        {
            "question": "In unsupervised learning, the algorithm is provided with:",
            "options": ["Labeled outputs", "Rewards and penalties", "Only input data without labels", "Correct classifications"],
            "correct_answer": "Only input data without labels"
        },
        {
            "question": "Customer segmentation is an example of:",
            "options": ["Supervised learning", "Reinforcement learning", "Clustering", "Regression"],
            "correct_answer": "Clustering"
        },
        {
            "question": "Which of the following is an example of reinforcement learning?",
            "options": ["Predicting exam scores", "Identifying spam emails", "A robot learning to walk by trial and error", "Customer segmentation"],
            "correct_answer": "A robot learning to walk by trial and error"
        },
        {
            "question": "In reinforcement learning, the agent learns by:",
            "options": ["Labeled training data", "Maximizing cumulative reward", "Clustering unlabeled data", "Reducing error rate"],
            "correct_answer": "Maximizing cumulative reward"
        },
        {
            "question": "Semi-supervised learning uses:",
            "options": ["Only labeled data", "Only unlabeled data", "Both labeled and unlabeled data", "Rewards and penalties"],
            "correct_answer": "Both labeled and unlabeled data"
        },
        {
            "question": "Predicting GPA based on study hours is an example of:",
            "options": ["Regression", "Classification", "Clustering", "Reinforcement"],
            "correct_answer": "Regression"
        },
        {
            "question": "Which of the following is a disadvantage of linear regression?",
            "options": ["Easy to interpret", "Assumes linear relationship", "Works well on small datasets", "Suitable for regression tasks"],
            "correct_answer": "Assumes linear relationship"
        },
        {
            "question": "Which algorithm is suitable for predicting continuous values?",
            "options": ["Linear regression", "Decision tree classifier", "K-means", "Apriori algorithm"],
            "correct_answer": "Linear regression"
        },
        {
            "question": "In k-Nearest Neighbors (k-NN), classification depends on:",
            "options": ["Distance from nearest neighbors", "Decision trees", "Reward maximization", "Feature reduction"],
            "correct_answer": "Distance from nearest neighbors"
        },
        {
            "question": "Which algorithm constructs hyperplanes for separation of data?",
            "options": ["Decision tree", "SVM", "K-means", "Naïve Bayes"],
            "correct_answer": "SVM"
        },
        {
            "question": "The support vectors in SVM are:",
            "options": ["Data points far from hyperplane", "Data points closest to hyperplane", "All training data points", "Randomly chosen points"],
            "correct_answer": "Data points closest to hyperplane"
        },
        {
            "question": "Which algorithm is used for grouping market-basket items?",
            "options": ["Linear regression", "Apriori algorithm", "SVM", "Logistic regression"],
            "correct_answer": "Apriori algorithm"
        },
        {
            "question": "Association rule mining helps in:",
            "options": ["Predicting continuous values", "Finding relationships among items", "Grouping similar customers", "Reinforcement learning"],
            "correct_answer": "Finding relationships among items"
        },
        {
            "question": "Which of the following is NOT a clustering algorithm?",
            "options": ["K-means", "Hierarchical clustering", "DBSCAN", "Logistic regression"],
            "correct_answer": "Logistic regression"
        },
        {
            "question": "Which algorithm is best for customer segmentation?",
            "options": ["Regression", "Classification", "Clustering", "Reinforcement"],
            "correct_answer": "Clustering"
        },
        {
            "question": "Market basket analysis is mainly based on:",
            "options": ["Regression", "Classification", "Association rules", "Reinforcement learning"],
            "correct_answer": "Association rules"
        },
        {
            "question": "Which type of learning is used in fraud detection systems?",
            "options": ["Supervised learning", "Unsupervised learning", "Reinforcement learning", "Dimensionality reduction"],
            "correct_answer": "Supervised learning"
        },
        {
            "question": "In ML workflow, after data collection, the next important step is:",
            "options": ["Model training", "Data preprocessing", "Evaluation", "Deployment"],
            "correct_answer": "Data preprocessing"
        },
        {
            "question": "Which of the following is an ethical concern in ML?",
            "options": ["Bias in datasets", "Model interpretability", "Privacy of data", "All of the above"],
            "correct_answer": "All of the above"
        },
        {
            "question": "Which step comes at the very end of ML workflow?",
            "options": ["Data preprocessing", "Training", "Deployment", "Evaluation"],
            "correct_answer": "Deployment"
        },
        {
            "question": "Which of the following is a disadvantage of k-NN?",
            "options": ["Non-parametric nature", "High computation for large datasets", "Handles nonlinear data", "Simple to implement"],
            "correct_answer": "High computation for large datasets"
        },
        {
            "question": "Which of the following is NOT a distance metric used in k-NN?",
            "options": ["Euclidean distance", "Manhattan distance", "Hamming distance", "Exponential distance"],
            "correct_answer": "Exponential distance"
        },
        {
            "question": "Which clustering method builds a hierarchy of clusters?",
            "options": ["K-means", "Hierarchical clustering", "PCA", "Regression"],
            "correct_answer": "Hierarchical clustering"
        },
        {
            "question": "K-means clustering requires:",
            "options": ["Number of clusters $k$ as input", "Labeled training data", "Rewards", "Regression coefficients"],
            "correct_answer": "Number of clusters $k$ as input"
        },
        {
            "question": "In k-means, cluster centers are updated by computing:",
            "options": ["Random values", "Median of features", "Mean of assigned points", "Logistic regression weights"],
            "correct_answer": "Mean of assigned points"
        },
        {
            "question": "Which clustering method does NOT require the number of clusters in advance?",
            "options": ["K-means", "DBSCAN", "Hierarchical (divisive)", "Both b and c"],
            "correct_answer": "Both b and c"
        },
        {
            "question": "Which algorithm is commonly used in market basket analysis?",
            "options": ["Apriori", "K-means", "PCA", "SVM"],
            "correct_answer": "Apriori"
        },
        {
            "question": "Overfitting is more likely when:",
            "options": ["Dataset is very large", "Model is very complex with few data points", "Data is balanced", "Regularization is applied"],
            "correct_answer": "Model is very complex with few data points"
        },
        {
            "question": "Which method helps prevent overfitting?",
            "options": ["Cross-validation", "Ignoring test data", "Using fewer features", "Overtraining"],
            "correct_answer": "Cross-validation"
        },
        # --- Q39-Q45 (Short Answer converted to Multiple Choice) ---
        {
            "question": "Differentiate Machine Learning from traditional programming.",
            "options": [
                "ML uses fixed rules; Traditional programs learn from data.",
                "ML is only for large data; Traditional is for small data.",
                "Traditional programming explicitly codes rules, while ML learns patterns from data without being explicitly programmed.",
                "ML is an older concept than traditional programming."
            ],
            "correct_answer": "Traditional programming explicitly codes rules, while ML learns patterns from data without being explicitly programmed."
        },
        {
            "question": "What are the three main types of machine learning?",
            "options": [
                "Linear, Non-linear, and Kernelized.",
                "Shallow, Deep, and Artificial General.",
                "Supervised, Unsupervised, and Reinforcement learning.",
                "Classification, Regression, and Association."
            ],
            "correct_answer": "Supervised, Unsupervised, and Reinforcement learning."
        },
        {
            "question": "Which is an example of supervised learning?",
            "options": [
                "Clustering customer data.",
                "Email spam classification using labeled examples of spam and non-spam.",
                "A robot exploring a maze for a reward.",
                "Generating new text based on a corpus."
            ],
            "correct_answer": "Email spam classification using labeled examples of spam and non-spam."
        },
        {
            "question": "Which is an example of unsupervised learning?",
            "options": [
                "Identifying fraud transactions.",
                "Predicting a stock price.",
                "Customer segmentation using clustering.",
                "Playing chess against an opponent."
            ],
            "correct_answer": "Customer segmentation using clustering."
        },
        {
            "question": "Which is an example of reinforcement learning?",
            "options": [
                "Predicting weather patterns.",
                "A robot learning to walk by maximizing rewards for correct movements.",
                "Categorizing images with labeled objects.",
                "Finding anomalies in network traffic."
            ],
            "correct_answer": "A robot learning to walk by maximizing rewards for correct movements."
        },
        {
            "question": "Define regression in ML.",
            "options": [
                "Regression predicts discrete categories or labels.",
                "Regression groups similar data points.",
                "Regression predicts continuous values based on input features.",
                "Regression is a type of unsupervised learning."
            ],
            "correct_answer": "Regression predicts continuous values based on input features."
        },
        {
            "question": "Define classification in ML.",
            "options": [
                "Classification finds the shortest path between states.",
                "Classification predicts discrete categories or labels from input features.",
                "Classification predicts continuous numeric values.",
                "Classification is solely concerned with feature selection."
            ],
            "correct_answer": "Classification predicts discrete categories or labels from input features."
        },
        # --- T/F 1-25 (True/False converted to Multiple Choice) ---
        {
            "question": "Machine learning teaches computers to learn patterns and make decisions from data without explicit programming.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "In traditional programming, the programmer writes rules which are applied to data.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Machine learning is a broader field, while Artificial Intelligence is a subset.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "Supervised learning requires inputs and correct outputs (labels).",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "In unsupervised learning, models are trained on labeled data.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "Reinforcement learning agents learn by receiving rewards or penalties from the environment.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Email spam classification is an example of supervised learning.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Market segmentation is an example of unsupervised learning.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "In reinforcement learning, 'policy' defines the strategy mapping states to actions.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Classification problems predict discrete categories.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Regression problems predict continuous values.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "k-NN considers multiple neighbors to decide the output.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Linear regression assumes a straight-line relationship between inputs and outputs.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Overfitting happens when a model learns noise in the training data.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Linear regression is highly resistant to outliers.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "SVM finds the hyperplane with maximum margin between classes.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Support vectors are the most important data points for defining the SVM boundary.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "K-Means clustering needs the number of clusters ($k$) to be specified.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Hierarchical clustering does not require specifying the number of clusters in advance.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "A dendrogram is used to visualize hierarchical clustering.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Association rule mining discovers interesting relationships between variables.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "The Apriori algorithm uses the principle that all subsets of a frequent itemset must also be frequent.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Confidence in association rule mining is defined as $\\frac{\\text{Transactions}(A \\cap B)}{\\text{Transactions}(A)}$.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Lift < 1 implies a negative relationship between items.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "PCA, LDA, and NMF are all dimensionality reduction techniques.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        # --- FIL in the BLANK 1-25 (Converted to Multiple Choice) ---
        {
            "question": "Machine Learning is a subset of:",
            "options": ["Data Mining", "Statistics", "Artificial Intelligence", "Computer Vision"],
            "correct_answer": "Artificial Intelligence"
        },
        {
            "question": "In traditional programming: Rules + Data $\\rightarrow$ __________.",
            "options": ["Algorithm", "Model", "Output", "Prediction"],
            "correct_answer": "Output"
        },
        {
            "question": "In ML: Data + Correct Answers (labels) $\\rightarrow$ Algorithm $\\rightarrow$ __________.",
            "options": ["Rules", "Outputs", "Predictions", "Data"],
            "correct_answer": "Predictions"
        },
        {
            "question": "Supervised learning uses inputs and __________.",
            "options": ["Random rewards", "Unlabeled data", "Labels/Correct outputs", "Policy"],
            "correct_answer": "Labels/Correct outputs"
        },
        {
            "question": "Predicting house prices is an example of __________ learning.",
            "options": ["Unsupervised", "Reinforcement", "Supervised", "Semi-supervised"],
            "correct_answer": "Supervised"
        },
        {
            "question": "Grouping customers by behavior is an example of __________ learning.",
            "options": ["Supervised", "Reinforcement", "Unsupervised", "Regression"],
            "correct_answer": "Unsupervised"
        },
        {
            "question": "In RL, the learner/decision maker is called the __________.",
            "options": ["Sensor", "Actuator", "Agent", "Observer"],
            "correct_answer": "Agent"
        },
        {
            "question": "In RL, feedback comes as __________.",
            "options": ["Labels", "Correct answers", "Rewards or penalties", "Features"],
            "correct_answer": "Rewards or penalties"
        },
        {
            "question": "Classification predicts __________ categories.",
            "options": ["Continuous", "Numeric", "Discrete", "Random"],
            "correct_answer": "Discrete"
        },
        {
            "question": "Regression predicts __________ values.",
            "options": ["Discrete", "Categorical", "Binary", "Continuous"],
            "correct_answer": "Continuous"
        },
        {
            "question": "In k-NN, the final label is decided by __________ vote of neighbors.",
            "options": ["Random", "Weighted", "Majority", "Unanimous"],
            "correct_answer": "Majority"
        },
        {
            "question": "The linear regression equation is:",
            "options": ["$f(x) = wx + b$", "$y = \\beta_0 + \\beta_1x + \\epsilon$", "$y = e^{x}$", "$y = \\sum (x_i - \\mu)$"],
            "correct_answer": "$y = \\beta_0 + \\beta_1x + \\epsilon$"
        },
        {
            "question": "In the GPA example, $\\beta_0 = 1.8$ means the predicted GPA when study hours = __________.",
            "options": ["1.8", "1", "0", "10"],
            "correct_answer": "0"
        },
        {
            "question": "Overfitting produces very low training error but high __________ error.",
            "options": ["Bias", "Model", "Test/Generalization", "Validation"],
            "correct_answer": "Test/Generalization"
        },
        {
            "question": "SVM separates data using a __________.",
            "options": ["Boundary", "Decision tree", "Centroid", "Hyperplane"],
            "correct_answer": "Hyperplane"
        },
        {
            "question": "The data points closest to the SVM hyperplane are called __________.",
            "options": ["Centroids", "Vectors", "Support vectors", "Outliers"],
            "correct_answer": "Support vectors"
        },
        {
            "question": "K-Means uses __________ distance to assign points to clusters.",
            "options": ["Manhattan", "Hamming", "Euclidean", "Chebyshev"],
            "correct_answer": "Euclidean"
        },
        {
            "question": "The tree-like diagram used in hierarchical clustering is called a __________.",
            "options": ["Decision tree", "Cluster map", "Dendrogram", "Scatter plot"],
            "correct_answer": "Dendrogram"
        },
        {
            "question": "In association rule mining, Support(A$\\rightarrow$B) = $\\frac{\\text{Transactions containing} (A \\cap B)}{\\text{__________}}$.",
            "options": ["Transactions containing (A)", "Transactions containing (B)", "Total transactions", "Frequent itemsets"],
            "correct_answer": "Total transactions"
        },
        {
            "question": "Confidence(A$\\rightarrow$B) = $\\frac{\\text{Transactions containing} (A \\cap B)}{\\text{Transactions containing __________}}$.",
            "options": ["(B)", "(A)", "(A $\\cup$ B)", "Total transactions"],
            "correct_answer": "(A)"
        },
        {
            "question": "Lift(A$\\rightarrow$B) > 1 means the items have a __________ relationship.",
            "options": ["Negative", "Neutral", "Inverse", "Positive"],
            "correct_answer": "Positive"
        },
        {
            "question": "Apriori generates __________ sets at each iteration to find frequent patterns.",
            "options": ["Support", "Confidence", "Candidate itemsets", "Association"],
            "correct_answer": "Candidate itemsets"
        },
        {
            "question": "Items that fail minimum support in Apriori are __________ immediately.",
            "options": ["Selected", "Pruned/Discarded", "Clustered", "Regressed"],
            "correct_answer": "Pruned/Discarded"
        },
        {
            "question": "PCA stands for __________.",
            "options": ["Principal Component Association", "Probabilistic Cluster Algorithm", "Principal Component Analysis", "Pattern Classification Agent"],
            "correct_answer": "Principal Component Analysis"
        },
        {
            "question": "LDA stands for __________.",
            "options": ["Linear Data Annotation", "Logistic Data Analysis", "Linear Discriminant Analysis", "Local Dependency Algorithm"],
            "correct_answer": "Linear Discriminant Analysis"
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
            "question": "The Markov Decision Process (MDP) is defined by:",
            "options": ["States, Actions, Rewards, Probabilities", "Inputs, Outputs, Weights", "Features, Labels, Noise", "Policy, Precision, Recall"],
            "correct_answer": "States, Actions, Rewards, Probabilities"
        },
        {
            "question": "The dilemma in RL between trying new actions and using known ones is called:",
            "options": ["Overfitting vs Underfitting", "Training vs Testing", "Exploration vs Exploitation", "Bias vs Variance"],
            "correct_answer": "Exploration vs Exploitation"
        },
        {
            "question": "$\\epsilon$-greedy algorithm balances exploration and exploitation by:",
            "options": ["Always choosing best action", "Always choosing random action", "Choosing random with probability $\\epsilon$", "Ignoring randomness"],
            "correct_answer": "Choosing random with probability $\\epsilon$"
        },
        {
            "question": "In $\\epsilon$-greedy, as $\\epsilon$ decreases over time, the agent:",
            "options": ["Explores more", "Exploits more", "Stops learning", "Ignores states"],
            "correct_answer": "Exploits more"
        },
        {
            "question": "The update rule in $\\epsilon$-greedy uses which parameter?",
            "options": ["Precision", "$ \\alpha $ (learning rate)", "Recall", "Batch size"],
            "correct_answer": "$ \\alpha $ (learning rate)"
        },
        {
            "question": "Q-learning is an example of:",
            "options": ["Supervised learning", "Unsupervised learning", "Model-free RL", "Model-based RL"],
            "correct_answer": "Model-free RL"
        },
        {
            "question": "In Q-learning, Q(s,a) represents:",
            "options": ["Reward function", "State value", "Action-state value", "Policy"],
            "correct_answer": "Action-state value"
        },
        {
            "question": "Reinforcement Learning uses trial and error to learn.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Policy in RL maps rewards to states.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "Value function measures long-term desirability of states.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Rewards always indicate long-term success.",
            "options": ["True", "False"],
            "correct_answer": "False"
        },
        {
            "question": "Model-based RL requires a simulator of the environment.",
            "options": ["True", "False"],
            "correct_answer": "True"
        },
        {
            "question": "Q-learning is a model-based RL method.",
            "options": ["True", "False"],
            "correct_answer": "False"
        }
    ]
}
