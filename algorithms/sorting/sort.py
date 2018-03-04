def bubble(sequence: list) -> list:
    """Сортировка пузырьком"""
    lst = sequence[:]
    length = len(lst)
    for i in range(length):
        exchange = False
        for j in range(length - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                exchange = True
        if not exchange:
            break

    return lst


def selection(sequence: list) -> list:
    """Сортировка выбором"""
    source = sequence[:]
    result = []
    while source:
        min_value, position = source[0], 0
        for i, value in enumerate(source):
            if min_value > value:
                min_value, position = value, i
        result.append(source.pop(position))

    return result


def quick(sequence: list) -> list:
    """Быстрая сортировка"""
    if len(sequence) < 2:
        return sequence
    base = sequence.pop(len(sequence) // 2)
    greater = []
    less = []
    for value in sequence:
        if value > base:
            greater.append(value)
        else:
            less.append(value)

    return quick(less) + [base] + quick(greater)


def merge(sequence: list) -> list:
    """Сортировка слиянием"""
    if len(sequence) < 2:
        return sequence

    middle = len(sequence) // 2
    right = merge(sequence[:middle])
    left = merge(sequence[middle:])

    result = []
    while True:
        if right and left:
            if right[0] < left[0]:
                result.append(right.pop(0))
            else:
                result.append(left.pop(0))
        else:
            break

    if right:
        result.extend(right)
    if left:
        result.extend(left)

    return result
