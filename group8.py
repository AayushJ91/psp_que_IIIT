# 1
# average of two floating number

def average(num1,num2):
    avg = (num1 + num2)/2
    return avg 
num1 = float(input("Enter the frist float number:"))
num2 = float(input("Enter the second float number:"))
avg = average(num1,num2)
print(f" average of {num1} and {num2} is {avg}")

# 2
s1 = float(input("side1 lenght"))
s2 = float(input("side2 lenght"))
s3= float(input("side3 lenght"))
s = (s1+s2+s3)/2
area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
print(f"area of triangle:{area}")
print(f"permeter is:{s*2}")

# 3
x1 = float(input(" x1:"))
x2 = float(input(" x2:"))
y1 = float(input(" y1:"))
y2 = float(input(" y2:"))
distance = ((((x1-x2)**2)+ ((y1 - y2)**2))**0.5)
print(distance)

# 4
age = int(input("enter the age:"))
if age>=18:
    print("condidate eligible for voting.")
else:
    print("condidate not eligible for voting.")

# 5
n=int(input("Enter input:"))
if n%2!=0:
    print('Weird')
elif n%2==0 and n in range(2,5):
    print('Not Weird')
elif n%2==0 and n in range(6,20):
    print('Weird')
elif n%2==0 and n>20:
    print('Not Weird')

# 6
s=input("Enter:")
ex=['.jpg','.gif','.png','.pdf','.txt','.zip']
if s[-4:] in ex or s[-5:]=='.jpeg':
    print('VALID')
else:
    print('INVALID')

# 7
def sum_of_odd_numbers(n):
    i = 1
    total_sum = 0
    while i <= n:
        if i % 2 != 0:
            total_sum += i
        i += 1
    print("The sum of all odd numbers from 1 to", n, "is:", total_sum)

# 8
price1 = int(input("Price of frist item:"))
price2 = int(input("Price of second item:"))
price3 = int(input("Price of thired item:"))
tax1 = (price1*8)/100
tax2 = (price2*8)/100
tax3 = (price3*8)/100
print("total cost",price1+price2+price3+tax1+tax2+tax3)

# 9
#display the grade and PASS or FAIL
mark = int(input("Enter the number:"))
if (00<= mark < 30):
    print("student is fail ,grde D-")
elif(30<=mark<35):
    print("student is fail ,grde D ")
elif (35<=mark<40):
    print("student is fail ,grde D+ ")
elif (40<=mark<45):
    print("student is Fail ,grde c-")
elif(45<=mark<50):
    print("student is pass,grde c ")
elif (50<=mark<55):
    print("student is pass pass ,grde C+")
elif(55<=mark<60):
    print("student is pass ,grde B- ")
elif(60<=mark<65):
    print("student is pass ,grde B")
elif(65<=mark<75):
    print("student is ,grde B+ ")
elif(75<=mark<80):
    print("student is ,grde A- ")
elif(80<=mark<90):
    print("student is ,grde A ")
elif(90<=mark<=100):
    print("student is ,grde A+ ")

# 10
# pattern
for i in range(1,6):
    print(' '*(5-i))
    for j in range(1,i+1):
        print(i,end=' ')
    print()    

# 11
a=int(input("Enter co-efficient of x^2: "))
b=int(input("Enter co-efficient of x: "))
c=int(input("Enter the constant value: "))

D=(b**2)-(4*a*c)
x1=((-b)+D)/(2*a)
x2=((-b)-D)/(2*a)

print(f"{x1} and {x2} are roots of given equation")

# 12
a = int(input("Enter the lenght of side a:"))
b = int(input("Enter the lenght of side b:"))
c = int(input("Enter the lenght of side c:"))
if  (a == b and b==c):
    print("teiangle is equilateal")
elif (a==b and b!=c):
    print("teiangle is isoseles.")
elif (a != b and b==c):
    print("teiangle is isoseles.")
elif (a != c and b==c):
    print("teiangle is isoseles.")


elif (a!=b and b!=c):
    print("teiangle is scalene")