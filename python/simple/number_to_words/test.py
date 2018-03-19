#!/usr/bin/env python3
from unittest import TestCase
from unittest import main
from number_to_words import convert_int_to_text
from number_to_words import number_to_words


class TestNumberToWords(TestCase):
    def test_convert_int_to_text(self):
        self.assertEqual(
            convert_int_to_text(1234567),
            ('один миллион двести тридцать четыре тысячи '
             'пятьсот шестьдесят семь')
        )

    def test_number_to_words(self):
        self.assertEqual(number_to_words(0.12), '0 (нуль) рублей 12 копеек')
        self.assertEqual(number_to_words(11.40),
                         '11 (одиннадцать) рублей 40 копеек')
        self.assertEqual(number_to_words(200),
                         '200 (двести) рублей 00 копеек')
        self.assertEqual(number_to_words(1000),
                         '1 000 (одна тысяча) рублей 00 копеек')
        self.assertEqual(number_to_words(99.99),
                         '99 (девяносто девять) рублей 99 копеек')
        self.assertEqual(number_to_words(3),
                         '3 (три) рубля 00 копеек')
        self.assertEqual(number_to_words(1.02),
                         '1 (один) рубль 02 копейки')
        self.assertEqual(
            number_to_words(1000234),
            '1 000 234 (один миллион двести тридцать четыре) рубля 00 копеек')
        self.assertEqual(
            number_to_words(1511234567.89),
            ('1 511 234 567 (один миллиард пятьсот одиннадцать миллионов '
             'двести тридцать четыре тысячи пятьсот шестьдесят семь) '
             'рублей 89 копеек')
        )


if __name__ == '__main__':
    main()
