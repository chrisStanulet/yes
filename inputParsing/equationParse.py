operators = ['+', '-', '*', '/', '^']
validChars = ['.', '|', '(',')']



def parse(e):
    result = ''
    # Split solve
    e = e.replace(' ','')
    e = e.split('=')
    if len(e) != 2:
        return 'ERR_2EQUAL'

    eqobj = [{}]

    #Simplify
    # Example: 16-2x=5x+9
    start = 0
    stop = 0
    i = 0
    expPart = 0
    for exp in e:
        for c in exp:
            if contains(c,operators): # If current char is an operator (Means that we have either found a new value, or the value is at the beginning, and is negative
                if i > 0: # Add value to equation object when not at first pause.
                    e = {'val':exp[start:stop]}
                    eqobj.append(e.copy())
                    if exp[i-1].isalpha(): # if character before operator is not a number (e.g. a variable,) bind variable to value.
                        eqobj[len(eqobj)-1]['multBy'] = exp[i-1]
                start = i
            else:
                stop = i+1
            i +=1
    expPart+=1

    print(expPart)




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
