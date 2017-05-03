from stack import Stack

def rpn(expression):
  operatorPriority = {}
  operatorPriority['('] = 0;
  operatorPriority['+'] = 1;
  operatorPriority['-'] = 1;
  operatorPriority['/'] = 2;
  operatorPriority['*'] = 2;


  i = 0;
  output = ''
  stack = Stack()
  while(len(expression) > i):
    sign = expression[i]
    isOperator = (sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == '(' or sign == ')')
    if (not isOperator):
      output += sign
    else:
      if (sign == '('):
        stack.push(sign)
      elif (sign == ')'):
        while (stack.peek() != '('):
          output += stack.pop()
        stack.pop()
      else:
        if (not stack.isEmpty() and operatorPriority[stack.peek()] >= operatorPriority[sign]):
          output += stack.pop()
        stack.push(sign)

    i += 1 

  while (not stack.isEmpty()):
    output += stack.pop()

  print(output) 


print('Enter expression(e.g.: 3 + 2 * 5):')
expression = input()

rpn(expression) 


