#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

const int LIMIT = 15500000;
const int SIEVE_SIZE = LIMIT / 2 + 1;
vector<bool> sieve(SIEVE_SIZE, 1);

void makeSieve() {
    int stop = (int) sqrt(LIMIT) + 1;
    for (int p = 3; p < stop; p += 2) {
        if (!sieve[p / 2]) continue;
        for (int n = p * p; n < LIMIT; n += p * 2) {
            sieve[n / 2] = false;
        }
    }
}

int getNthPrime(int n) {
    if (n == 1) return 2;
    int primeCount = 1;
    for (int p = 3; p < LIMIT; p += 2) {
        if (sieve[p / 2]) {
            primeCount++;
            if (primeCount == n) return p;
        }
    }
    return -1; // shouldn't happen
}

int main()
{
    makeSieve();
    int K;
    cin >> K;
    int p = getNthPrime(K);
    cout << p << endl;
}
