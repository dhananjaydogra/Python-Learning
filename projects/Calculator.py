logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
    return n1 + n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def subtract(n1,n2):
    return n1 - n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

selection='n'
result=0.0

continue_calc=True
while continue_calc:
    if selection != "y":
        print(logo)
        num_1=float(input("What is the first number?: "))
    else:
        num_1=result
    for operators in operations:
        print(operators)

    operator= input("Pick an operation: ")
    num_2=float(input("What is the next number?: "))

    result=operations[operator](num_1,num_2)
    print(f"{num_1} {operator} {num_2} = {result}")

    selection=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or 'e' to Exit: ").lower()
    if selection =='n':
        print("\n"*100)
    elif selection == 'e':
        continue_calc = False
