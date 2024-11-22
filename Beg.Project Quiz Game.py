
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

# List of questions that can be used & change later for the Quiz. Each question is a dictionary.
questions = [
    {
        "prompt": "What is the capital of Indonesia?",
        "options": ["A. Bandar Seri Begawan", "B. Kuala Lumpur", "C. Jakarta", "D. Manila"],
        "answer": "C"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the loudest animal on earth?",
        "options": ["A. Bottlenose Doplhin", "B. Sperm Whale", "C. Greater Bulldog Bat", "D. Lion"],
        "answer": "B"
    },
    {
        "prompt": "How many elements are in the periodic table?",
        "options": ["A. 120", "B. 110", "C. 132", "D. 118"],
        "answer": "D"
    }
]

# Time to run the quiz :)
run_quiz(questions)