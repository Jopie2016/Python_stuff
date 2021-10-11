import unittest
import oop


class TestOop(unittest.TestCase):

    def test_walk(self):
        result = oop.john.walk()
        self.assertEqual(result, "John Is walking...")


if __name__ == '__main__': #Code doesn't work but
    unittest.main()
