class IntegerSet:
    def __init__(self, numbers):
        if not all(isinstance(num, int) for num in numbers):
            raise ValueError("All elements must be integers")
        self.numbers = set(numbers)
    
    def sum(self):
        return sum(self.numbers)
    
    def average(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0
    
    def maximum(self):
        return max(self.numbers) if self.numbers else None
    
    def minimum(self):
        return min(self.numbers) if self.numbers else None
import unittest

class TestIntegerSet(unittest.TestCase):
    def setUp(self):
        self.set1 = IntegerSet([1, 2, 3, 4, 5])
        self.set2 = IntegerSet([10, 20, 30])
        self.set3 = IntegerSet([-1, -2, -3, -4])
        self.set4 = IntegerSet([])

    def test_sum(self):
        self.assertEqual(self.set1.sum(), 15)
        self.assertEqual(self.set2.sum(), 60)
        self.assertEqual(self.set3.sum(), -10)
        self.assertEqual(self.set4.sum(), 0)

    def test_average(self):
        self.assertEqual(self.set1.average(), 3)
        self.assertEqual(self.set2.average(), 20)
        self.assertEqual(self.set3.average(), -2.5)
        self.assertEqual(self.set4.average(), 0)

    def test_maximum(self):
        self.assertEqual(self.set1.maximum(), 5)
        self.assertEqual(self.set2.maximum(), 30)
        self.assertEqual(self.set3.maximum(), -1)
        self.assertIsNone(self.set4.maximum())

    def test_minimum(self):
        self.assertEqual(self.set1.minimum(), 1)
        self.assertEqual(self.set2.minimum(), 10)
        self.assertEqual(self.set3.minimum(), -4)
        self.assertIsNone(self.set4.minimum())

if __name__ == '__main__':
    unittest.main()
