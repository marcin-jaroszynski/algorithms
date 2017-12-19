"""
Hacker Rank challenge: https://www.hackerrank.com/challenges/counter-game/problem
"""

def isPowerOf2(n):
  return (not(n & (n - 1)))

def getGreatestPowerOf2(n):
  number = n - 1;
  currentPowerOf2 = 2;
  while (number >= currentPowerOf2 * 2):
    currentPowerOf2 = currentPowerOf2 * 2;
  return currentPowerOf2

def whoWin(number):
  isPlayerLouise = True
  while (number != 1): 
    if (not isPowerOf2(number)):
      number = number - getGreatestPowerOf2(number)
    else:
      number = number - int(number / 2)

    if (number == 1):
      if (isPlayerLouise):
        print('Louise')
      else:
        print('Richard')

    isPlayerLouise = not isPlayerLouise

testCases = 0
testCases = int(input().strip());
if (testCases < 1):
  testCases = 1;
if (testCases > 10):
  testCases = 10;
for i in range(testCases):
  number = int(input().strip())
  whoWin(number);