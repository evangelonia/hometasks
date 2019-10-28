import unittest
import to_binary


class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(int(to_binary.to_binary_func(5)), 101, "Should be 101")


if __name__ == "__main__":
    unittest.main()
