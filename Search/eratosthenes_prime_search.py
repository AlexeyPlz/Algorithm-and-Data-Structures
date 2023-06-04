def eratosthenes_prime_search(number: int) -> list[int | bool]:
    """
    Поиск всех простых чисел до заданного значения через решето Эратосфена.\n
    Сложность O(n*log(log n)).
    """
    numbers = list(range(number + 1))
    numbers[0] = numbers[1] = False
    for i in range(2, number):
        if numbers[i]:
            for j in range(2 * i, number + 1, i):
                numbers[j] = False
    return numbers


if __name__ == '__main__':
    print(eratosthenes_prime_search(int(input())))
