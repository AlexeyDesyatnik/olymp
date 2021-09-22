# Оптимизированное решение, алгоритм адаптирован из
# https://github.com/davepl/Primes/tree/drag-race/PrimePython/solution_2
# Всё ещё не проходит по времени, но существенно лучше простого решения

from math import sqrt

LIMIT = 16_000_000
bits = bytearray(b"\x01") * ((LIMIT + 1) // 2)

factor = 1
q = sqrt(LIMIT) / 2
bitslen = len(bits)

while factor <= q:
    factor = bits.index(b"\x01", factor)
    start = 2 * factor * (factor + 1)
    step = factor * 2 + 1
    size = bitslen - start
    bits[start::step] = b"\x00" * (size // step + bool(size % step))

    factor += 1

K = int(input())
prime_count = 1
prime = 2
n = 1
while n > 0:
    if prime_count == K:
        print(prime)
        break
    prime = n * 2 + 1
    prime_count += 1
    n = bits.find(1, n + 1)
