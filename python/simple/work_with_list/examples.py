def concat_items(lst):
    """Возвращает строку, содержащую объедененные элементы списка"""
    if len(lst) < 2:
        return ''.join(lst)
    return '{} and {}'.format(', '.join(lst[:-1]), lst[-1])


def draw_chars(lst):
    """Поворачивает на 90 градусов изображение в виде матрицы"""
    x = len(lst)
    lst = [[lst[x - 1 - j][i] for j in range(x)] for i in range(len(lst[0]))]
    for s in lst:
        print(' '.join(s))


if __name__ == '__main__':
    grid = [['.', 'O', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', 'O', '.', '.', '.', '.']]

    for s in grid:
        print(' '.join(s))
    draw_chars(grid)
