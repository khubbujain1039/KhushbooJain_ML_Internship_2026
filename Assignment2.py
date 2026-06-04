 #Sum of First 10 Natural Numbers
sum = 0
for i in range(1, 11):
    sum += i
print("Sum of first 10 natural numbers:", sum)


#Factorial of a Number
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)


#Fibonacci Series up to n terms
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


#Largest Among 3 Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number =", largest)



#Student Result System
print("===== STUDENT RESULT SYSTEM =====")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

subjects = int(input("Enter number of subjects: "))

total = 0

for i in range(subjects):
    marks = float(input(f"Enter marks of Subject {i+1}: "))
    total += marks

percentage = total / subjects

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Total Marks:", total)
print("Percentage :", percentage)
print("Grade      :", grade)




