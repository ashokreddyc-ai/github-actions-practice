import unittest
from app import add,subtract

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 20), 30)
    def test_subtract(self):
        self.assertEqual(subtract(20, 5), 15)

if __name__ == "__main__":
    unittest.main()