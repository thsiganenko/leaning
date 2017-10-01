def simple_reverse(s):
    return s[::-1]

def reads_with_end_line(s):
    result = []
    length = len(s)
    for i in range(length):
        result.append(s[length-1-i])
    return ''.join(result)

def reverse_with_recursion(s):
    return reverse_with_recursion(s[1:]) + s[0] if s else ''

def change_two_char(s):
        s = list(s)
        length = len(s)
        for i in range(length // 2):
            s[i], s[length - 1 - i] = s[length - 1 - i], s[i]

        return ''.join(s)

def reads_with_end_line_oneline(s):
    return ''.join(s[i] for i in range(len(s) - 1, -1, -1))

def concatination_char_with_empty_string(s):
    result = ''
    for char in s:
        result = char + result
    return result

def using_reduce(s):
    from functools import reduce
    return reduce(lambda acc, cur: cur + acc, s, '')

