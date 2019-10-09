operators = ['+', '-', '*', '/', '^']
validChars = ['.', '|', '(',')']
functions = ["sin", "cos", "tan", "sqrt", "asin", "acos", "atan"]


def parse(e):
    outputQueue = []
    operatorStack = []

    expressions = e.split('=')

    iterations = 0

    for exp in expressions:
        for char in exp:
            if char.isnumeric():  # if token is a number...
                outputQueue.append(char)  # push to output queue
            else:
                if iterations + 3 < len(exp) - 1:
                    if contains(exp[iterations:iterations + 3], functions):
                        print("Work In progress...")

        iterations += 1




def contains(a, b):
    res = 0
    i = 0
    for char in a:
        if char in b:
            res +=1
        i += 1

    if res > 0:
        return True
    else:
        return False


def replace(a, b, c):
    res = ''
    i = 0
    for char in a:
        if char in b:
            res += c
        else:
            res += a[i]

        i += 1

    return res





#TESTING
equation = input("Enter Equation\n")

parse(equation)

# parse(equation)
