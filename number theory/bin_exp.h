/*
* Description: Computes a^n \mod m
* Time: $O(\log n)$
* Status: Tested
*/
#pragma once

int bin_exp(int a, int n, int m) {
  a %= m;
  int res = 1;
  while(n) {
    if(n&1) res = res * a % m;
    a = a * a % m;
    n >>= 1;
  }
  return res;
}