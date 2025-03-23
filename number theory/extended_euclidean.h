/**
 * Description: Finds two integers $x$ and $y$ that solve $ax+by=\gcd(a,b)$
 * Time: $O(\log max(a,b))$
 * Status: Tested
 */
#pragma once

int extended_euclidean(int a, int b, int &x, int &y) {
  if (b == 0) {
    x = 1;
    y = 0;
    return a;
  }
  int x1,y1;
  int gcd = extended_euclidean(b,a%b,x1,y1);
  x = y1;
  y = x1 - y1*(a/b);
  return gcd;
}