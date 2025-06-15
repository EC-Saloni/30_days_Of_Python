import sys
import time

# 'GENERATOR'


#QUESTION NO 1 -  Even Numbers Generator -
              # Write a generator function generate_evens(n) that yields even numbers from 0 up to n.

def generate_evens(n):
    for i in range(n):
        if i%2 == 0:
          yield i
    
    
for num in generate_evens(20):
    print(num)


#QUESTION NO 2 - Countdown Generator -
                #Create a generator countdown(n) that yields numbers from n to 0.

def countdown(n):
    for i in range(n,0,-1):
        yield i

for i in countdown(20):
    print(i)


#QUESTION NO 3 - Infinite Natural Numbers -
                # Write a generator natural_numbers() that yields numbers starting from 1 and goes on forever.

def natural_numbers():
    i = 1
    while True:
        yield i
        i +=1

for i in natural_numbers():
    print(i)


#QUESTION NO 4 - Lines Starting with a Word -
                #Create a generator that reads a file and yields only lines that start with the word "Error".

def read_error_line(filename):
    with open(filename,'r') as file:
        for line in file:
            if line.startswith( 'Error'):
                yield line

for i in read_error_line('a.txt'):
    print(i)



# COMPARISON BITWEEN LIST AND GENERATORS



#QUESTION NO 5 - Memory Usage Comparison -
                # Create a list that stores squares of numbers from 1 to 1 million.
                # Then write a generator that does the same.
                # Measure and print memory usage of both using the sys.getsizeof() function.

#list
start = time.time()
list = []
for i in range(1000000):
    list.append(i**2)
print(list)
end = time.time()
print("List Time:", end - start, "seconds") #output : 0.25 seconds
print(sys.getsizeof(list))  #output : 824464


#Generator 
def sqr_gen(n):
    for i in n:
     yield i**2

start1 = time.time()
for i in sqr_gen(1000000):
    print(i)
end1 = time.time()

print("List Time:", end1 - start1, "seconds") #output : 0.20 seconds
print(sys.getsizeof(sqr_gen(100000))) #output : 112

