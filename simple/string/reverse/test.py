#!/usr/bin/env python3
import unittest
import solutions


class TestReverseString(unittest.TestCase):

    def setUp(self):
        self.functions = []

        for name in dir(solutions):
            if not name.startswith('_'):
                self.functions.append(name)

    def test_static_string(self):
        source = 'Hello world!!!'
        result = '!!!dlrow olleH'

        for func in self.functions:
            with self.subTest(func=func):
                self.assertEqual(result, getattr(solutions, func)(source))

    def test_empty_string(self):
        source = ''
        result = ''

        for func in self.functions:
            with self.subTest(func=func):
                self.assertEqual(result, getattr(solutions, func)(source))
        
    def test_number(self):
        source = 1234567

        for func in self.functions:
            with self.subTest(func=func):
                with self.assertRaises(TypeError):
                    getattr(solutions, func)(source)


if __name__ == '__main__':
    unittest.main()
