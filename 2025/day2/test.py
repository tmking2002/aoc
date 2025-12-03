import unittest
from part1 import check_validity, check_range, find_sum

class TestPart1(unittest.TestCase):

    def test_sample(self):
        with open('day2/sample.txt') as f:
            data = f.read()
            ranges = data.split(',')
        self.assertEqual(find_sum(ranges), 1227775554)

    def test_validity_1(self):
        number = 505
        self.assertEqual(check_validity(number), True)

    def test_validity_2(self):
        number = 11
        self.assertEqual(check_validity(number), False)

    def test_validity_3(self):
        number = 12
        self.assertEqual(check_validity(number), True)

    def test_validity_4(self):
        number = 1188511885
        self.assertEqual(check_validity(number), False)

    def test_validity_5(self):
        number = 38593859
        self.assertEqual(check_validity(number), False)

    def test_validity_6(self):
        number = 123456789
        self.assertEqual(check_validity(number), True)

if __name__ == '__main__':
    unittest.main()