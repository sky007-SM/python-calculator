#Standard Calculator 
choice = 'y'
while choice.lower() != 'n':
    try:
        #Receives Input of operands and operator
        value1 = float(input("\nEnter first number:"))
        value2 = float(input("Enter second number:"))
    except ValueError:
        print("Error: Invalid number input") #Handles Invalid character input
        print("Retry with valid values")
    else:
        operator = input("Choose operation: +,-,*,/") 

        #Conditions which checks string value
        if operator == '+':
            print("Result:", value1 + value2) 
        elif operator == '-':
            print("Result:", value1 - value2) 
        elif operator == '*':
            print("Result:", value1 * value2) 
        elif operator == '/':
            try: 
                print("Result:", value1 / value2)
            except ZeroDivisionError:
                print("Error: Division by zero") #Handles division by zero
        else:
            print("Invalid operation") #Handles Invalid operator
        choice = input("\nDo you want to Continue: y/n")
      

