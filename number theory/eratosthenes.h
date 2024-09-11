/**
 * Description: Returns all prime numbers in range [1,n].
 * Time: $O(N \log \log n)$ 
 * Status: Tested
 */
#pragma once

const int MAX = 1e6; //can handle larger values if needed

vector<int> eratosthenes (int n) {
  bitset<MAX> is_prime;
  is_prime.set();
  is_prime[0] = is_prime[1] = 0;

  vector<int> primes;
  for (int i = 2; i <= n; ++i) {
    if (is_prime[i]) {
      primes.push_back(i);
      for (int j = i; j <= n; j += i) {
        is_prime[j] = 0;
      }
    }
  }
  return primes;
}