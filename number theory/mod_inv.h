/**
 * Description: Computes $a^{-1} \mod m$. where $a^{-1}$ represents a number such that $a*a^{-1} \equiv 1 \mod m$
 * Time: $O(\log (\max{(a,b)}))$
 * Status: Tested
 */

#pragma once

#include "./extended_euclidean.h"

int mod_inv(int a, int m) {
  int x,y;
  int gcd = extended_euclidean(a,m,x,y);
  if (gcd != 1) return -1;
  else return (x % m + m) % m;
}