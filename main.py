#Simple Calculator

value1=float(input("Enter first number:")) #Receives first operand
value2=float(input("Enter second number:")) #Receives second operand
operator=input("Choose operation: +,-,*,/") #Receives the operator

#Conditions which checks string value
if operator == '+':
    print(value1 + value2) #Displays sum of the two values
elif operator == '-':
    print(value1 - value2) #Displays difference of the two values
elif operator == '*':
    print(value1 * value2) #Displays product of the two values
elif operator == '/' and value2 !=0:
    print(value1 / value2) #Displays Quotient of the two values
else:
    print("Invalid operation") #Handles Invalid operator

