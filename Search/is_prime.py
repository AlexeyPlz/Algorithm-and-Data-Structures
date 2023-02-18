def is_prime(number: int) -> bool:
    """
    Проверка на простое число.\n
    Сложность O(√n).
    """
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    print(is_prime(int(input())))
