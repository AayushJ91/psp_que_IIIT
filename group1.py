# 1
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

# 2
n = int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end = ' ')
    print(' ')    

# 3
num = int(input("enter number"))
no_of_digits=0
while num>0:
    m = num%10
    no_of_digits+=1
    num=num//10

print(no_of_digits)

# 4
#squre root greatest integer

n = int(input("Enter the number:"))
for i in range(1,n):
    if i**2 > n:
        print(i-1)
        break

# squre root greatest integer using while loop
n = int(input("Enter the number:"))
while i >0:
    if i**2 > n:
        print(i-1)
        break


#using mathematics
n = int(input("Enter the number:")) 
a = n**0.5
print(a)

# 5
#sum of squares of frist n natural number

n = int(input("Enter the number:"))
sum = 0
for i in range(1, n+1):
    p = i**2
    sum = sum + p
print("the sum of squares:",sum)    

# 6
# input side of a square and print its area
side  = float(input("Enter the side of square:"))

#formula area = side x side
area = side **2
print(f" the area os square is: {side}x{side} = {area}")

# 7
# the prime number from 1 to N
n = int(input("Enter the number:"))

for i in range(2,n+1):
    for o in range(2,i):
        if i%o==0:
            break
    else:
        print(i)
    
# 8
# print number from 100 to 1
for i in range(100,0,-2):
    print(i)

# 9
P = input("Enter principal amount in rupees:")

R = input("Enter the iterest rate:")
T = input("Enter the time period in year:")
simple_interest = ((P*R)*T)
print(simple_interest)

# 10
# print a word n time 
n = int(input("Enter the number:"))
for i in range (1, n+1):
    if i < (n+1):
        print(f"{i} anil")

# 11
n = int(input("Enter the number:"))
if n == 1:
      print(f"{n} is not a prime number.")
elif n== 2: 
     print(f"{n} is a prime number.")     
else: 
      for i in range(2,n):
            if (n)%i==0:
                print(f"{n} is not a prime number.")
                break
            else:
                print(f"{n} is a prime number.")
                break

# 12
#print current datev and time
import datetime
now = datetime.datetime.now()
print("current date and time is",now)

# 13
# find the lenght of string

n = str(input("enter the string:"))
print(len(n))

# 14
# display all the numbers which are divisible by 11 but not by 2 between 100 and 500
 
for i in range(100,500):
    if (i%11 == 0 and i%2 != 0):
        print(i)

# 15
weight =int(input("enter thev weight in kg:"))
hight = float(input("enter thev hight in miter :"))
bmi = (weight)/(hight**2)
if 21< bmi <33:
    print("condidate qualified")
else:
    print("condidate not qualified")  

# 16
#fizzbuzz program
n = int(input("enter the number:"))
if (n%5==0 and n%3 ==0):
    print("Fizzbuzz instead of number")

elif n%3 == 0:
    print("Fizz instead of number")
elif n%5 == 0:

    print("buzz instead of number")

# 17
# check  if a number is amultiple of 7 or not

n = int(input("Enter the number:"))
 
if n%7 ==0:
    print(f"{n} is multiple of 7")
else:
    print(f"{n} is not multiple of 7")    

# 18
a = int(input("Enter the frist number:"))
b = int(input("Enter the second number:"))
if a >= b:
    print("true")
else:
     print("flase")

# 19
# cube root using for loop
n = int(input("ENTER THE NUMBER:"))
for i in range(1,n):
    if i**3 > n:
        print(i-1)
        break

# cube root using while loop
n = int(input("ENTER THE NUMBER:"))
while i > 0:
    if i**3 > n:
        print(i-1)
        break
# mathematics
n = int(input("ENTER THE NUMBER:"))
a = n**(1/3)
print(a)

# 20
# average of two floating number

def average(num1,num2):
    avg = (num1 + num2)/2
    return avg 
num1 = float(input("Enter the frist float number:"))
num2 = float(input("Enter the second float number:"))
avg = average(num1,num2)
print(f" average of {num1} and {num2} is {avg}")