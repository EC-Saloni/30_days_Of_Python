#Area of a circle
pi = 3.14
r = float(input("Enter the value of redius:"))
area = pi*r**2
print(f"Area of a circle: {area}")

#Perimeter of circle
perimeter = 2*pi*r
print(f"Perimeter of circle:{perimeter}")

#Simple interest
p = float(input("Enter the value of principle:"))
r = float(input("Enter the value of rate:"))
t = float(input("Enter the time:"))
simple_interest = (p*r*t)/100
print(f"Simple interest:{simple_interest}")

#Converting Farheinheit to celcius
f = float(input("Enter temperature in farheinheit:"))
c = (f-32)*5/9
print(f"Temperature in Celcius:{c}")

#Converting celcius to farheinheit
c = float(input("Enter temperature in celcius:"))
f = (c*9/5)+32
print(f"Temperature in farheinheit:{f}")