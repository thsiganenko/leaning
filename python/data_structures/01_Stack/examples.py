#!/usr/bin/env python
"""Примеры использование структуры данных Стек

   дата начала работы: 2016-07-03
   дата завершения работы: 2016-07-04
   рефакторинг: 2018-03-04
"""
from stack import Stack


def string_reverse(string):
    """Переворачивает строку

    >>> string_reverse('):')
    ':)'
    """
    stack = Stack()
    for i in string:
        stack.push(i)
    return ''.join([stack.pop() for __ in range(len(stack))])


def check_brackets(string):
    """Проверяет соответствие открывающих и закрывающих скобок

    >>> check_brackets('([{}])')
    True
    >>> check_brackets('([(]))')
    False
    """
    stack = Stack()
    OPEN_BRACKETS = '([{'
    CLOSE_BRACKETS = ')]}'

    for i in string:
        if i in OPEN_BRACKETS:
            stack.push(i)
            continue
        if i in CLOSE_BRACKETS:
            if stack.is_empty():
                return False
            if OPEN_BRACKETS.index(stack.pop()) != CLOSE_BRACKETS.index(i):
                return False

    if stack.is_empty():
        return True

    return False


def decimal_to_binary(number):
    """Конвертор десятичного числа в двоичное

    >>> decimal_to_binary(25)
    '11001'
    """
    stack = Stack()
    number = int(number)
    while number != 0:
        stack.push(number % 2)
        number //= 2

    return ''.join([str(stack.pop()) for i in range(len(stack))])


def decimal_to_hexadecimal(number):
    """Конвертор десятичного числа в шеснадцатеричное

    >>> decimal_to_hexadecimal(365)
    '16D'
    """
    stack = Stack()
    number = int(number)
    alphabet = '0123456789ABCDEF'

    while number > 0:
        char = alphabet[number % 16]
        stack.push(char)
        number //= 16

    return ''.join([stack.pop() for i in range(len(stack))])


def infix_to_postfix(expression):
    """Преобразование выражения из инфиксной нотации в постфиксную

    >>> infix_to_postfix('A*(B+C*((D-4)*(8+3)/7)+E)/2')
    'A B C D 4 - 8 3 + * 7 / * + E + * 2 /'
    """
    stack = Stack()
    PRIORITY_OPERATORS = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    output = []

    for i in expression:
        if i == ' ':
            continue
        elif i == '(':
            stack.push(i)
        elif i == ')':
            while stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        elif i in PRIORITY_OPERATORS:
            if stack.is_empty():
                stack.push(i)
            elif PRIORITY_OPERATORS[i] > PRIORITY_OPERATORS[stack.peek()]:
                stack.push(i)
            else:
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())
                stack.push(i)
        else:
            output.append(i)

    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)


def calc_postfix(expression):
    """Вычисление постфиксного выражения

    >>> calc_postfix('2 3 + 45 -')
    -40.0
    """
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '^': lambda x, y: x**y
    }
    stack = Stack()
    expression = expression.split()
    for i in expression:
        if i in operators:
            try:
                y = stack.pop()
                x = stack.pop()
            except IndexError:
                return 'Not a balanced expression'
            try:
                result = operators[i](x, y)
            except KeyError:
                return 'Error calculate'
            stack.push(result)
        else:
            try:
                stack.push(float(i))
            except ValueError:
                return 'Error type of operands'

    return stack.pop()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
