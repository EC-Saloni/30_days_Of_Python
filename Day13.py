# "EXCEPTION HANDLING"
class NegativeNumberError(Exception):
    pass


#QUESTION NO 1 - Handle divide-by-zero error
try:
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    divide = a/b
    print(divide)

except ZeroDivisionError:
    print("You can't divide a number with zero.")

#QUESTION NO 2 - Handle file not found error
try:
    with open("erf.txt","r") as file:
        c = file.read()
        print(c)

except FileNotFoundError:
    print("This file is not exist.")

#QUESTION NO 3 - Create a custom exception
def checkForNegative(x,y):
    if x<0 or y<0:
        raise NegativeNumberError("Negative number is not allowed.")
    else:
        print("The number is positive.")
        
try:
     a1 = int(input("Enter value of a1(non-negative) : "))
     b1 = int(input("Enter value of b1(non-negative) : "))
     checkForNegative(a1,b1)
     divide = a1/b1
     print(divide)

except NegativeNumberError as e:
    print(f"Error : {e}")

except ZeroDivisionError as e:
    print(f"Error : {e}")

#QUESTION NO 4 - Write a calculator that performs addition,substraction,multiplication,and division.
#                Handle invalid input using nested try blocks.
def calculator():
    try:
        n1 = int(input("Enter the value of n1 : "))
        n2 = int(input("Enter the value of n2 : "))
        operator = input("Enter the operator : ")
        try:
            if operator == '+':
                print(f"Addition : {n1+n2}")
            elif operator == '-':
                print(f"Substraction : {n1-n2}")
            elif operator == '*':
                print(f"Multiplication : {n1*n2}")
            elif operator == '/':
                print(f"Division : {n1/n2}")
        except ZeroDivisionError:
            print("You can't divide a number with zero.")

    except ValueError:
        print("Invalid input! Please enter a valid number")

    finally:
        print("Thank you for execution.")

calculator()
        
            


        
 


    