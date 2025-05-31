#    "FUNCTION"
#QUESTION 1 - Create a function to add,substract,multiply and divide between 2 numbers
#Void functions
def add(a,b): #Addition
    return a+b

def sub(a,b): #Substraction
    return a-b

def mul(a,b): #Multiply
    return a*b

def div(a,b): #Divide
    return a/b

n1 = int(input("Enter 1st number:"))
n2 = int(input("Enter 2nd number:"))
print(f"Addition : {add(n1,n2)}")
print(f"Substraction : {sub(n1,n2)}")
print(f"Multiply : {mul(n1,n2)}")
print(f"Divide : {div(n1,n2)}")

#QUESTION 2 - Create a recursive function of factorial
def fact(n):
     if n<0 :
         return "Factorial of negative value is not defined"
     if n==0 or n==1:
        return 1
     else:
        return n*fact(n-1)

n3 = int(input("Enter a number:"))
print(f"Factorial of {n3} is : {fact(n3)}")

#QUESTION 3 - Create a recursive function of fibbonacci series
def fibb(n):
        if n==0:
           return 0
        elif n==1:
           return 1
        else:
           return fibb(n-1)+fibb(n-2)

n4 = int(input("Enter a number:"))
print(f"Fibbonacci series till {n4} is :")
for i in range(n4):
    print(fibb(i),end=" ")

# #QUESTION NO 4 - Create a function to calculate the BMI(Body Mass Index )
def bmi(w,h):
    return w/(h**2)

weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in meter : "))
print(f"Your BMI is : {bmi(weight,height)}")

#QUESTION NO 5 - Create a function to check if the number is prime or not
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True    

print(is_prime(5))


#QUESTION NO 6 - Create a lambda function to square a number
sqr = lambda x:x**2
print(sqr(6))
        
