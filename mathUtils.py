def is_valid_equation(equation):
    allowed_chars = "x0123456789+-*/ "
    correct_char_count = 0
    has_number = False
    for i in equation:
        for j in allowed_chars:
            if j == i.lower():
                if i.isdigit() or i.lower() == "x":
                    has_number = True
                correct_char_count += 1
                break

    if correct_char_count == len(equation) and has_number:
        return True
    else:
        return False

def calculate_equation(equation, x):
    if is_valid_equation(equation):
        equation = equation.lower().replace(" ", "")
        result = eval(equation)
        print(result)
        return result
    else:
        print("wrong equation") 