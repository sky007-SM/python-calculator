#Standard Calculator 
def calculate(value1, value2, operator):

    #Conditions which checks string value
    if operator == '+':
        return value1 + value2 
    elif operator == '-':
        return value1 - value2 
    elif operator == '*':
        return value1 * value2 
    elif operator == '/':
        if value2 != 0: 
            return value1 / value2
        else :
            print("Error: Division by zero") #Handles division by zero
    else:
        print("Invalid operation") #Handles Invalid operator
        

def main():

    choice = 'y'
    while choice.lower() != 'n':
        try:
            #Receives Input of operands and operator
            value1 = float(input("\nEnter first number:"))
            value2 = float(input("Enter second number:"))
        except ValueError:
            print("Error: Invalid number input") #Handles Invalid character input
            print("Input valid values")
        else:
            operator = input("Choose operation: +,-,*,/") 
            result = calculate(value1,value2,operator)
            if result is not None:
                print("Result:", result)
        choice = input("\nDo you want to Continue: y/n")
        while choice.lower() not in ["n", "y"]:
            print("Invalid choice entry")
            choice = input("\nDo you want to Continue: y/n")

main()
        

