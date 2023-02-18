def binary_search(data: list[int], number: int) -> int | None:
    """
    Бинарный поиск в отсортированном массиве данных с возвратом индекса.\n
    Сложность O(log n).
    """
    left, right = 0, len(data) - 1
    while left <= right:
        index = (left + right) // 2
        middle = data[index]
        if number > middle:
            left = index + 1
        elif number < middle:
            right = index - 1
        else:
            return index
    return None


if __name__ == '__main__':
    print(binary_search(list(map(int, input().split())), int(input())))
