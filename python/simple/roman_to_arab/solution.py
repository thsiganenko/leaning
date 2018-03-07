from collections import OrderedDict


def roman_to_arab(roman: str) -> int:
    """Конвертирует Римскую запись числа в Арабскую"""
    ARAB_NUMBERS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    ROMAN_NUMBERS = [1, 5, 10, 50, 100, 500, 1000]
    result = 0
    prev = 0
    for char in roman:
        cur = ROMAN_NUMBERS[ARAB_NUMBERS.index(char)]
        if  cur > prev:
            result += cur - prev * 2
        else:
            result += cur
        prev = cur

    return result
