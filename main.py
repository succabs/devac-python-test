import unittest


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def power(x, y):
    """Calculate x raised to the power y without using math.pow."""
    result = 1
    for _ in range(int(y)):
        result *= x
    return result


print(add(5, 4))  # --> 9
print(multiply(3, 4))  # --> 12
print(power(2, 8))  # --> 256


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(6, 5), 11)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, -9), -10)
        self.assertNotEqual(add(0, 2), 3)
        self.assertNotEqual(add(10, -5), 10)

    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(0, -10), 0)
        self.assertEqual(multiply(-20, 3), -60)
        self.assertNotEqual(multiply(0, 2), 3)
        self.assertNotEqual(multiply(5, 5), 20)

    def test_power(self):
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(10, 0), 1)
        self.assertEqual(power(60, 1), 60)
        self.assertEqual(power(4, 2), 16)
        self.assertNotEqual(power(5, 2), 20)
        self.assertNotEqual(power(2, 4), 12)


if __name__ == "__main__":
    unittest.main()
