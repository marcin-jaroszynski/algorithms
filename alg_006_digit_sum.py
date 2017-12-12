"""
Calculate digit sum for specific number
"""

def digit_sum(number):
  result = 0
  x = number
  while (x != 0):
    result += x % 10
    x = int(x / 10)
  return result

print('Enter some number: ')
number = int(input())
print('Digit sum for number: ' + str(number) + ' is: ' + str(digit_sum(number)))  