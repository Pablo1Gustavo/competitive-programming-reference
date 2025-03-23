/**
 * Description: Returns all prime numbers in range [1,n].
 * Time: $O(N \log \log n)$
 * Status: Tested
 */
#pragma once
#include <vector>
#include <bitset>
using namespace std;

const int MAX = 1e7;

vector<int> eratosthenes(int n)
{
    bitset<MAX> is_prime;
    is_prime.set();
    is_prime[0] = is_prime[1] = false;

    vector<int> primes;
    for (int i = 2; i <= n; ++i)
    {
        if (is_prime[i])
        {
            primes.push_back(i);
            for (int j = i; j <= n; j += i)
            {
                is_prime[j] = false;
            }
        }
    }
    return primes;
}