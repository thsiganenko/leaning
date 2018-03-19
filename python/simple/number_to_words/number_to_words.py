#!/usr/bin/env python3
def _variant_of_word(n, variants):
    """
    Функция выбирает и возвращает вариант слова с правильным окончанием
    из переданного списка. Порядок вариантов слова должен соответствовать
    правилу  1, 2, 5.

    Например:
        ('копейка', 'копейки', 'копеек')
        ('рубль', 'рубля', 'рублей')
    """
    if 11 <= n % 100 <= 14:
        return variants[2]
    if n % 10 == 1:
        return variants[0]
    if 1 < n % 10 < 5:
        return variants[1]

    return variants[2]


def convert_int_to_text(num):
    """
    Функция принимает целое число, и возвращает строку  - запись числа
    прописью.

    Например:
    >>> convert_int_to_text(1234567)
    'один миллион двести тридцать четыре тысячи пятьсот шестьдесят семь'
    """
    literals_numbers = {
        'units': (
            'нуль',
            'один',
            'два',
            'три',
            'четыре',
            'пять',
            'шесть',
            'семь',
            'восемь',
            'девять',
            'десять',
            'одиннадцать',
            'двенадцать',
            'тринадцать',
            'четырнадцать',
            'пятнадцать',
            'шестнадцать',
            'семнадцать',
            'восемнадцать',
            'девятнадцать'
        ),
        'decades': (
            '',
            'десять',
            'двадцать',
            'тридцать',
            'сорок',
            'пятьдесят',
            'шестьдесят',
            'семьдесят',
            'восемьдесят',
            'девяносто'
        ),
        'hundreds': (
            '',
            'сто',
            'двести',
            'триста',
            'четыреста',
            'пятьсот',
            'шестьсот',
            'семьсот',
            'восемьсот',
            'девятьсот'
        )
    }

    order = (
        ('тысяча', 'тысячи', 'тысяч'),
        ('миллион', 'миллиона', 'миллионов'),
        ('миллиард', 'миллиарда', 'миллиардов')
    )

    if num == 0:
        return 'нуль'

    triads_numbers = []
    triads_words = []

    while num:
        triads_numbers.append(num % 1000)
        num //= 1000

    for group, triad in enumerate(triads_numbers):
        literal = []
        hundred, rest = divmod(triad, 100)

        if hundred:
            literal.append(literals_numbers['hundreds'][hundred])

        if 0 < rest < 20:
            literal.append(literals_numbers['units'][rest])
        elif rest:
            decade, unit = divmod(rest, 10)
            literal.append(literals_numbers['decades'][decade])
            literal.append(literals_numbers['units'][unit])

        if triad and group != 0:
            literal.append(_variant_of_word(triad, order[group - 1]))

        triads_words.append(' '.join(literal))

    if len(triads_words) > 1 and triads_words[1]:
        triads_words[1] = triads_words[1].replace('один', 'одна')
        triads_words[1] = triads_words[1].replace('два', 'две')

    return ' '.join(group for group in reversed(triads_words) if group)


def number_to_words(num):
    """
    Функция number_to_words принимает в качестве параметра число с
    плавающей точкой, и возвращает строку, содержащее запись числа
    в бухгалтерском формате.

    Например:
    >>> number_to_words(34567.89)
    '34 567 (тридцать четыре тысячи пятьсот шестьдесят семь) рублей 89 копеек'
    """
    measure = {
        'penny': ('копейка', 'копейки', 'копеек'),
        'rouble': ('рубль', 'рубля', 'рублей'),
    }

    rouble = int(num)
    penny = int(round((num - rouble) * 100))

    result = []
    result.append('{:,d}'.format(rouble).replace(',', ' '))
    result.append('({})'.format(convert_int_to_text(rouble)))
    result.append(_variant_of_word(rouble, measure['rouble']))
    result.append('{:02d}'.format(penny))
    result.append(_variant_of_word(penny, measure['penny']))

    return ' '.join(result)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
