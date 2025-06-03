# "FILE HANDLING"

#QUESTION NO 1 - Write to a text file
with open("abc.txt","w") as file:
    file.write("Hello! I am a Python Developer.")
    file.write("\nI am at the learning phase. ")


#QUESTION NO 2 - Read to a text file
with open("abc.txt") as file:
    c = file.read()
    print(c)


#QUESTION NO 3 - Append to a text file
with open("abc.txt","a") as file:
    file.write("\nMy name is Saloni Yadav.")


#QUESTION NO 4 - Write a Python program that:
            # Takes name and marks of 3 students from the user.
            # Stores each student’s data in a file called students.
            #After storing the data, read and display the content of the file.
with open("Student.txt","w") as file:
    for i in range(1,4):
      name = input(f"Enter name of Student {i} : ")
      marks = int(input(f"Enter marks of {name} : "))
      file.write(f"Name : {name} , marks : {marks}\n ")

# #Read from that file
with open("Student.txt") as file:
   content = file.read()
   print(f"Reading data from students.txt...\n \n {content}")


#QUESTION NO 5 - count the character,words from the file
def char_word_count(file_name):
    with open(file_name,"r") as file:
      text = file.read()
      char_count = len(text)
      word_count = len(text.split())
    return char_count,word_count

file_name = "abc.txt"
result = char_word_count(file_name)
if result:
   char_count,word_count = result
   print(f"Character count : {char_count}")
   print(f"Word count : {word_count}")

    

         





