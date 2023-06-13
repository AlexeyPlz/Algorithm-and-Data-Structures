def selection_sorting(data: list[int]) -> list[int]:
    """
    Сортировка выбором.\n
    Сложность O(n**2).
    """
    for i in range(len(data)-1):
        min_index = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


if __name__ == '__main__':
    print(selection_sorting(list(map(int, input().split()))))
