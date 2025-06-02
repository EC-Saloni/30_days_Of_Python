def add(a,b): #Addition
    return a+b

def sub(a,b): #Substraction
    return a-b

def mul(a,b): #Multiply
    return a*b

def div(a,b): #Divide
    return a/b

def fact(n):
     if n<0 :
         return "Factorial of negative value is not defined"
     if n==0 or n==1:
        return 1
     else:
        return n*fact(n-1)
     

def fibb(n):
        if n==0:
           return 0
        elif n==1:
           return 1
        else:
           return fibb(n-1)+fibb(n-2)