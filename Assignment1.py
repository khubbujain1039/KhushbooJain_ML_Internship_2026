# 1.Find area of rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of rectangle =", area)

# 2. Find simple interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (years): "))

si = (principal * rate * time) / 100

print("Simple Interest =", si)

#3. Convert a temperature from celsius to fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

#4.calculate average of 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)

# 5.find sqaure and cube of a number
num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)

# 6. Swap two numbers without using third variablec
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

# 7. Create a student report Program that take student details using input()
#Store students marks in variable and calculate total marks and percentage.10

name = input("Enter student name: ")

m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)