from unittest import TestCase
from arithmetic_app import generate_question

class TestArithmeticApp(TestCase):

    def test_generate_problem_is_not_negative(self):
        number_one, number_two = generate_question()
        self.assertEqual(number_one - number_two >= 0, True)

    def test_generate_problem_values(self):
        number_one, number_two = generate_question()
        self.assertEqual(number_one - number_two, max(number_one, number_two) - min(number_one, number_two))

