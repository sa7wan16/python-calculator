from calc_art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {"+":add, "-":subtract, "*": multiply, "/":divide}
def calculator():
    print(logo)
    num1 = float(input("Enter your first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operator = input("pick an operator : ")
        num2 = float(input("Enter your next number: "))
        calculation = operations[operator]

        answer = calculation(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")
        restart = input(f"press 'y' to continue with {answer}, press 'n' to restart the calculator, press 'x' to exit")
        if restart == "y":
            num1 = answer
        elif restart == "x":
            print("GoodBye")
            should_continue = False
        else:
            should_continue = False
            calculator()

calculator()



