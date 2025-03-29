/**
 * Description: Returns all prime factors of a number by using precomputed primes.
 * Time: $O(\sqrt{MAX} \log \log \sqrt{MAX})$ for computing the necessary primes and $O(\log N)$ per query.
 * Status: Tested
 */
#pragma once
#include <math.h>
#include "./eratosthenes.h"

int safe_sqrt(int x)
{
    int sq = max((int)(sqrt(x) - 1), 0);
    while (sq * sq < x)
    {
        sq++;
    }
    return sq;
}

const int MAX = 1e7;
vector<int> primes = eratosthenes(safe_sqrt(MAX));

vector<int> factorization(int n)
{
    vector<int> factors;
    for (auto &p : primes)
    {
        if (p * p > n)
        {
            break;
        }
        while (n % p == 0)
        {
            factors.push_back(p);
            n /= p;
        }
    }
    if (n > 1)
    {
        factors.push_back(n);
    }
    return factors;
}