# q1
s=input("Enter sentence:")
if s.count(' ')>=5:
    print(s)
else:
    s=input("Enter sentence:")

# q2
s=input("Enter sentence:")
if s.count(' ')>=5:
    print(s)
else:
    s=input("Enter sentence:")

# q3
n = int(input("Enter the number:"))
factors = []
for i in range(1,n+1):
    if n%i == 0:
        factors.append(i)
print(factors)

# q4
n1=int(input("Enter number:"))
n2=int(input("Enter number:"))
if n1%n2==0:
    print(f"{n1} is multiple of {n2}")
else:
    print(f"{n1} is not multiple of {n2}")

# q5
input_user  = input(" Enter the sentence:")
if len(input_user)<6:
    print("lemgth is less the 6 try again.")
    input_user  = input(" Enter the sentence:")
else:
    print(input_user)

# q6
a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))
d=(b**2-4*a*c)
s1=(-b+d**0.5)/(2*a)
s2=(-b-d**0.5)/(2*a)
print(f"Solutions of quadratic equation are {s1} and {s2}")

# q7
a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))
d=(b**2-4*a*c)
s1=(-b+d**0.5)/(2*a)
s2=(-b-d**0.5)/(2*a)
print(f"Solutions of quadratic equation are {s1} and {s2}")

# q8
n1=int(input("Enter number:"))
n2=int(input("Enter number:"))
if n1%n2==0:
    print(f"{n1} is multiple of {n2}")
else:
    print(f"{n1} is not multiple of {n2}")

# q9
l=eval(input("Enter list"))
l.reverse()
print(l)
l.sort()
print(l)
l.append(6)
print(l)

# q10
t=eval(input("Enter tuple:"))
c=t.count(0)
print(f"{t} has {c} zeros")

# q11
t=eval(input("Enter list:"))
t2=[]
for i in t:
    if i in t2:
        pass
    else:
        t2.append(i)
print(t2)

# q12
t=eval(input("Enter list:"))
t2=[]
for i in t:
    if i in t2:
        pass
    else:
        t2.append(i)
print(t2)

# q13
import random

print(random.randint(0,100))


import cmath
a = 1 
b = 5 
c = 6 
# calculate the discriminant
d = (b**2) - (4*a*c)

# find the solution
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print("the soiution are {0} and {1}".format(sol1,sol2))