def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# This is my code
# user input
def calculator():
    continue_problem = True
    num1 = float(input("What is the first number?: "))

    while continue_problem:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick a function: ")
        num2 = float(input("What is the second number you choose?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation")

        if choice == 'y':
            num1 = answer
        else:
            continue_problem = False
            print("\n" * 25)
            calculator()


calculator()

# This my Insructor's code
# should_accumulate = True
# num1 = float(input("What is the first number?: "))
#
# while should_accumulate:
#     for symbol in operations:
#         print(symbol)
#     operation_symbol = input("pick an operation: ")
#     num2 = float(input("What is the next number?: "))
#     answer = operations[operation_symbol](num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")
#
#     choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.")
#
#     if choice == "y":
#         num1 = answer
#     else:
#         should_accumulate = False
#         print("\n" * 20)
