import art
#create various functions that takes in values and returns the output based on the function
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}

def calculator():
    print(art.logo)
    num1 = float(input("What's your first number?: "))
    should_continue =True
    while should_continue:
        for key in operators:
            print(key)
        operation = input("Pick an operation: ")

        num2 = float(input("What's your second number?: "))

        result = operators[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, "
              f"or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            num1 = result
        elif choice == "n":
            should_continue = False
            print("\n" * 5)
            calculator()

calculator()

