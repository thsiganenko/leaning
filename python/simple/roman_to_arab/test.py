#!/usr/bin/env python
from solution import roman_to_arab
from unittest import TestCase
from unittest import main


class TestRomanToArab(TestCase):
    def test_base_case(self):
        """Тест базового использования функции конвертера"""
        self.assertEqual(roman_to_arab('I'), 1)
        self.assertEqual(roman_to_arab('IV'), 4)
        self.assertEqual(roman_to_arab('V'), 5)
        self.assertEqual(roman_to_arab('IX'), 9)
        self.assertEqual(roman_to_arab('XXI'), 21)
        self.assertEqual(roman_to_arab('XLII'), 42)
        self.assertEqual(roman_to_arab('MMXIV'), 2014)


if __name__ == '__main__':
    main()
