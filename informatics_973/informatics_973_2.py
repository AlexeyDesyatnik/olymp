# Переход от прямолинейного решения к оптимизированному

LIMIT = 1000
SIEVE_SIZE = LIMIT + 1
sieve = [True] * SIEVE_SIZE


def MakeSieve():
    for p in range(2, SIEVE_SIZE):
        if (not sieve[p]):
            continue
        for m in range(p + p, SIEVE_SIZE, p):
            sieve[m] = False


# Проверка: простые числа меньше 100
primes_under_50 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def GetPrimes(upper_boundary=50):
    for p in range(2, upper_boundary):
        if sieve[p]:
            yield p


MakeSieve()
primes = list(GetPrimes())
print(primes)
print("CORRECT" if primes == primes_under_50 else "ERROR")
