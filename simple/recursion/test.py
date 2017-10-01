#!/usr/bin/env python3

import sys
from io import StringIO
import unittest
import solutions


class TestSolutionForRecursion(unittest.TestCase):

    def setUp(self):
        self.save_out = sys.stdout
        sys.stdout = StringIO()

    def test_task_01(self):
        ''' От 1 до n

            Дано натуральное число n. Выведите все числа от 1 до n включительно
            в одну строку разделенных пробелом

            Например:
                input: 5
                output: 1 2 3 4 5

        '''

        source = []
        for i in range(10):
            solutions.task_01(i)
            sys.stdout.write('\n')
            source.append(' '.join([str(x) for x in range(1, i + 1)]))

        sys.stdout.seek(0)
        result = [s.strip() for s in sys.stdout.readlines()]

        for i, case in enumerate(source):
            with self.subTest(case=case, i=i):
                self.assertEqual(case, result[i])

    def test_task_02(self):
        ''' Точная степень двойки

            Дано натуральное числое N. Выведите слово 'YES',
            если число N является точной степенью двойки, или слово
            'NO' в противном случае.
            Операцией возведения в степень пользоваться нельзя!

            Например:
                input: 8
                output: YES

                input: 3
                output: NO

        '''
        source = [1, 2, 5, 8, 32, 50, 1024]
        result = ['YES', 'YES', 'NO', 'YES', 'YES', 'NO', 'YES']
        data = []

        for i in source:
            solutions.task_02(i)

        sys.stdout.seek(0)
        data = [ans.strip() for ans in sys.stdout.readlines()]
        for i, v in enumerate(result):
            with self.subTest(i=i, v=v):
                self.assertEqual(data[i], v)

    def test_task_03(self):
        ''' Сумма цифр числа

            Дано натуральное число N. Вычислите сумму его цифр

            При решении этой задачи нельзя использовать строки,
            списки, массивы (ну и цыклы, разумеется).

            Например:
                input: 179
                output: 17

        '''

        source = [1, 7, 13, 27, 42, 777, 1024, 4048, 10000]
        result = [1, 7, 4, 9, 6, 21, 7, 16, 1]
        data = []

        for num in source:
            solutions.task_03(num)

        sys.stdout.seek(0)
        data = [int(num.strip()) for num in sys.stdout.readlines()]

        for i, num in enumerate(result):
            with self.subTest(i=i, num=num):
                self.assertEqual(num, data[i])

    def test_task_04(self):
        ''' Цифры числа справа налево

            Дано натуральное число N. Выведите все его цифры по
            одной, в обратном порядке, разделяя их пробелами.

            При решении этой задачи нельзя использовать строки,
            списки, массивы (ну и цыклы, разумеется). Разрешена
            только рекурсия и целочисленная арифметика.

            Например:
                input: 179
                output: 9 7 1
        '''

        source = [1, 12, 378, 98754]
        result = ['1', '2 1', '8 7 3', '4 5 7 8 9']
        data = []

        for num in source:
            solutions.task_04(num)

        sys.stdout.seek(0)
        data = [s.strip() for s in sys.stdout.readlines()]

        for i, s in enumerate(result):
            with self.subTest(i=i, s=s):
                self.assertEqual(s, data[i])

    def test_task_05(self):
        ''' Цифры числа слева направо.

            Дано натуральное число N. Выведите его цифры по одной, в обычном
            порядке, разделяя их пробелами.

            При решении этой задачи нельзя использовать строки, списки,
            массивы(ну и циклы, разумеется). Разрешена только рекурсия
            и целочисленная арифметика.

            Например:
                input: 179
                output: 1 7 9

        '''
        source = [1, 42, 637, 1945, 98765]
        result = ['1', '4 2', '6 3 7', '1 9 4 5', '9 8 7 6 5']
        data = []

        for n in source:
            solutions.task_05(n)

        sys.stdout.seek(0)
        data = [s.strip() for s in sys.stdout.readlines()]

        for i, ans in enumerate(result):
            with self.subTest(i=i, ans=ans):
                self.assertEqual(ans, data[i])

    def test_task_06(self):
        ''' Палиндром

            Дано слово, состоящее только из строчных латинчких букв.
            Проверьте, является ли это слово палиндромом. Выведите YES
            или NO.

            При решении задачи нельзя пользоваться циклами, в решениях на
            Python нельзя использовать срезы с шагом, отличным от 1
        '''
        source = ['radar', 'yes', 'abccba', 'a']
        result = ['YES', 'NO', 'YES', 'YES']
        data = []

        for word in source:
            solutions.task_06(word)

        sys.stdout.seek(0)
        data = [ans.strip() for ans in sys.stdout.readlines()]

        for i, ans in enumerate(result):
            with self.subTest(i=i, ans=ans):
                self.assertEqual(ans, data[i])

    def tearDown(self):
        sys.stdout = self.save_out

if __name__ == '__main__':
    unittest.main()
