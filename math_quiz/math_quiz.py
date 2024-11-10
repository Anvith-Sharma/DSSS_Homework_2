import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within a specified range.

    """
    return random.randint(min_value, max_value)


def select_random_operator():
    """
    Select a random mathematical operator.

    """
    return random.choice(['+', '-', '*'])


def create_problem_and_answer(number1, number2, operator):
    """
    Create a math problem string and calculate the answer based on the given operator.

    """
    problem = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:  # operator == '*'
        answer = number1 * number2

    return problem, answer  


def math_quiz():
    """
    Run the math quiz game where the player answers a series of randomly generated
    math questions. The score is calculated based on the number of correct answers.
    """
    score = 0
    total_questions = 3  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate two random numbers and an operator
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)
        operator = select_random_operator()

        # Generate the math problem and its correct answer
        problem, correct_answer = create_problem_and_answer(number1, number2, operator)
        print(f"\nQuestion: {problem}")

        # Get and validate the user's answer
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue  # Skip to the next question if input is invalid

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()

