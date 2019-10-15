from collections import namedtuple

LPAREN, RPAREN = '(',')'

OpProp = namedtuple('OpProp','precedence association')

operators = {
    '^':OpProp(3,'r'),
    '*':OpProp(2,'l'),
    '/':OpProp(2,'l'),
    '+':OpProp(1,'l'),
    '-':OpProp(1,'l'),
    '(':OpProp(9,'l'),
    ')':OpProp(0,'l'),

}


# This helped me understand what was happening: https://rosettacode.org/wiki/Parsing/Shunting-yard_algorithm#Python
# since Wikipedia's pseudocode was written badly.


def shuntingYardAlgorithm(input):

    out, stack = [], []

    for token in input:
        if token.isnumeric():
            out.append(token)
        elif token in operators:
            if stack:
                (tokenPrec, tokenAcc) = operators[token]
                if len(stack) > 0:  (stackPrec, tokenPrec) = operators[stack[-1]]
                if token is not LPAREN or RPAREN:
                    if stackPrec > tokenPrec:
                        out.append(stack.pop())
                    elif stackPrec <=  tokenPrec:
                        out.append(token)
                else:
                    if token is LPAREN:
                        stack.append(token)
                    elif token is RPAREN:
                        while stack and stack[-1] is not LPAREN:
                            out.append(stack.pop())
                        if stack and stack[-1] is LPAREN:
                            stack.pop()
    while stack:
        out.append(stack.pop())
    return out;






print(shuntingYardAlgorithm('3+4*2/(1-5)^2^3'))








