using System;
using System.Collections;
using static System.Math;

namespace informatics_973_csharp
{
    class Informatics_973
    {
        const int LIMIT = 15485864;
        const int SIEVE_SIZE = LIMIT / 2 + 1;

        static BitArray sieve = new BitArray(SIEVE_SIZE);

        static void MakeSieve() {
            sieve.SetAll(true);
            int stop = (int)(Sqrt(LIMIT) + 1);
            for (int p = 3; p <= stop; p += 2) {
                if (!sieve[p / 2]) continue;
                for (int n = 3 * p; n <= LIMIT; n += 2 * p) {
                    sieve[n / 2] = false;
                }
            }
        }

        static int GetNthPrime(int n) {
            if (n == 1) return 2;
            int primeCount = 1;
            for (int p = 3; p < LIMIT; p += 2) {
                if (sieve[p / 2]) {
                    primeCount += 1;
                    if (primeCount == n) return p;
                }
            }
            return -1; // nth prime beyond limit, shouldn't happen
        }
        static void Main(string[] args)
        {
            int k = int.Parse(Console.ReadLine());
            MakeSieve();
            int p = GetNthPrime(k);
            Console.WriteLine(p);
        }
    }
}
