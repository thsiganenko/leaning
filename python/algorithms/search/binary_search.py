def binary_search(array, item):
    """Реализация алгоритма бинарного поиска"""
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None
