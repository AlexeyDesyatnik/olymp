package informatics_973.informatics_973_java;

import java.util.Arrays;
import java.util.Scanner;

public class Informatics_973 {
    static final int LIMIT = 15_500_000;
    static final int SIEVE_SIZE = LIMIT / 2 + 1;
    static boolean[] sieve = new boolean[SIEVE_SIZE];

    private static void MakeSieve() {
        Arrays.fill(sieve, true);
        int stop = (int) (Math.sqrt(LIMIT) + 1);
        for (int p = 3; p < stop; p += 2) {
            if (!sieve[p / 2]) continue;
            for (int n = p * p; n < LIMIT; n += p * 2) {
                sieve[n / 2] = false;
            }
        }
    }

    private static int GetNthPrime(int n) {
        if (n == 1) return 2;
        int primeCount = 1;
        for (int p = 3; p < LIMIT; p += 2) {
            if (sieve[p / 2]) {
                primeCount++;
                if (primeCount == n) return p;
            }
        }
        return -1; // nth prime beyond limit, shouldn't happen
    }
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int k = sc.nextInt();
        MakeSieve();
        int p = GetNthPrime(k);
        System.out.println(p);
    }
}