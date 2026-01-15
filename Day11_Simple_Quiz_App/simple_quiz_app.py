import random

#30-day Python challenge
print("------30-day Python challenge 11/30------")
print("Simple Quiz App")

score= 0

quiz = [
    {
        "question": "What keyword is used to define a function in Python?",
        "answer": "def"
    },
    {
        "question": "Which data type stores multiple values in order?",
        "answer": "list"
    },
    {
        "question": "What function is used to take input from the user?",
        "answer": "input"
    },
    {
        "question": "Which loop is best when the number of repetitions is known?",
        "answer": "for"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "answer": "#"
    }
]

total_quiz= len(quiz)

running = True

while running:

    random_question = random.choice(quiz)
    print(random_question["question"])

    user_answer = input("Enter the Answer (Type q anytime to quit): ").strip().lower()

    if user_answer == "q":
       print(f"Game Over. Your score: {score}")
       break

    elif user_answer == random_question["answer"]:
        print(f"{user_answer} is Correct!")
        score +=1
        quiz.remove(random_question)
        print(f"Your Score is: {score}/{total_quiz}")
        if len(quiz) == 0:
            print("You Win! Congratulation")
            break
    else:
        print(f"{user_answer} is Wrong! Answer: {random_question['answer']}")
        continue
