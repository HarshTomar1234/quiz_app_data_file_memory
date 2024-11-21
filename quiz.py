import json
import random

users = {}


def load_quiz_data():
    """Load quiz data from a file."""
    try:
        with open("quiz_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Quiz data file not found!")
        return {}

#########################################################
def save_quiz_data(data):
    """Save quiz data to a file."""
    with open("quiz_data.json", "w") as file:
        json.dump(data, file, indent=4)

#########################################################

def register():
    name = input("Enter a username: ")
    if name in users:
        print("User already exists!")
        return False
    pwd = input("Enter a password: ")
    users[name] = pwd
    print("Registration successful!")
    return True


def login():
    name = input("Enter your username: ")
    pwd = input("Enter your password: ")
    if users.get(name) == pwd:
        print("Login successful!")
        return name
    print("Invalid username or password!")
    return None

#########################################################

def quiz(subject, user, quiz_data):
    print(f"\nStarting {subject} quiz!")
    score = 0
    if subject not in quiz_data:
        print(f"No quiz data available for {subject}.")
        return

    questions = random.sample(quiz_data[subject], len(quiz_data[subject]))[:5]

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['q']}")
        for idx, option in enumerate(q["o"], 1):
            print(f"{idx}. {option}")
        try:
            ans = int(input("Your answer (1/2/3/4): "))
            if q["o"][ans - 1] == q["a"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['a']}")
        except (ValueError, IndexError):
            print("Invalid input! Skipping this question.")

    print(f"\n{user}, your score is {score}/5.")

#########################################################

def main():
    print("Welcome to the Quiz Application!")
    user = None
    quiz_data = load_quiz_data()

    while not user:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if register():
                continue
        elif choice == "2":
            user = login()
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice!")

    while True:
        print("\nSubjects:\n1. C++\n2. Python")
        choice = input("Choose a subject (1/2): ")
        if choice == "1":
            quiz("C++", user, quiz_data)
        elif choice == "2":
            quiz("Python", user, quiz_data)
        else:
            print("Invalid choice!")
            continue

        play_again = input("Do you want to take another quiz? (yes/no): ").lower()
        if play_again != "yes":
            print("Goodbye!")
            break

#########################################################

if __name__ == "__main__":
    main()
