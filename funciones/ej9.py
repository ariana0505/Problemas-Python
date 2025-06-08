def get_MCD(number1, number2):
  
    if number1 == number2:
        return number1

    while number2 != 0:
        remainder = number1 % number2
        number1 = number2
        number2 = remainder

    return number1

def get_MCM(a, b):
    mcd = get_MCD(a, b)
    return abs(a * b) // mcd