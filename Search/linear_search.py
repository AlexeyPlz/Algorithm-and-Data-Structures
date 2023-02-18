def linear_search(data: list[int], number: int) -> int | None:
    """
    Линейный поиск в массиве данных с возвратом индекса.\n
    Сложность O(n).
    """
    for index in range(len(data)):
        if data[index] == number:
            return index
    return None


if __name__ == '__main__':
    print(linear_search(list(map(int, input().split())), int(input())))
