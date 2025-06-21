import math

#   'Comprehensions Deep Dive'


#QUESTION NO 1 - Create a list of cubes of odd numbers between 1 and 20.
cube = [x**3 for x in range(21) if x%2 != 0]
print(cube)   #Output : [1, 27, 125, 343, 729, 1331, 2197, 3375, 4913, 6859]



#QUESTION NO 2 - From a list of words, create a dict where key = word, value = length, but only for words with length > 4.
dic = {l:len(l) for l in ['apple','cat','mango','dog','grapes'] if len(l) > 4}
print(dic)  # Output : {'apple': 5, 'mango': 5, 'grapes': 6}



#QUESTION NO 3 - Use a generator expression to yield all even numbers below 100.
gen = (x for x in range(100) if x%2 == 0)
for i in gen:
    print(i)



#QUESTION NO 4 - From a list ["apple", "banana", "cherry", "kiwi", "fig"], create a list of words that contain the letter 'a'.
l1 = [x for x in ["apple", "banana", "cherry", "kiwi", "fig"] if 'a' in x]
print(l1)  #Output : ['apple', 'banana']



#QUESTION NO 5 - Create a dictionary where the keys are numbers 1 to 5 and the values are their factorials.
fact = {x:math.factorial(x) for x in range(6)}
print(fact)  #Output : {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120}



#QUESTION NO 6 - Create a dictionary where keys are characters from a string and values are their ASCII values.
ascii_value = {x:ord(x) for x in ['A','B','C','D','E']}
print(ascii_value)  #Output : {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69}



#QUESTION NO 7 - Given two lists A = [1, 2, 3], B = [4, 5, 6], build a list of all possible sums (i+j).
sums = [x+y for x in [1, 2, 3] for y in [4, 5, 6]]
print(sums)  #Output : [5, 6, 7, 6, 7, 8, 7, 8, 9]


