# Geoffrey Tang
def add(pos):
    temp = float(operation[pos - 1]) + float(operation[pos + 1])
    operation.pop(pos - 1)
    operation.pop(pos)
    operation[pos - 1] = str(temp)


def subtract(pos):
    temp = float(operation[pos - 1]) - float(operation[pos + 1])
    operation.pop(pos - 1)
    operation.pop(pos)
    operation[pos - 1] = str(temp)


def multiply(pos):
    temp = float(operation[pos - 1]) * float(operation[pos + 1])
    operation.pop(pos - 1)
    operation.pop(pos)
    operation[pos - 1] = str(temp)


def divide(pos):
    temp = float(operation[pos - 1]) / float(operation[pos + 1])
    operation.pop(pos - 1)
    operation.pop(pos)
    operation[pos - 1] = str(temp)


def mod(pos):
    temp = float(operation[pos - 1]) % float(operation[pos + 1])
    operation.pop(pos - 1)
    operation.pop(pos)
    operation[pos - 1] = str(temp)


def exponent(pos):
    temp = float(operation[pos - 1]) ** float(operation[pos + 1])
    operation.pop(pos - 1)
    operation.pop(pos)
    operation[pos - 1] = str(temp)


previous = 0
print('Input format = (number) (operation) (number) (operation) ...')
print('e.g. 5 + 8 - 2')
print('Available operations: +, -, /, *, %, *, P, ! (previous answer')
print('-' * 10)
while True:
    n = list(input())
    operation = ['']
    pos = 0
    for i in n:
        if str.isnumeric(i) or i == '.':
            operation[pos] += i
        elif i == 'P':
            operation[pos] = previous
        elif i == '+' or i == '-' or i == '/' or i == '*' or i == '%' or i == '^':
            operation.append('')
            pos += 1
            operation[pos] += i
            operation.append('')
            pos += 1
    yes = True  # repeated multiple times to account for PEMDAS
    while yes:
        yes = False
        for i in range(len(operation)):
            if operation[i] == '^':
                exponent(i)
                yes = True
                break
    yes = True
    while yes:
        yes = False
        for i in range(len(operation)):
            if operation[i] == '%':
                mod(i)
                yes = True
                break
    yes = True
    while yes:
        yes = False
        for i in range(len(operation)):
            if operation[i] == '*':
                multiply(i)
                yes = True
                break
    yes = True
    while yes:
        yes = False
        for i in range(len(operation)):
            if operation[i] == '/':
                divide(i)
                yes = True
                break
    yes = True
    while yes:
        yes = False
        for i in range(len(operation)):
            if operation[i] == '+':
                add(i)
                yes = True
                break
    yes = True
    while yes:
        yes = False
        for i in range(len(operation)):
            if operation[i] == '-':
                subtract(i)
                yes = True
                break
    print(operation[0])
    previous = operation[0]
    print('-' * 10)

