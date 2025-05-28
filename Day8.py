# "DICTIONARY"

#Create a dictionary 
d = {"a":1, "b": 2,"c":3}

#Access the value with the help of key
print(d.items())

#Accessing key value pairs in for loop
for key,value in d.items():
    print(key,value)

#QUESTION 1 - Create a contact book
contact = {
    "jony" : {
        "name": "Jony",
        "Mobile no." : 28796314,
        "Email" : "jony28@gmail.com"
    },
    "tony" : {
        "name" : "Tony",
        "Mobile no." : 84679321,
        "Email" : "tony84@gmaail.com"
    },
    "bob" : {
        "name": "Bob",
        "Mobile no." : 880886532,
        "Email" : "bob88@gmail.com"
    },
    "alice" : {
        "name" : "Alice",
        "Mobile no." : 94553217,
        "Email" : "Alice94@gmail.com"
    }
}
for key,value in contact.items():
    print(key,value)

#QUESTION 2 - Add a new persion in dictionary contact
contact.update(alexa = {"name":"Alexa","Mobile no.":8563247,"Email":"Alexa85@gmail.com"})
for key,value in contact.items():
     print(key,value)

#QUESTION 3 - Merge 2 dictionary
d1 = {"d":4,"e":9,"f":6}
d.update(d1)
print(d)
# OR
merge_dic = {**d,**d1}
print(merge_dic)


#QUESTION 4 - Find the key with maximum value in a dictionary
max_value = max(d,key=d.get)
print(max_value)

#QUESTION 5 - Group the element by their length
a = ["cat","bat","apple","banana","grapes","dog" ]
d3 = {}
for i in a:
    length = len(i)
    if length in d3:
        d3[length].append(i)
    else:
        d3[length] = [i]
print(d3)

#QUESTION 6 - count charecter frequency in a string using a dictionary
name3 = "Marry"
d4 = {}
for i in name3:
    if i in d4:
        d4[i] += 1
    else:
        d4[i] = 1
print(d4)
