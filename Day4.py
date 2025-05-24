#Check if a number is even or odd
num = 40
if num%2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Largest among 3 numbers
n1 = 5
n2 = 9
n3 = 10
if n1>=n2 and n1>=n3:
    print(f"n1 '{n1}' is the largest number.")
elif n2>=n1 and n2>=n3:
    print(f"n2 '{n2}' is the largest number.")
else:
    print(f"n3 '{n3}' is the largest number.")

#Student grade calculator
name = input("Enter student's name:")
math_mark = int(input("Enter maths marks:"))
eng_mark = int(input("Enter english marks:"))
sci_mark = int(input("Enter science marks:"))
hin_mark = int(input("Enter hindi marks:"))
com_mark = int(input("Enter computer marks:"))

total = math_mark+eng_mark+sci_mark+hin_mark+com_mark
per = total/5
print(name)
print(total)
print(per)

if per >= 80 :
    print("Grade A")
elif per >=60:
    print("Grade B")
elif per >=40:
    print("Grade C")
else:
    print("Fail!!")