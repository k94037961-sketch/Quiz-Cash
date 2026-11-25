name=input("Enter your name: ")
print("Welcome to Game, " + name + "!")
list_of_questions = {
    "question1": {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
        "answer": "C",
        "reward": 1000
    },
    "question2": {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
        "answer": "B",
        "reward": 5000
    },
    "question3": {
        "question": "What is the chemical symbol for water?",
        "options": ["A) H2O", "B) CO2", "C) NaCl", "D) O2"],
        "answer": "A",
        "reward": 10000
    },
    "question4": {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Leo Tolstoy", "D) Mark Twain"],
        "answer": "B",
        "reward": 50000
    }
}
all_answers_correct = True
total_reward = 0

for key, value in list_of_questions.items():
    print(value["question"])
    for option in value["options"]:
        print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ")
    if user_answer.strip().upper() == value["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is " + value["answer"] + ".")
        all_answers_correct = False

if all_answers_correct:
    total_reward = sum(value["reward"] for value in list_of_questions.values())
    print("Congratulations, " + name + "! You won Rs. " + format(total_reward, ",") + "!")
else:
    print("Sorry, " + name + ". You lost. Your total reward is Rs. " + format(total_reward, ",") + ".")
    

