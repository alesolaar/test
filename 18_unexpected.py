import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):
    def test_get_sqrt(self):
        self.assertEqual(get_sqrt(144),12)
        self.assertEqual(get_sqrt(0),0)

        with self.assertRaises(ValueError):
            get_sqrt(-1)

    def test_divide(self):
      self.assertEqual(divide(144,12),12)
      self.assertEqual(divide(0,5),0)

      with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()