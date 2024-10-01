import unittest
from euler import eulers_totient

class TestEulerTotient(unittest.TestCase):

    def test_euler_totient(self):
        self.assertEqual(eulers_totient(1), 1)
        self.assertEqual(eulers_totient(2), 1)
        self.assertEqual(eulers_totient(3), 2)
        self.assertEqual(eulers_totient(4), 2)
        self.assertEqual(eulers_totient(5), 4)
        self.assertEqual(eulers_totient(6), 2)
        self.assertEqual(eulers_totient(7), 6)
        self.assertEqual(eulers_totient(8), 4)
        self.assertEqual(eulers_totient(9), 6)
        self.assertEqual(eulers_totient(10), 4)

    def test_large_number(self):
        self.assertEqual(eulers_totient(13), 12)
        self.assertEqual(eulers_totient(17), 16)

    def test_edge_cases(self):
        self.assertEqual(eulers_totient(0), 0)
        self.assertEqual(eulers_totient(1), 1)

if __name__ == "__main__":
    unittest.main()