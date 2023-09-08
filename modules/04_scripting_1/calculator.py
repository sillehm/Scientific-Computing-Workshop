
def calculator():

    first = int(input("First number: "))

    second = int(input("Second number: "))

    operator = input("Operator: ")

    if operator == '+':
        print(f"Result: {first + second}")

    elif operator == '-':
        print(f"Result: {first - second}")
    
    elif operator == '*':
        print(f"Result: {first * second}")
    
    elif operator == "/":
        print(f"Result: {first / second}")


if __name__ == "__main__":
    calculator()