operators = ['+', '-', '*', '/', '^']
validChars = ['.', '|', '(', ')']
functions = ["sin", "cos", "tan", "sqrt", "asin", "acos", "atan"]



# Example: 16-2x=5x+9
outputQueue = []
operatorStack = []
precedence = {'(':1,'^':2,'m':3,'/':4,'+':5,'-':6}
def parse(e):

    expressions = e.split('=')

    iterations = 0

    for exp in expressions:
        for char in exp:

            #If the character is numeric, push to output queue.
            if char.isnumeric():
                outputQueue.append(char)
                exp.pop(iterations)

            #If the character is an operator...
            if char in operators:

                #While there is an operator on top of the operator stack, there is an operator at the top of the operator stack with greater precedence, or the operator at the top of the operator stack has equal precedence and is left associative
                while (len(operatorStack) > 0 or hasGreaterPrecedence(char, operatorStack(len(operatorStack)-1)) == 1 or (hasGreaterPrecedence(char, operatorStack(len(operatorStack)-1)) == 0 and operatorStack(len(operatorStack)-1) == '{')) and operatorStack(len(operatorStack)-1) != '(':

                    outputQueue.append(operatorStack.pop(len(operatorStack)-1))

                operatorStack.append(char)
                exp.pop(iterations)

            if char == '(':
                operatorStack.append('(')
                exp.pop(iterations)

            if char == ')':
                while operatorStack(len(operatorStack)-1) != '(':
                    outputQueue.append(operatorStack.pop(len(operatorStack)-1))

                if operatorStack(len(operatorStack)-1) == ')':
                    operatorStack.pop(len(operatorStack)-1)

            iterations += 1

        if operatorStack is not None:






def popAll(a, popToA):
    i = 0
    for char in popToA:
        a.append(a.ppend)

        i+=1



def hasGreaterPrecedence(a,b):

    if precedence[a] > precedence[b]:
        return 1
    else:
        return -1




def isFunctionOnTop():

    for funct in functions:
        if operatorStack[len(operatorStack)-1] in funct:
            return True
        else:
            return False



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
