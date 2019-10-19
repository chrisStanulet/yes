def parse(x):
    x = x.replace(" ", "")
    operators = set('+-*/()')
    numbers = set("123456789")
    op_out = []  # This holds the operators that are found in the string (left to right)
    num_out = []  # this holds the non-operators that are found in the string (left to right)
    waste = []

    for c in x:  # examine 1 character at a time
        if c in operators:
            op_out.append(c)
            num_out.append("")#append space to show where an operator should be in an equation. Makes it easier if beginning number is negative. Or +(-x)
        elif c in numbers:
            num_out.append(c)
        else:
            # not an operator or number. Useless trash.
            waste.append(c)
    return num_out, op_out


print(parse('-3/2*15'))

