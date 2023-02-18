def linear_prime_search(number: int) -> list[int]:
    """
    Линейный поиск всех простых чисел до заданного значения.\n
    Сложность O(n).
    """
    lp = [0] * (number + 1)
    primes = []
    for i in range(2, number + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > number):
                break
            lp[x] = p
    return primes


if __name__ == '__main__':
    print(linear_prime_search(int(input())))
