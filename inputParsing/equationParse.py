from collections import namedtuple

OpProp = namedtuple('OpProp','precedence association')

operators = {
    '^': OpProp(4, 'r'),
    '*': OpProp(3, 'l'),
    '/': OpProp(3, 'l'),
    '+': OpProp(2, 'l'),
    '-': OpProp(2, 'l'),
    '(':OpProp(9,'l'),
    ')':OpProp(0,'l'),

}


# Algorithm was created with help from https://rosettacode.org/wiki/Parsing/Shunting-yard_algorithm#Python
# WRITTEN BY ANGELO DELUCA

# Planned modifications:
# - Add trig function parsing capability

def tokenizeInput(input):
    inp = splitArr(input)
    tokList = []
    i = 0
    for token in inp:
        if token in operators:
            tokList.append((token, operators[token]))
        elif token.isalpha() and token not in operators:  # IF TOKEN IS A VARIABLE
            if i > 0 and inp[
                i - 1] not in operators:  # IF PREVIOUS TOKEN IS NOT AN OPERATOR, INSERT ASTERISK AND THEN INSERT VARIABLE
                tokList.append(('*', operators['*']))
                tokList.append(('NUMBER', token))
            else:
                tokList.append(('NUMBER', token))
        else:
            tokList.append(('NUMBER', token))
        i += 1
    return tokList;


def shuntingYardAlgorithm(input):
    input = tokenizeInput(input)
    out, stack = [], []
    for token, value in input:

        if token is 'NUMBER':
            out.append(value)
        else:
            ctok, (ctp, cta) = token, value

            while stack:
                stok, (stp, sta) = stack[-1]

                if (cta == 'l' and ctp <= stp) or (cta == 'r' and ctp < stp):

                    if ctok is not ')':
                        if stok is not '(':
                            out.append(stack.pop())
                        else:
                            break
                    else:
                        if stok is not '(':
                            out.append(stack.pop())
                        else:
                            stack.pop()
                            break
                else:
                    break

            if ctok is not ')':
                stack.append((token, value))

    while stack:
        out.append(stack.pop())

    return out

def rpnToString(exp):

    output = ''
    x = ''
    for token in exp:
        if type(token) == tuple:
            output += x + str(token[0])
        else:
            output += x + token
        x = ' '
    return output;


def splitArr(input):
    out = []
    num = ''
    for char in input:
        if (not char.isnumeric()) and (char is not '.'):
            if num is not '':
                out.append(num)
                num = ''
            out.append(char)
        else:
            num = num + char

    if num: out.append(num)
    return out
