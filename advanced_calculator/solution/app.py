def eval(expression):
    result = 0
    while len(expression) != 0:
        isPositive = True
        if expression[0] == " ":
            expression = expression[1: len(expression)]
        if expression[0] == "+":
            expression = expression[2: len(expression)]
        elif expression[0] == "-":
            isPositive = False
            expression = expression[2: len(expression)]

        if expression[0] == "(":
            bracket = eval(expression[1: len(expression)])
            expression = expression[expression.index(")"): len(expression)]
            if isPositive:
                result += bracket
            else:
                result -= bracket
        elif expression[0] == ")":
            return result
        else:
            if isPositive:
                result += int(expression[0])
            else:
                result -= int(expression[0])
            expression = expression[2: len(expression)]
    return result


print(eval('- (3 + ( 2 - 1 ) )'))
# -4