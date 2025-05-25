#Sum of 100 natural numbers
sum = 0
for i in range(1,101):
    sum +=i
print(f"Sum of 100 natural numbers:{sum}")


# #Print a table using for loop
num = int(input("Enter a number you want to print table:"))
for i in range(1,11):
    print(f"{num}*{i} = {num*i}")


#Factorial of a number using for loop
fact = 1
n = int(input("Enter a number you want factorial:"))
for i in range(1,n+1):
    fact = fact*i
print(f"Factorial of {n} is : {fact}")


#Print a pattern like this:
""" 
*
**
***
****
"""
for i in range(1,5):              
    print("*" *i)

# #Generate fibbonacci series upto n 
n1 = 0
n2 = 1
i = 2
n = int(input("Enter n:"))
print(f"{n1}\n{n2}")
while(i<=n):
     n1 , n2 = n2 , n1+n2
     i += 1
     print(n2)

#Check if a number is a armstrong or not
add = 0
number = int(input("Enter a number:"))
l_num = len(str(number)) #Converting in string because we can't find length of a int in python directly
for i in str(number): #Converting in string because int is not iterable
     add += int(i)**l_num
if (number == add):
     print(f"{number} is the Armstrong number. ")
else:
     print(f"{number} is not a Armstrong number.")


     
     





