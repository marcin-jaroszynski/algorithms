def pascal_triangle(maxRows):
  currentRow = 1
  a = [1];

  while(maxRows >= currentRow):
    spaces = maxRows - currentRow;
    currentString = ''
    for j in range(spaces):
      currentString += " "

    for j in range(len(a)): 
      currentString += str(a[j]) + " "
 
    print(currentString)
 
    tmp = [1]
    for j in range(1, currentRow):
      tmp.append(a[j - 1] + a[j])

    tmp.append(1)
    a = tmp
    currentRow+=1

pascal_triangle(5)