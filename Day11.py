import calc  #Import calc user built module

print(calc.add(4,5))  #Addition
print(calc.sub(12,5)) #Substraction
print(calc.mul(3,11))  #Multiplication
print(calc.div(20,4))  #Division

#Calculating factorial of a number
print(f"Factorial : {calc.fact(4)}")

#Fibbonacci series till n
print("Fibbonacci series : ")
for i in range(7):
    print(calc.fibb(i),end=" ")
