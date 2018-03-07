#!/usr/bin/env python
import unittest
from random import randint
from random import randrange
import sort


class TestSortFunctions(unittest.TestCase):
    def setUp(self):
        self.sort_functions = []
        for name in dir(sort):
            if not name.startswith('_'):
                self.sort_functions.append(name)

    def test_static_set(self):
        test_data_set = (
            [],
            [2, 1],
            [3, 2, 1],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            ['i'],
            ['a', 'm'],
            ['i', 'a', 'm'],
            ['y', 'u', 'r', 'e', 'a', 'f' , 'i', 'p'],
        )
        for data in test_data_set:
            for func in self.sort_functions:
                with self.subTest(func=func):
                    self.assertEqual(sorted(data), getattr(sort, func)(data))

    def test_random_set(self):
        length = 10
        test_data_set = (
            [randint(1, 1000) for _ in range(length)],
            [chr(randrange(97, 123)) for _ in range(length)],
        )
        for data in test_data_set:
            for func in self.sort_functions:
                with self.subTest(func=func):
                    self.assertEqual(sorted(data), getattr(sort, func)(data))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
