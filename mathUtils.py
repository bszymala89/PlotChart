def isValidEquasion(equasion):
    allowedChars = "x0123456789+-*/ "
    correctCharCount = 0
    hasNumber = False
    for i in equasion:
        for j in allowedChars:
            if j == i.lower():
                if i.isdigit() or i.lower() == "x":
                    hasNumber = True
                correctCharCount += 1
                break

    if correctCharCount == len(equasion) and hasNumber:
        return True
    else:
        return False

def calculateEquasion(equasion, x):
    if isValidEquasion(equasion):
        equasion = equasion.lower().replace(" ", "")
        result = eval(equasion)
        print(result)
        return result
    else:
        print("wrong equasion") 