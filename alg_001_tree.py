def drawTree(rows):
  currentRow = 1
  while (rows >= currentRow):
    spaces = rows - currentRow
    currentString = "";
    for i in range(spaces):
      currentString += " "
    for j in range(2*currentRow-1):
      if j % 2 == 0:
        currentString += "*"
      else:
        currentString += " "
    print(currentString)
    currentRow += 1

drawTree(7)