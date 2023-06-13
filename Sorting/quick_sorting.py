def quick_sorting(data: list[int]) -> list[int]:
    """
    Быстрая сортировка.\n
    Сложность O(n*log n).
    """
    if len(data) < 2:
        return data
    pivot = data[0]
    return quick_sorting([i for i in data[1:] if i < pivot]) + [pivot] + quick_sorting([i for i in data[1:] if i > pivot])  # noqa


if __name__ == '__main__':
    print(quick_sorting(list(map(int, input().split()))))
