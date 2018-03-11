def task_01(n):
    """От 1 до n

    Дано натуральное число n. Выведите все числа от 1 до n включительно
    в одну строку разделенных пробелом

    Например:
    >>> task_01(5)
    1 2 3 4 5
    """
    if n == 0:
        return
    task_01(n-1)
    print(n, end=' ')


def task_02(n):
    """Точная степень двойки

    Дано натуральное числое N. Выведите слово 'YES',
    если число N является точной степенью двойки, или слово
    'NO' в противном случае.
    Операцией возведения в степень пользоваться нельзя!

    Например:
    >>> task_02(8)
    YES

    >>> task_02(3)
    NO
    """
    if n == 1:
        print('YES')
        return
    elif n % 2 == 1 or n == 0:
        print('NO')
        return
    task_02(n//2)


def task_03(n):
    """Сумма цифр числа

    Дано натуральное число N. Вычислите сумму его цифр

    При решении этой задачи нельзя использовать строки,
    списки, массивы (ну и цыклы, разумеется).

    Например:
    >>> task_03(179)
    17
    """
    def inner(n):
        if n == 0:
            return 0
        return (n % 10) + inner(n // 10)

    print(inner(n))


def task_04(n):
    """Цифры числа справа налево

    Дано натуральное число N. Выведите все его цифры по
    одной, в обратном порядке, разделяя их пробелами.

    При решении этой задачи нельзя использовать строки,
    списки, массивы (ну и цыклы, разумеется). Разрешена
    только рекурсия и целочисленная арифметика.

    Например:
    >>> task_04(179)
    9 7 1
    """
    if n < 10:
        print(n)
    else:
        print(n % 10, end=' ')
        task_04(n // 10)


def task_05(n):
    """Цифры числа слева направо.

    Дано натуральное число N. Выведите его цифры по одной, в обычном
    порядке, разделяя их пробелами.

    При решении этой задачи нельзя использовать строки, списки,
    массивы(ну и циклы, разумеется). Разрешена только рекурсия
    и целочисленная арифметика.

    Например:
    >>> task_05(179)
    1 7 9
    """
    def inner(n):
        cur = n % 10
        if n >= 10:
            inner(n // 10)
        print(cur, end=' ')

    inner(n)
    print()


def task_06(word):
    """Палиндром

    Дано слово, состоящее только из строчных латинчких букв.
    Проверьте, является ли это слово палиндромом. Выведите YES
    или NO.

    При решении задачи нельзя пользоваться циклами, в решениях на
    Python нельзя использовать срезы с шагом, отличным от 1

    Например:
    >>> task_06('ahha')
    YES

    >>> task_06('hello')
    NO
    """

    def reverse(word):
        if not word:
            return ''
        return reverse(word[1:]) + word[0]
    print('YES' if reverse(word) == word else 'NO')


def hanoi(n, a, b, c):
    """Решение задачи про Ханойские башни"""
    if n != 0:
        hanoi(n - 1, a, c, b)
        print('Move ', a, ' to ', c)
        hanoi(n - 1, b, a, c)
