# Переход от прямолинейного решения к оптимизированному
# 1. Исходное прямолинейное решение:
# 4.4 сек на заполнение решета
# 2. Использование множителей только до кв.корня из верхнего предела:
# 1.7 сек на заполнение
# 3. Рассмотрение только нечётных элементов решета:
# 1.4 сек
# 4. Заполнение только по нечётным производным элементам (3p, 5p и т.д.):
# 0.8 сек
# 5. Хранение значений решета только для нечётных чисел:
# 1.3 сек (антиоптимизация по времени, зато оптимизация по памяти в 2 раза)
# 5-я оптимизация требует 4-ю для корректной работы
# 6. Заполнение решета через срезы
# 0.5 сек на заполнение

import math
from time import time

LIMIT = 15_500_000
SIEVE_SIZE = LIMIT + 1
sieve = [True] * SIEVE_SIZE

def MakeSieve():
    for p in range(3, int(math.sqrt(SIEVE_SIZE) + 1), 2):
        if not sieve[p // 2]:
            continue
        start = (3 * p) // 2
        step = p
        amount = math.ceil((SIEVE_SIZE - start) / step)
        sieve[start :: step] = [False] * amount

# Проверка: простые числа меньше 100
primes_under_50 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def GetPrimes(upper_boundary=50):
    yield 2
    for p in range(3, upper_boundary, 2):
        if sieve[p // 2]:
            yield p

t1 = time()
MakeSieve()
t2 = time()
print(t2 - t1)
primes = list(GetPrimes())
print(primes)
print("CORRECT" if primes == primes_under_50 else "ERROR")
