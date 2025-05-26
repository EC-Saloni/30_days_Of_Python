#Lists 
#QUESTION 1 - Find min and max in a list
l1 = [1,4,7,2,9,6,2,5,4]
print(f"Minimum of the list:{min(l1)}")
print(f"Maximum of the list:{max(l1)}")

#QUESTION 2 - Revome duplicate from the list
l2 = []
for i in l1: #Iterate over l1
    if i not in l2: #Check i is in l2 or not if not then append i in l2
        l2.append(i)
print(l2) 

#QUESTION 3 - list comprehension of square of a even number
s = [i**2 for i in l1 if i%2 == 0]
print(s)

#QUESTION 4 - Sort a list in decending order
l1.sort(reverse=True)
print(l1)

#QUESTION 5 - Sum and average of list elements
sum = 0
lst = [2,5,4,3]
for i in range(0,len(lst)):
    sum+=lst[i]
print(f"Sum of lst:{sum}")

avg = sum/len(lst)
print(f"Average of lst:{avg}")

#QUESTION 6 - Remove all even number from the list
for i in lst[:]: #making copy of a list
    if i%2 == 0:
        lst.remove(i)
print(lst)

#QUESTION 7 - Flatten 2D list into 1D list
two_D_l = [[1,2,3],[4,5,6]]
First take sublists like [1,2,3] and [4,5,6]
Then take i in sublists like 1,2,3,4,5,6
Then print i
flatten = [i for sublist in two_D_l for i in sublist]
print(flatten)

#QUESTION 8 - Find common elements in two lists
lst1 = [1,3,5,7]
lst2 = [2,4,5,6]
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i] == lst2[j]:
            print(f"Common : {lst1[i]}")

#QUESTION 9 - Split a list into two - one containing even numbers other containing odd numbers
l3 = [1,3,5,4,9,8,2]
even = []
odd = []
for i in range(len(l3)):
    if l3[i]%2 == 0:
        even.append(l3[i])
    else:
        odd.append(l3[i])
print(f"Even number list:{even}")
print(f"odd number list:{odd}")

#QUESTION 10 - Rotate a list to the right by 2 position
n = 2
#l3[-2:]+l3[:-2] = [8,2]+[1,3,5,4,9] = [8,2,1,3,5,4,9]
rotate_lst = l3[-n:]+l3[:-n]
print(l3)
print(rotate_lst)

    
    








