import math
print("Keshav's calculator!")

def mainfunction():
  operator = input('''
  Enter  + for a sum
  Enter  - for a difference 
  Enter  x for multiplying
  Enter  / for division
  Enter % for modulus
  Enter g for the greatest common demonimator between your 2 inputs
  Enter ^ for to raise your first input to the 2nd input power)

  ''')
  inputa = int(input('What is your first number?'))
  inputb = int(input('What is your seccond number?'))
  if operator == '/':
    print('{} / {} = '.format(inputa, inputb))
    print(inputa / inputb)
  if operator == 'x':
    print('{} * {} = '.format(inputa, inputb))
    print(inputa * inputb)
  if operator == '-':
    print('{} / {} = '.format(inputa, inputb))
    print(inputa / inputb)
  if operator == '+':
    print('{} + {} = '.format(inputa, inputb))
    print(inputa + inputb)
  if operator == '%':
    print('{} mod {} = '.format(inputa, inputb))
    print(inputa % inputb)
  if operator == 'g':
    print ("The gcd of your inputs is: ", end="") 
    print (math.gcd(inputa,inputb)) 
  if operator == '^':
    print('{} ^ {} = '.format(inputa, inputb))

    print(pow(inputa,inputb))
  else:
    print('The operation you want is invalid run the program again!')


mainfunction()




def repeat():
  r = input('''
  Do you want do do another calculation?
  Type y or n.

  
  ''')
  if r.upper() == "Y":
    mainfunction()
  elif r.upper() == "N":
    print('Bai!')
  else:
    repeat()

repeat()










