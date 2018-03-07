def collatz(num):
    return (3 * num) + 1 if num % 2 else num // 2


def main(number):
    try:
        if number > 1:
            while number != 1:
                number = collatz(number)
                print(number)
    except TypeError:
        pass
