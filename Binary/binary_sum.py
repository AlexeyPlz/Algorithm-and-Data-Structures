def binary_sum(number_one: str, number_two: str) -> str:
    """
    Сложение двух бинарных чисел.\n
    Сложность O(n).
    """
    data_one = list(map(int, number_one.strip()))
    data_two = list(map(int, number_two.strip()))
    memory, result = 0, ''
    while data_one or data_two or memory:
        total = 0
        if memory:
            total += memory
        if data_one:
            total += data_one.pop(-1)
        if data_two:
            total += data_two.pop(-1)
        result += str(total % 2)
        memory = total // 2
    return result[::-1]


if __name__ == '__main__':
    print(binary_sum(input(), input()))
