def add(a, b):
    return a + b

def subtract(a, b):
    return  a - b

def multiply(a, b):
    return  a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return  a / b

def square(x):
    return  x ** 2