#Length of a string
name = "Arijit"
print(len(name))

#Reverse of a string
lan = "Programming Language"
print(lan[::-1])

#Count the vowel in the string
count = 0
vowels = ["a","e","i","o","u"]
for ch in range(len(lan)):
     for vo in range(len(vowels)):
       if(lan[ch]==vowels[vo]):
           count +=1
       else:
           continue
print(f"Number of vowels:{count}")

#Check if a string is a palindrom or not
s = "madam"
reverse_s = s[::-1]
if (s==reverse_s):
    print(f"The given string '{s}' is a palindrom.")
else:
    print("The given string is not a palindrom.")

#First and last letter Match
m = "Eagle"
if m[0].lower() == m[-1].lower():
    print("MATCH")
else:
    print("NOT MATCH")


#Check password strength
#Conditions -
# strong if - length >=8 , upper case, lower case, number 
#Otherwise "weak"
password = input("Enter your password:")
if password.isalnum() == True:
    print("Strong Password!!")
else:
    print("Weak password!!")



        
