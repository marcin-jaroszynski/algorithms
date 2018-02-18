def isPrimeNumber(number):
  if (2 > number):
    return False
  for i in range(2, number-1):
    if (number % i == 0):
      return False 
  return True


def isEvenPerfectNumber(number):
  index = 0
  total = 0
  perfectNumber = 0
  while (number > perfectNumber):
    total += pow(2, index)
    if (isPrimeNumber(total)):
      perfectNumber = total * pow(2, index)
    index += 1
  if (number == perfectNumber and number != 0):
    return True
  return False
 
print('Enter number: ')
number = int(input()) 
 
if (isEvenPerfectNumber(number)):
  print('Number: '+ str(number) + ' is even perfect number!')
else:
   print('Number: '+ str(number) + ' is not even perfect number!')