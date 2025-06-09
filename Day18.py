#"ENCAPSULATION"

#QUESTION NO 1 -  Create a Student class with: # Private variables: __name, __marks.
                    # A method to set marks only if they are between 0 and 100.
                    # A method to display student details.

class Student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks
    
    def set_marks(self,marks):
        if self.__marks >=0 and self.__marks <=100:
            self.__marks = marks
        else:
            print("Enter valid number(between 0 to 100)")

    def display_details(self):
        print(f"Name of the student : {self.__name}")
        print(f"Marks of the student : {self.__marks}")

s = Student("Ali",75)
s.set_marks(81)
s.display_details()

#QUESTION NO 2 - Create a PasswordManager class with: # Private variable __password.
                # Methods to set a new password (must be at least 8 characters, contain numbers and letters).
                # A method to verify a password entered by the user.

class PasswordManager:
    def __init__(self,password):
        self.__password = password

    def set_pass(self,password):
            if len(password) >=8:

                has_letter = False
                has_number = False

                for i in password:
                    if i.isalpha():
                        has_letter =True
                    elif i.isdigit():
                        has_number = True

                if  has_letter and has_number:
                        self.__password = password
                else:
                        print("Plaese enter letters and numbers!!")
            else:
                print("Password must be 8 or more than 8 characters!!")

    def display(self):
        print(f"Your password:{self.__password}")

    def verify_user_input(self,prompt):
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        else:
            print("No input provided!!")

p = PasswordManager("rinki563")
new_pass = p.verify_user_input("Enter your password:")
if new_pass:
    p.set_pass(new_pass)

p.display()