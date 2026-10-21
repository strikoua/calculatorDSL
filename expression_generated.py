def calculate():
    return 1 + 2 * 4 / 3

try:
    print(calculate())
except ZeroDivisionError:
    print("Cannot divide by zero")