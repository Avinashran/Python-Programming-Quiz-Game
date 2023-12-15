
import random
import time
import sys
import datetime

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
GREY = "\033[90m"
RESET = "\033[0m"


def quiz_question(question_number, question, options, correct_answer):
    print(f"\nQuestion {question_number}: {question}")
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

    start_time = time.time()
    while True:
        user_answer = input("Your answer (enter the option number): ")

        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            user_answer_index = int(user_answer) - 1
            if options[user_answer_index] == correct_answer:
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)
                print(f"{GREEN}Correct! Time taken: {time_taken} seconds{RESET}\n")
                return True, time_taken
            else:
                print(f"{RED}Wrong! The correct answer is: {correct_answer}{RESET}\n")
                return False, 0
        else:
            print("Invalid input. Please enter a valid option number.\n")


def play_quiz(player_name, player_scores):
    questions = [
        {
            "question": "What is the result of print(88+22)?",
            "options": ["95", "100", "105", "110"],
            "correct_answer": "110"
        },
        {
            "question": "Which programming concept is used to repeat a block of code?",
            "options": ["For Loop", "While Loop", "If Statement", "Function"],
            "correct_answer": "While Loop"
        },
        {
            "question": "What does the 'len()' function do?",
            "options": ["Returns the length of a string", "Calculates square root", "Finds maximum value",
                        "Counts elements in a list"],
            "correct_answer": "Returns the length of a string"
        },
        {
            "question": "In Python, how do you define a function?",
            "options": ["define", "function", "def", "define_function"],
            "correct_answer": "def"
        },
        {
            "question": "What is the purpose of the 'else' clause in an 'if' statement?",
            "options": ["To handle exceptions", "To execute a block of code if the 'if' condition is False",
                        "To define a function", "To initialize variables"],
            "correct_answer": "To execute a block of code if the 'if' condition is False"
        },
        {
            "question": "What does the 'pop()' method do in a list?",
            "options": ["Adds an element to the end of the list", "Removes the last element from the list",
                        "Sorts the list", "Counts the occurrences of a specified element"],
            "correct_answer": "Removes the last element from the list"
        },
        {
            "question": "How do you open a file in Python for reading?",
            "options": ["open('file.txt', 'r')", "read_file('file.txt')", "file.open('file.txt', 'read')",
                        "open_file('file.txt')"],
            "correct_answer": "open('file.txt', 'r')"
        },
        {
            "question": "Which module is used for mathematical operations in Python?",
            "options": ["math", "calc", "numbers", "arithmetic"],
            "correct_answer": "math"
        },
        {
            "question": "What is the output of 'print(3 / 2)'?",
            "options": ["0.5", "1", "2", "1.5"],
            "correct_answer": "1.5"
        },
        {
            "question": "How do you check if a key exists in a dictionary?",
            "options": ["check_key()", "key_exists()", "exists_key()", "in"],
            "correct_answer": "in",
            "difficulty": "Normal"
        }
    ]

    random.shuffle(questions)  # Shuffle the questions list to make them random

    print(f"Hello {BLUE}{player_name}{RESET}, Welcome to the Python Programming Quiz!\n")
    correct_answers = 0
    total_time_taken = 0

    for idx, question_data in enumerate(questions, start=1):
        result, time_taken = quiz_question(idx, question_data["question"], question_data["options"],
                                           question_data["correct_answer"])
        if result:
            correct_answers += 1
            difficulty_level = question_data.get("difficulty", "Normal")
            score = correct_answers * (10 if difficulty_level == "Normal" else 15)
            print(f"Your current score: {GREEN}{score}{RESET}\n")
            total_time_taken += time_taken

    player_scores.append((player_name, correct_answers, total_time_taken))

    # Display scoreboard after each quiz attempt
    print(f"{RED}SCOREBOARD{RESET}")
    player_scores.sort(key=lambda x: (-x[1], x[2]))  # Sort by score (highest first) and then by time taken
    for i, (name, score, time_taken) in enumerate(player_scores, start=1):
        print(f"{i}. {BLUE}{name}{RESET}: {GREEN}Score: {score}/{len(questions)}{RESET}, Time Taken: {time_taken:.2f} seconds")

    print("\n")


if __name__ == "__main__":
    player_scores = []  # List to store scores for all players

    while True:
        player_name = input("Enter your name (or 'exit' to quit): ")
        if player_name.lower() == 'exit':
            break

        play_quiz(player_name, player_scores)

    # Display final scoreboard for all players
    print(f"{RED}Final Scoreboard for all players:{RESET}\n")
    player_scores.sort(key=lambda x: (-x[1], x[2]))  # Sort by score (highest first) and then by time taken
    for i, (name, score, time_taken) in enumerate(player_scores, start=1):
        print(f"{i}. {BLUE}{name}{RESET}: {GREEN}Score: {score}/{len(questions)}{RESET}, Time Taken: {time_taken:.2f} seconds")

    print("\n")
