# 1
n = input(" enter num: ")
num = int(n)
sum = 0
digits = len(n)
print(digits)

l=[int(x) for x in n]
print(l)
for i in l:
    sum = sum + (i**digits)
print(sum)
if sum == num:
    print(f"{n} is a armstrong number.")
else:
    print(f"{n} is not a armstrong number.")

# 2
radius = float(input("Enter the radius of circle:"))
# formula = 3.14 x r**2
area = (3.14)*(radius**2)

print(area)

# 3
num1 = int(input("enter the number:"))
num2 = int(input("enter the number:"))
num3 = int(input("enter the number:"))

l = [num1,num2,num3]
l.sort()
print(l)
# decreasing order
l.sort(reverse=True)
print(l)
print(l[::-1])

# 4
char = input("Enter the character:")
#check the type of character

if 'A'<= char <= 'Z':
    print(f"{char} is a uppecase letter.")
elif 'a'<= char <='z':
    print(f"{char} is a lowercase letter.")
elif '0' <= char <= '9':
    print(f"{char} is a  digit .")
else:
    print(f"{char} is another character.")

# 5
def average(n1,n2,n3,n4,n5):
    avg = (n1 +n2+n3+n4+n5)/5
    return avg
    
# 6
string = str(input("Enter the alphabat:"))

if string in ("a","e","i","o","u","A","E","I","O","U"):
    print(f"{string} is a vowel")

else:
    print(f"{string} is a consonsnt")

# 7
x = int(input("Enter the number:"))
n = int(input("Enter the number:"))
y = 1
for i in range(0,n):
    y = y*x
print(y)

# 8
second = int(input("Enter the time in seconds:"))

mins = second/60
hours = second/(60*60)
print(mins)
print(hours)

# 9
days = int(input("enter the days"))
year  = days//365
print(f"years: {year}")

n = days%365
month = n//30

print(f"months: {month}")

day = n%30
print(f"day: {day}")

# 10
n = int(input("Enter the number:"))
if (n%5==0 and n%11==0):
    print(f"{n} divisible both 5 and 11 ")
else:
    print(f"{n} not divisible both 5 and 11 ")

# 11
n = int(input("Enter the number:"))
for i in range(1,n):
    if n%i == 0 :
        print(i,end=",")

# 12
for i in range(1,6):
    print(' '*(5-i),end=' ')
    for j in range(1,i+1):
        print(1,end=' ')
    print()

# 13
num = input("Enter:")
print(num[::-1])

# 14
for i in range(4,0,-1):
    print(' '*(4-i),end=' ')
    for j in range(4,4-i,-1):
        print(j,end=' ')
    print()

# 15
a = int(input("Enter the number:"))
b = a
c = b 
print(a)
print(b)
print(c)

# 16
angle_1 = int(input("enter the angle frist:"))
angle_2 = int(input("enter the angle second:"))
angle_3 = int(input("enter the angle thred:"))

total = angle_1+angle_2+angle_3
if total == 180:
    print("they form a triangle angle.")
else:
    print("they form not a triangle angle.")