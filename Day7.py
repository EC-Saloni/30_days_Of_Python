#TUPLES
#Create a tuple
t1 = (1,2,3,4,5)

#QUESTION 1 - Coverting into list
l1 = list(t1)
print(l1)
print(type(l1))
#Converting list into tuple
t = tuple(l1)
print(t)
print(type(t))

#QUESTION 2 - Count the number of times an element appears in a tuple.
t2 = (1,2,3,1,3,4,1)
print(t2.count(1))

#QUESTION 3 - Sort a number of tuple
l2 = list(t2)
l2.sort()
print(tuple(l2))

#QUESTION 4 - Creating a tuple of tuple and extract all first elements
t4 = ((1,2,3),(4,5,9),(6,7,8))
print(len(t4))
for i in range(len(t4)):
    for j in range(len(t4[i])):
        if t4[i][j] == t4[i][0]:
            print(f"First element of row {i}:{t4[i][j]}")

#   "SET"
#Create a set
s = {1,2,3,4}

#QUESTION 1 - Add 5 in the set
s.add(5)
print(s)

#QUESTION 2 - Remove 2 from the set
s.remove(2)
print(s)

#QUESTION 3 - Convert a list into set to remove duplicate values
l = [1,1,2,3,2,4,3]
print(set(l))

#QUESTION 4 - Find the union, intersection,Difference, symmetric difference of a set
s1 = {2,4,5,6}
print(f"Union : {s.union(s1)}") #Union '|'
print(f"Intersection : {s.intersection(s1)}") #Intersection '&'
print(f"Difference : {s.difference(s1)}") #Differnce '-'
print(f"Symmetric difference : {s.symmetric_difference(s1)}") #Symmentric difference '^'
    
#QUESTION 5 - Given a string, find all unique vowels used in it using sets.

name = "Saloni"
vowel = {"a","e","i","o","u"}
s2 = set(name)
for ch in s2:
    if ch in vowel:
        print(ch)

#2nd method
print(s2&vowel) #Intersection of s2 and vowel sets
