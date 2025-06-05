# "MAP-FILTER-REDUCE"
from functools import reduce

#QUESTION NO 1 - Given a list of numbers,return a list with each numbers squared using map()
# num = [1,2,8,6,7,9]
# sqr = list(map(lambda x:x**2,num))
# print(sqr)

# #QUESTION NO 2 - Convert a list of lowercase strings to uppercase using map().
fruits = ["apple","mango","banana","lichi","orange"]
# upperString = list(map(lambda x:x.upper(),fruits))
# print(upperString)

# #QUESTION NO 3 - Return a list of lengths of each string in the list.
# lengthOfList = list(map(lambda x:len(x),fruits))
# print(lengthOfList)

# #QUESTION NO 4 - From a list of integers,filter out only the even numbers using filter().
# evenNum = list(filter(lambda x: x%2 == 0,num))
# print(evenNum)

# #QUESTION NO 5 - Given a list of characters,filter out only the vowels.
# char = ['a','c','r','o','y','u','s']
# vowels = list(filter(lambda x:x == 'a' or x=='e' or x=='i' or x=='o' or x=='u',char ))
# print(vowels)

# #QUESTION NO 6 - From a list of strings,filter only the palindroms(words that read the same backward).
# word = ["madam","saloni","racecar","hello","sam"]
# palindrom = list(filter(lambda x:x==x[::-1],word))
# print(palindrom)

# #QUESTION NO 7 - Find the product of all numbers in a list using reduce().
# product = reduce(lambda x,y:x*y ,num)
# print(product)

# #QUESTION NO 8 - Use reduce() to find the largest number in a list.
# # largestNum = reduce(lambda x,y:x if x>y else y , num)
# # print(largestNum)

# #QUESTION NO 9 - Use reduce() to concatenate all strings.
# w = ["hello" ," ", "World" , "!"]
# concatenate = reduce(lambda x,y:x+y , w)
# print(concatenate)

#QUESTION NO 10 - Square odd numbers and find their sum from a list of integers.
# a = [1,2,3,4,5,6,7,8,9,10]
# odd = list(filter(lambda x:x%2 != 0 ,a))
# square = list(map(lambda x:x**2,odd))
# sum = reduce(lambda x,y:x+y , square)
# print(f"Odd numbers : {odd}")
# print(f"Square of odd numbers : {square}")
# print(f"Sum of square : {sum}")


#"zip(),enumerate(),any(),all()"

#QUESTION NO 11 - you have two lists.USe zip() to print output like: l1-item:l2-item
# name = ["Alice","Bob","Tony","Tom"]
# score = [90,87,78,63]
# for name,score in zip(name,score):
#     print(f"{name} : {score}")
             
#QUESTION NO 12 - Create a dictionary from two lists.
# keys = ["id","name","age"]
# values = [100,"Alice",21]
# z = zip(keys,values)
# print(dict(z))

#QUESTION NO 13 - Use enumerate() to print: index:list_item
# for index,fruit in enumerate(fruits,1):
#     print(f"{index} : {fruit}")

#QUESTION NO 14 - check if any of the numbers in the list is divided by 5.
# n = [11,16,8,10,15]
# a = any(i%5 == 0 for i in n)
# print(f"Number is divided by 5 : {a}")

#QUESTION NO 15 - Check if all the items in list are positive.
num = [1,6,2,4,0,-8,-1]
al = all(i>=0 for i in num)
print(f"All the items are positive : {al}")
