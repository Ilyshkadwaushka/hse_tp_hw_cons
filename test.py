import unittest
from main import _min, _mult
import time
import functools

array = [int(i) for i in open('file.txt').readline().split()]

class MyTests(unittest.TestCase):

    def test_min_func(self):
        time_start = time.time()
        self.assertEqual(_min(array), min(array))
        print('Потраченное время на работу функции _min = ', time.time()  - time_start)

    def test_mult_func(self):
        time_start = time.time()
        self.assertEqual(_mult(array), functools.reduce(lambda x, y: x * y, array))
        print('Потраченное время на работу функции _mult = ', time.time() - time_start)


if __name__ == '__main__':
    unittest.main()
