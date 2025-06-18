import time

# ['DECORATORS']

#QUESTION NO 1 - Decorator with One Function
                # Create a decorator @double_output that multiplies the return value of the function by 2.

def double_output(func):
    def wrapper(*args):
        return func(*args)*2
    return wrapper

@double_output
def abc(n):
    return n

print(abc(5)) #output : 10


#QUESTION NO 2 - Execution Time Decorator
                # Write a decorator timer that prints the time taken to execute a function.

def time_print(func):
    def wrapper():
        start = time.time()
        starting_time = time.strftime("%H:%M:%S",time.localtime(start))
        print(f"Starting time : {starting_time}")

        func()

        end = time.time()
        ending_time = time.strftime("%H:%M:%S",time.localtime(end))
        print(f"Ending time : {ending_time}")

        total_time = end - start
        print(f"The time taken to execute a function : {total_time:.5f} seconds")
    return wrapper

@time_print
def execution_time():
    print("Hello World!!")

execution_time()


#QUESTION NO 3 - Argument Logger
                # Write a decorator log_args that prints the arguments passed to a function each time it is called.
                ## When multiply(2, 3) is called, it should print: "Arguments: (2, 3)"


def log_args(func):
    def wrapper(*args,**kwrags):
        return f"Arguments{*args,*kwrags}"
    return wrapper

@log_args
def multiply(x,y):
    return x*y

print(multiply(5,6)) #Output - Arguments(5, 6)

#QUESTION NO 4 - Chaining Multiple Decorators  -
                #  Write two decorators:
                # One that converts a function’s return string to uppercase.
                # One that adds a prefix "Result: ".
                # Chain them both on a function that returns "hello world".

def uppercase_fun(func):
    def wrapper(*args):
        result = func(*args)
        return result.upper()
    return wrapper

def add_prefix(func):
    def wrapper():
        return f"Result: {func()}" 
    return wrapper


@add_prefix
@uppercase_fun
def hw():
    return f"hello world"

print(hw())  #Output - Result: HELLO WORLD


