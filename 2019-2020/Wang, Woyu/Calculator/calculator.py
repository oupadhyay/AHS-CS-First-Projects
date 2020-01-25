# Woyu Wang and Iniyan Joseph
# Great work!
# Score: 9/10
# + 7 for completion of task
# + 2 for an extensive list of functions and the trig functions...
# Potential Improvments:
# Find a way to make parentheses work to force Order of Operations 
# Make it easier to have multiple functions with the symbols (+) rather than "sum"
# ~ Ojasw Upadhyay 

import math

# !IMPORTANT NOTICE!
# Do not use +, -, *, /, %, or ^
# Use add, sub, mul, div, mod, or pow respectively
# For example: '5 add 3' will result in '8.0'
# Order of operations is adhered to
# Enjoy!

# Acceptable operations
opers = ['floor','ceil','abs','!','sin','cos','tan','cubert', 'sqrt', 'pow', 'mul', 'div', 'mod', 'add', 'sub']
# Characters in valid numbers
numValid = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-']
# Main code
while True:
  # Get input and format
  io = input("> ")
  io = io.replace(' ','')
  # Iterate through operation array (order of operations)
  for i in range(0, len(opers)):
    # Iterate through io
    j = 0
    while j < len(io):
      if(not(io[j] in numValid)):
        # Operation
        o = j
        while(o < len(io) and not(io[o] in numValid)): o += 1
        operation = io[j:o]
        # Number a
        a = j - 1
        while(a >= 0 and io[a] in numValid): a -= 1
        try: numA = float(io[a+1:j])
        except ValueError: pass
        # Number b
        b = o + 1
        while(b < len(io) and io[b] in numValid): b += 1
        try: numB = float(io[o:b])
        except ValueError: pass
        # Execute operation
        if(operation == opers[i] and operation == 'floor'):
          j = 0
          res = math.floor(numB)
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'ceil'):
          j = 0
          res = math.ceil(numB)
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'abs'):
          j = 0
          res = abs(numB)
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == '!'):
          j = 0
          res = math.factorial(numA)
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'sin'):
          j = 0
          res = math.sin(numB)
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'cos'):
          j = 0
          res = math.cos(numB)
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'tan'):
          j = 0
          res = math.tan(numB)
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'cubert'):
          j = 0
          res = numB ** (1. / 3)
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'sqrt'):
          j = 0
          res = numB ** (1. / 2)
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'pow'):
          j = 0
          res = numA ** numB
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'mul'):
          j = 0
          res = numA * numB
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'div'):
          j = 0
          res = numA / numB
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'mod'):
          j = 0
          res = numA % numB
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'add'):
          j = 0
          res = numA + numB
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
        if(operation == opers[i] and operation == 'sub'):
          j = 0
          res = numA - numB
          io = io.replace(io[a+1:b], str(res), 1)
          print(io)
      j += 1

