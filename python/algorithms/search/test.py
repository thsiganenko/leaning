#!/usr/bin/env python
from unittest import TestCase
from unittest import main
# from solution import binary_search
from binary_search import binary_search


class TestForBinarySearch(TestCase):
    def test_normal_mode(self):
        data = list(range(100))
        for num in range(100):
            with self.subTest(num=num):
                self.assertEqual(binary_search(data, num), num)

    def test_three_item_in_list(self):
        data = [1, 2, 3]
        for num in range(1, 4):
            with self.subTest(num=num):
                self.assertEqual(binary_search(data, num), num - 1)

    def test_two_item_in_list(self):
        data = [1, 2]
        for num in range(1, 3):
            with self.subTest(num=num):
                self.assertEqual(binary_search(data, num), num - 1)

    def test_one_item_in_list(self):
        data = [42]
        self.assertEqual(binary_search(data, 42), 0)

    def test_missing_values(self):
        data = list(range(10))
        search = [-1, 42, 10]
        for num in search:
            with self.subTest(num=num):
                self.assertIsNone(binary_search(data, num))


if __name__ == '__main__':
    main()
