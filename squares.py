"""MATHS GAME APPLICAITON PYTHON CODE"""

import random

def start_game():
    print("--- Welcome to the Square Quiz Game! ---")
    
    # 1. Get user input for range
    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    score = 0
    results_log = [] # To keep track of what they got right/wrong

    # 2. Loop through each number in the range
    for i in range(start, end + 1):
        correct_answer = i ** 2
        
        # 3. Generate 3 unique random "wrong" answers
        wrong_answers = set()
        while len(wrong_answers) < 3:
            fake = random.randint(correct_answer - 20, correct_answer + 20)
            if fake != correct_answer and fake > 0:
                wrong_answers.add(fake)
        
        # Combine and shuffle options
        options = list(wrong_answers) + [correct_answer]
        random.shuffle(options)

        print(f"\nWhat is the square of {i}?")
        for idx, opt in enumerate(options):
            print(f"{idx + 1}) {opt}")

        # 4. Get user choice
        try:
            choice = int(input("Your answer (1-4): "))
            user_answer = options[choice - 1]
        except (ValueError, IndexError):
            print("Invalid input! Treating it as a wrong answer.")
            user_answer = None

        # 5. Check answer and log result
        if user_answer == correct_answer:
            print("Correct! ✅")
            score += 1
            results_log.append((i, correct_answer, "Correct"))
        else:
            print(f"Wrong! ❌ The correct answer was {correct_answer}")
            results_log.append((i, correct_answer, "Wrong"))

    # 6. Final Score
    print("\n" + "="*20)
    print(f"Quiz Over! Your final score is: {score}/{len(range(start, end + 1))}")
    
    # 7. Review Section
    show_review = input("\nWould you like to see a review of all answers? (yes/no): ").lower()
    if show_review == 'yes' or show_review == 'y':
        print("\n--- Review Table ---")
        print(f"{'Number':<10} | {'Square':<10} | {'Result'}")
        print("-" * 35)
        for num, ans, res in results_log:
            print(f"{num:<10} | {ans:<10} | {res}")

if __name__ == "__main__":
    start_game()