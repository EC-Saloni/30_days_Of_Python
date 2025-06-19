import re

# 'REGULAR EXPRESSION'

# QUESTION NO 1 - Find all digits in a string
            # Text: "My ID is 245 and PIN is 7865"

Text = "My ID is 245 and PIN is 7865"
pattern = r"\d+"

matches = re.findall(pattern,Text)

if matches:
    print(matches)  # Output: ['245', '7865']


#QUESTION NO 2 - Match valid mobile numbers (10 digits)
                # Text: "Call me at 9876543210 or 12345"

Text= "Call me at 9876543210 or 12345"
Pattern= r"\b\d{10}\b"

matches = re.search(Pattern,Text)

if matches:
    print("Phone number :",matches.group()) #Output : Phone number : 9876543210



#QUESTION NO 3 - Match valid email addresses
                # Text: "Emails: test@mail.com, wrong@mail, user@site.org"

Emails= "test@mail.com, wrong@mail, user@site.org"
Pattern= r"[\w\.-]+@[\w\.-]+\.\w+"

matches = re.match(Pattern,Emails)

if matches:
    print("Valid Email:",matches.group())  #Output : Valid Email: test@mail.com


#QUESTION NO 4 - Find dates in format DD/MM/YYYY
                # Text: "Today's date is 19/06/2025"
            
Sentence = "Today's date is 19/06/2025"
Pattern= r"\b\d{2}/\d{2}/\d{4}\b"

matches = re.search(Pattern,Sentence)

if matches:
    print("Date : ", matches.group())


#QUESTION NO 5 - Match strong passwords
                # Criteria: At least 8 characters, includes a digit, lowercase, uppercase, and special character

Password = "Karina@123"
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

matches = re.match(pattern,Password)

if matches:
    print("Strong password : ",matches.group())
else:
    print("Week password")


#QUESTION NO 6 -Match all valid Indian PIN codes (6 digits, not starting with 0)
               

PIN_Code = "239300"
pattern = r"\b[1-9][0-9]{5}\b"

matches = re.match(pattern,PIN_Code)

if matches:
    print("Valid PIN code : ",matches.group()) # Output : Valid PIN code :  239300
else:
    print("Invalid PIN Code")


#QUESTION NO 7 - Find all repeated words (like "the the")
                # Text: "This is is a test test sentence"
                

Text= "This is is a test test sentence"
Pattern= r"\b(\w+)\s+\1\b"

matches = re.findall(Pattern,Text)

if matches:
    print(matches) #Output : ['is', 'test']
