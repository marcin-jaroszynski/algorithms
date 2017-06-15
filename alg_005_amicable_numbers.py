"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

URL: https://projecteuler.net/problem=21
"""
import math

def d(n):
  totalSum = 1;
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      totalSum += i;
      totalSum += n//i;
  return totalSum

totalSum = 0
for i in range(1, 10000):
  a = i
  b = d(a)
  if (b > a):
    if (d(b) == a and a != b):
      totalSum = totalSum + a+ b;

print(totalSum)
