#Simple Calculator

#Receives Input of operands and operator
value1=float(input("Enter first number:")) 
value2=float(input("Enter second number:")) 
operator=input("Choose operation: +,-,*,/") 

#Conditions which checks string value
if operator == '+':
    print("Result:", value1 + value2) 
elif operator == '-':
    print("Result:", value1 - value2) 
elif operator == '*':
    print("Result:", value1 * value2) 
elif operator == '/':
    if value2!=0: 
        print("Result:", value1 / value2) 
    else:
        print("Error: Division by zero") #Handles division by zero
else:
    print("Invalid operation") #Handles Invalid operator

