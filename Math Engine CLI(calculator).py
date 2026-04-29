import os as o
import math

def Enter_the_process():
        while True:
            try:   
                num1, process, num2 = int(input("Enter first number: ")), input("Enter operation (+, -, *, /): "), int(input("Enter second number: "))
                return num1, process, num2
            except ValueError:
                print("Please enter valid numbers")
                input("Press Enter to continue")
                o.system("cls")

def calculation(num1, process, num2):
    if process == "+":
        result = num1 + num2

    elif process == "-":
        result = num1 - num2

    elif process == "*":
        result = num1 * num2

    elif process == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        else:
            result = num1 / num2

    elif process == "xy":
        result = num1 ** num2

    elif process == "sqrt":
        result = num1 ** 0.5

    elif process == "cot":
        result = 1 / math.tan(num1)

    elif process == "log":
        result = math.log(num1)

    elif process == "ln":
        result = math.log(num1, math.e)

    elif process == "abs":
        result = abs(num1)

    elif process == "!":
        result = 1
        for i in range(1, num1 + 1):
            result *= i

    elif process == "sqrt":
        result = num1 ** 0.5

    elif process == "sin":
        result = math.sin(num1)

    elif process == "cos":
        result = math.cos(num1)

    elif process == "tan":
        result = math.tan(num1)

    
    try:
        return result
    
    except:
        o.system("cls")
        input("Invalid operation!\nPress Enter to continue")
        return None

def exit_menu():
    o.system("cls")
    print("1.main menu\n2.exit")
    chouse = input("enter your chouse(1 or 2)?")
    if chouse == "1":
        main()
    else:
        exit()

def help():
    o.system("cls")
    print("""
    +: addition
    -: subtraction
    *: multiplication
    /: division
    xy: exponentiation
    sqrt: square root
    cot: cotangent
    log: logarithm
    ln: natural logarithm
    abs: absolute value
    !: factorial
    sin: sine
    cos: cosine
    tan: tangent
    """)
    input("Press Enter to continue")
    o.system("cls")

def main():
    chouse = input("""
    1.calculater
    2.help
    3.exit
    enter your chouse:
    """)
    if chouse == "1":
        main()
    elif chouse == "2":
        help()
    else:
        exit()
    a = 0
    while True:
        o.system("cls")
        if a == 0:
            input("Welcome to my Simple Calculator!\nPress Enter to continue")
        o.system("cls")
        try:
            output = calculation(*Enter_the_process())
        except:
            print("cannot divide by zero!")
            input("Press Enter to continue")
            o.system("cls")
            continue
        if output is not None :
            o.system("cls")
            input(f"Result: {output}\nPress Enter to continue")
            exit_menu()
        a = 1

if __name__  == "__main__":
    main()

