def calculator(a, b, operator):
    pass

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b

    elif operator == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b