# Multiple Choice Quiz Program

# Questions and choices
questions = [
    {
        "question": "What is the capital of India?",
        "choices": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web development?",
        "choices": ["A. Python", "B. HTML", "C. Java", "D. C++"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "choices": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    }
]

score = 0

# Loop through questions
for q in questions:
    print("\n" + q["question"])
    for choice in q["choices"]:
        print(choice)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

# Final score
print("\nYour final score is:", score, "out of", len(questions))
