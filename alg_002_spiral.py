def spiral(a, m, n):
  RIGHT = 1
  DOWN = 2
  LEFT = 3
  UP = 4
  maxRows = m * n
  n -= 1
  m -= 1
  i = 0
  j = 0
  maxM = m
  maxN = n
  leftMargin = 0
  topMargin = 0
  direction = RIGHT
  counter = 0
  output = '';

  while (counter < maxRows):
    output += str(a[i][j]) + ' '
    if (direction == RIGHT):
      j += 1
      if (j == maxN):
        direction = DOWN
    elif (direction == DOWN):
      i += 1
      if (i == maxM):
        direction = LEFT
    elif (direction == LEFT):
      j -= 1
      if (j == leftMargin):
        direction = UP
        topMargin += 1
        leftMargin += 1
    elif (direction == UP):
      i -= 1
      if (i == topMargin):
        direction = RIGHT
        maxM -= 1
        maxN -= 1

    counter += 1

  print output

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
  ]

spiral(matrix, 5, 5)