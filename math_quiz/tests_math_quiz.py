import unittest
from math_quiz import generate_random_integer, select_random_operator, create_problem_and_answer

class TestMathQuizFunctions(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if the function generates numbers within the specified range
        for _ in range(100):  # Run multiple times to ensure randomness
            result = generate_random_integer(1, 10)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 10)

    def test_select_random_operator(self):
        # Test if the function selects one of the specified operators
        operators = {'+', '-', '*'}
        for _ in range(100):  # Run multiple times to ensure randomness
            result = select_random_operator()
            self.assertIn(result, operators)

    def test_create_problem_and_answer(self):
        # Test addition
        problem, answer = create_problem_and_answer(5, 3, '+')
        self.assertEqual(problem, "5 + 3")
        self.assertEqual(answer, 8)

        # Test subtraction
        problem, answer = create_problem_and_answer(5, 3, '-')
        self.assertEqual(problem, "5 - 3")
        self.assertEqual(answer, 2)

        # Test multiplication
        problem, answer = create_problem_and_answer(5, 3, '*')
        self.assertEqual(problem, "5 * 3")
        self.assertEqual(answer, 15)

if __name__ == "__main__":
    unittest.main()
