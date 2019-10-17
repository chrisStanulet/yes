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


# This helped me understand what was happening: https://rosettacode.org/wiki/Parsing/Shunting-yard_algorithm#Python
# since Wikipedia's pseudocode was written horribly.


def tokenizeInput(input):
    inp = input
    tokList = []
    i = 0
    for token in inp:
        if token in operators:
            tokList.append((token, operators[token]))
        elif token.isalpha() and token not in operators:  # IF TOKEN IS A VARIABLE
            if i > 1 and inp[
                i - 1] not in operators:  # IF PREVIOUS TOKEN IS NOT AN OPERATOR, INSERT ASTERISK AND THEN INSERT VARIABLE
                tokList.append(('*', operators['*']))
                tokList.append(('NUMBER', token))
            else:
                tokList.append(('NUMBER', token))
        else:
            tokList.append(('NUMBER', token))
        i += 1
        print(tokList)
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













print(shuntingYardAlgorithm('3+4*2/(1-5)^2^3'))








