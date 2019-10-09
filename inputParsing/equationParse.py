operators = ['+', '-', '*', '/', '^']
validChars = ['.', '|', '(', ')']
functions = ["sin", "cos", "tan", "sqrt", "asin", "acos", "atan"]


# Example: 16-2x=5x+9
def parse(e):
    outputQueue = []
    operatorStack = []

    expressions = e.split('=')

    iterations = 0

    for exp in expressions:
        for char in exp:
            if char.isnumeric():  # if token is a number...
                outputQueue.append(char)  # push to output queue
            else:  # if token is not a number

                # if token is a function
                if iterations + 3 < len(exp) - 1 and contains(exp[iterations:iterations + 3], functions):
                    operatorStack.append(exp[iterations:iterations + 3])
                elif iterations + 4 < len(exp) - 1 and contains(exp[iterations:iterations + 4], functions):
                    operatorStack.append(exp[iterations:iterations + 4])

                # if token is an operator
                if contains(char, operators):
                    '''while ((there is a function at the top of the operator stack)
               or (there is an operator at the top of the operator stack with greater precedence)
               or (the operator at the top of the operator stack has equal precedence and is left associative))
              and (the operator at the top of the operator stack is not a left parenthesis):
            pop operators from the operator stack onto the output queue.
        push it onto the operator stack.'''

        iterations += 1


def contains(a, b):
    res = 0
    i = 0
    for char in a:
        if char in b:
            res += 1
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


# TESTING
equation = input("Enter Equation\n")

parse(equation)

# parse(equation)
