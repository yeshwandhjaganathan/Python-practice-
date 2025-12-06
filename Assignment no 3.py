# all_tools_menu.py
# Combined small programs:
# - Number guessing game (while, break, continue, else)
# - Multiplication table generator
# - Simple CLI BMI calculator
# Also demonstrates: pass, break, continue, while-else
# Author: Yarvy for Yashwant

import random
import sys
import math

def number_guessing_game():
    """Number Guessing Game using while, break, continue, and while-else"""
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    print("\n--- Number Guessing Game ---")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have up to {max_attempts} attempts. Good luck!")

    while attempts < max_attempts:
        attempts += 1
        try:
            s = input(f"Attempt {attempts}/{max_attempts} — Enter your guess (or 'q' to quit): ").strip()
            if s.lower() == 'q':
                print("You chose to quit. Goodbye!")
                break                # demonstrate break
            guess = int(s)
        except ValueError:
            print("Invalid input — enter an integer or 'q' to quit.")
            continue                # demonstrate continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed {secret_number} in {attempts} attempts.")
            break                    # correct guess -> exit loop
    else:
        # This else runs only if loop didn't encounter a 'break' (i.e., used all attempts)
        print(f"Out of attempts — the number was {secret_number}. Better luck next time!")

    print("Number Guessing Game finished.\n")


def generate_multiplication_table(number, limit=10):
    """Prints multiplication table for given number up to limit."""
    print(f"\nMultiplication Table for {number} (1 to {limit}):")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")
    print()  # blank line


def multiplication_table_interactive():
    """Interactive wrapper with validation and demonstration of pass"""
    print("\n--- Multiplication Table Generator ---")
    while True:
        try:
            num_str = input("Enter an integer (or 'b' to go back to main menu): ").strip()
            if num_str.lower() == 'b':
                pass  # pass used as a no-op demonstration before breaking back to menu
                print("Returning to main menu...\n")
                break
            number = int(num_str)
            limit_str = input("Enter upper limit (default 10): ").strip()
            limit = int(limit_str) if limit_str else 10
            if limit <= 0:
                print("Limit should be positive. Try again.")
                continue
            generate_multiplication_table(number, limit)
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue


def bmi_calculator_cli():
    """
    Simple BMI CLI calculator:
    BMI = weight(kg) / (height(m) ** 2)
    Interprets BMI according to standard categories.
    """
    print("\n--- BMI CALCULATOR (CLI) ---")
    while True:
        try:
            s = input("Enter weight in kg (or 'b' to return to menu): ").strip()
            if s.lower() == 'b':
                print("Returning to main menu...\n")
                break
            weight = float(s)
            height = float(input("Enter height in meters (e.g., 1.75): ").strip())

            if weight <= 0 or height <= 0:
                print("Weight and height must be positive numbers.")
                continue

            bmi = weight / (height ** 2)
            bmi_rounded = round(bmi, 2)
            interpretation = get_bmi_interpretation(bmi)

            print(f"\nYour BMI is: {bmi_rounded}")
            print(f"Interpretation: {interpretation}\n")
            # after successful calculation, ask if user wants another or back to menu
            again = input("Calculate again? (y/n): ").strip().lower()
            if again != 'y':
                print("Returning to main menu...\n")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values (or 'b' to go back).")
            continue


def get_bmi_interpretation(bmi_value):
    """Returns BMI category string (standard simplified categories)."""
    # Use float comparisons; keep ranges similar to web standards
    if bmi_value < 18.5:
        return "Underweight"
    elif 18.5 <= bmi_value < 25:
        return "Healthy Weight"
    elif 25 <= bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"


def about_demo_control_statements():
    """Small demo showing pass, break, continue usage succinctly."""
    print("\n--- Control Statements Demo ---")
    items = [1, 2, 'skip', 4, 0, 5]
    print("Looping items and demonstrating continue/pass/break:")
    for x in items:
        if x == 'skip':
            print("found 'skip' — continue (skip this iteration)")
            continue
        if x == 0:
            print("found 0 — break (exit loop)")
            break
        # pass demonstration (no operation)
        if x == 4:
            pass  # intentionally do nothing here
        print("Processing item:", x)
    else:
        # only runs if loop did not encounter break
        print("Completed loop without break.")
    print("Demo finished.\n")


def main_menu():
    menu_text = """
==== PYTHON MINI-TOOLBOX ====
Choose an option:
1. Number Guessing Game
2. Multiplication Table Generator
3. BMI Calculator (CLI)
4. Control Statements Demo (while/break/continue/pass)
5. Exit
"""
    while True:
        print(menu_text)
        choice = input("Enter choice (1-5): ").strip()
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            multiplication_table_interactive()
        elif choice == '3':
            bmi_calculator_cli()
        elif choice == '4':
            about_demo_control_statements()
        elif choice == '5':
            print("Exiting. Have a nice day!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main_menu()
