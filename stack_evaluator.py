"""Tests for stack_evaluator.py. Run with:  python test_stack_evaluator.py"""

import os
import tempfile
import unittest

from stack_evaluator import ExpressionError, Stack, evaluate, format_result, process_file


class StackTests(unittest.TestCase):
    def test_push_pop_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 1)

    def test_empty_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()


class EvaluateTests(unittest.TestCase):
    def check(self, expression, expected):
        self.assertEqual(format_result(evaluate(expression)), expected)

    def test_assignment_examples(self):
        self.check("3 + 5 * 2", "13")
        self.check("(8 / 4) + 7 * 2", "16")
        self.check("10 - (2 + 3) * 4", "-10")

    def test_precedence_and_brackets(self):
        self.check("2 + 3 * 4", "14")
        self.check("(2 + 3) * 4", "20")
        self.check("100 / 10 / 5", "2")
        self.check("10 - 4 - 3", "3")
        self.check("((1 + 2) * (3 + 4))", "21")

    def test_decimals_and_division(self):
        self.check("7 / 2", "3.5")
        self.check("0.1 + 0.2", "0.3")

    def test_unary_minus(self):
        self.check("-5 + 3", "-2")
        self.check("2 * -3", "-6")
        self.check("(-2 + 3) * 4", "4")
        self.check("--4", "4")

    def test_errors(self):
        for bad in ["5 / 0", "(1 + 2", "1 + 2)", "3 +", "* 4", "2 3", "abc", "", "()", "2 (3)"]:
            with self.assertRaises(ExpressionError, msg=bad):
                evaluate(bad)


class FileTests(unittest.TestCase):
    def test_file_round_trip(self):
        with tempfile.TemporaryDirectory() as folder:
            source = os.path.join(folder, "in.txt")
            target = os.path.join(folder, "out.txt")
            with open(source, "w") as file:
                file.write("3 + 5 * 2\n-----\n1 / 0\n-----\n10 - (2 + 3) * 4\n")
            process_file(source, target)
            with open(target) as file:
                self.assertEqual(file.read(), "13\n-----\nError: division by zero\n-----\n-10\n")


if __name__ == "__main__":
    unittest.main()