def isValidEquation(equation):
    allowedChars = "x0123456789+-*/ "
    correctCharCount = 0
    hasNumber = False
    for i in equation:
        for j in allowedChars:
            if j == i.lower():
                if i.isdigit() or i.lower() == "x":
                    hasNumber = True
                correctCharCount += 1
                break

    if correctCharCount == len(equation) and hasNumber:
        return True
    else:
        return False

def calculateEquation(equation, x):
    if isValidEquation(equation):
        equation = equation.lower().replace(" ", "")
        result = eval(equation)
        print(result)
        return result
    else:
        print("wrong equation") 