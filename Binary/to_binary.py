def to_binary(number: int) -> str:
    """
    Представление числа в двоичной системе.\n
    Сложность O(n).
    """
    if number == 0:
        return '0'
    result = ''
    while number:
        number, remain = divmod(number, 2)
        result += str(remain)
    return result[::-1]


if __name__ == '__main__':
    print(to_binary(int(input())))
