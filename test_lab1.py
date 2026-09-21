import unittest
from lab1 import wins_rock_scissors_paper, factorial, fibonacci, sum_to_goal, UpCounter, DownCounter


class TestLab1(unittest.TestCase):
    def test_wins_rock_scissors_paper(self):
        self.assertTrue(wins_rock_scissors_paper("rock", "scissors"))
        self.assertTrue(wins_rock_scissors_paper("paper", "rock"))
        self.assertTrue(wins_rock_scissors_paper("scissors", "paper"))
        self.assertTrue(wins_rock_scissors_paper("ROCK", "Scissors"))
        self.assertFalse(wins_rock_scissors_paper("rock", "paper"))
        self.assertFalse(wins_rock_scissors_paper("rock", "rock"))

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(6), 8)

    def test_sum_to_goal(self):
        val1, val2 = sum_to_goal([1, 2, 3, 4], 5)
        self.assertEqual(val1 + val2, 5)
        self.assertEqual(sum_to_goal([1, 2, 3], 10), (None, None))

    def test_counters(self):
        up = UpCounter(2)
        self.assertEqual(up.count(), 0)
        up.update()
        self.assertEqual(up.count(), 2)

        down = DownCounter(3)
        self.assertEqual(down.count(), 0)
        down.update()
        self.assertEqual(down.count(), -3)


if __name__ == "__main__":
    unittest.main()