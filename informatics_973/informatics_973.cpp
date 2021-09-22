#include <iostream>
#include <vector>
using namespace std;
int main()
{
    const int SIEVE_SIZE = 15800000;
    vector<bool> sieve(SIEVE_SIZE, 1);
    int K;
    cin >> K;
    int count = 0;
    int i;
    for (i = 2; count < K; i++)
    {
        if (!sieve[i])
            continue;
        count++;
        //cout << i << endl;
        for (int j = i + i; j < SIEVE_SIZE; j += i)
            sieve[j] = false;
    }
    cout << (i - 1) << endl;
}
