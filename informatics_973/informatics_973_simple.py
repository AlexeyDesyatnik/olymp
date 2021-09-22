# Прямолинейное решение, не пройдёт по времени (и скорее всего по памяти)

def GetNthPrime(n, upper_limit=16_000_000):
    sieve = [True] * upper_limit
    prime_count = 0
    last_prime = 0
    for p in range(2, upper_limit):
        if (not sieve[p]):
            continue
        last_prime = p
        prime_count += 1
        if prime_count == n:
            return last_prime
        for m in range(p + p, upper_limit, p):
            sieve[m] = False

n = int(input())
p = GetNthPrime(n)
print(p)