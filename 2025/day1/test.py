import unittest
from part2 import find_password

class TestPart2(unittest.TestCase):

    def test_sample(self):
        with open('day1/sample.txt') as f:
            data = f.read()
            lines = data.split('\n')
        self.assertEqual(find_password(lines), 6)

    def test_ex1(self):
        lines = ['L50', 'R50']
        self.assertEqual(find_password(lines), 1)
    
    def test_ex2(self):
        lines = ['L50', 'L50']
        self.assertEqual(find_password(lines), 1)

    def test_ex3(self):
        lines = ['R50', 'L50']
        self.assertEqual(find_password(lines), 1)

    def test_ex4(self):
        lines = ['R50', 'R50']
        self.assertEqual(find_password(lines), 1)

    def test_ex5(self):
        lines = ['L150', 'L50']
        self.assertEqual(find_password(lines), 2)

    def test_ex6(self):
        lines = ['L150', 'R50']
        self.assertEqual(find_password(lines), 2)

    def test_ex7(self):
        lines = ['R150', 'L50']
        self.assertEqual(find_password(lines), 2)

    def test_ex8(self):
        lines = ['R150', 'R50']
        self.assertEqual(find_password(lines), 2)
    
    def test_ex9(self):
        lines = ['L50', 'R100']
        self.assertEqual(find_password(lines), 2)

    def test_ex10(self):
        lines = ['R1000']
        self.assertEqual(find_password(lines), 10)

    def test_ex11(self):
        lines = ['R50', 'R400']
        self.assertEqual(find_password(lines), 5)

    def test_ex12(self):
        lines = ['L50', 'R101']
        self.assertEqual(find_password(lines), 2)


if __name__ == '__main__':
    unittest.main()