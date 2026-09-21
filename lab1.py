def wins_rock_scissors_paper(player, opponent):
    p = player.lower()
    o = opponent.lower()
    if p == "rock" and o == "scissors":
        return True
    elif p == "paper" and o == "rock":
        return True
    elif p == "scissors" and o == "paper":
        return True
    return False


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 0
    curr = 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def sum_to_goal(numbers, goal):
    seen = {}
    for i, num in enumerate(numbers):
        complement = goal - num
        if complement in seen:
            return complement, num
        seen[num] = i
    return None, None


class UpCounter:
    def __init__(self, step_size=1):
        self._step_size = step_size
        self._count = 0

    def count(self):
        return self._count

    def update(self):
        self._count += self._step_size


class DownCounter(UpCounter):
    def __init__(self, step_size=1):
        super().__init__(step_size)

    def update(self):
        self._count -= self._step_size