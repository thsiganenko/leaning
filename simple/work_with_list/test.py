#!/usr/bin/env python

import sys
from io import StringIO
import unittest
from examples import concat_items
from examples import draw_chars


class TestForListConcat(unittest.TestCase):
    def test_normal_mode(self):
        spam = [['apples', 'bananas', 'tofu', 'cats'],
                ['apples', 'bananas', 'cats'],
                ['apples', 'bananas'],
                ['apples']]

        result = ['apples, bananas, tofu and cats',
                  'apples, bananas and cats',
                  'apples and bananas',
                  'apples']

        for i, lst in enumerate(spam):
            with self.subTest(i=i, lst=lst):
                self.assertEqual(concat_items(lst), result[i])


class TestForFunctionDrawChars(unittest.TestCase):
    def setUp(self):
        self.save_io = sys.stdout
        sys.stdout = StringIO()

    def teamDown(self):
        sys.stdout = self.save_io

    def test_normal_mode(self):
        source = [['.', 'O', '.', '.', '.', '.'],
                  ['.', 'O', 'O', '.', '.', '.'],
                  ['O', 'O', 'O', 'O', '.', '.'],
                  ['O', 'O', 'O', 'O', 'O', '.'],
                  ['.', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', '.'],
                  ['O', 'O', 'O', 'O', '.', '.'],
                  ['.', 'O', 'O', '.', '.', '.'],
                  ['.', 'O', '.', '.', '.', '.']]

        result = ['. . O O . O O . .',
                  'O O O O O O O O O',
                  '. O O O O O O O .',
                  '. . O O O O O . .',
                  '. . . O O O . . .',
                  '. . . . O . . . .']

        draw_chars(source)
        sys.stdout.seek(0)
        output = [s.strip() for s in sys.stdout.readlines()]
        self.assertEqual(output, result)


if __name__ == '__main__':
    unittest.main()
