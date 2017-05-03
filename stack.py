class Stack(object):
  def __init__(self):
    self.current = 0
    self.data = []

  def push(self, value):
    self.data.append(value)
    self.current += 1

  def pop(self):
    if self.current > 0:
      value = self.data.pop(self.current-1)
      self.current -= 1
      return value
    else:
      return ''

  def isEmpty(self):
    return (len(self.data) == 0)

  def peek(self):
    if self.isEmpty() != True:
      return self.data[self.current-1]

  def clear(self):
    self.data = []

  def length(self):
    return len(self.data)