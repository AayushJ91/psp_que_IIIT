# 1 done
# 2 done
# 3 done
# 4 done
# 5 done
# 6 done
# 7
def greeting_s(names):
    for i in names:
        if i.startswith("s") == True:
            print(f"hello {i}")
        else:
            pass

# 9
def printing_patt(lines):
    for i in range(1,lines+1):
        print(f" "*(lines-i), end="")
        print("*"*i)

# 10
def multiplication_table(num):
    for i in range(1,11):
        return f"{num} * {i} = {num*i}"
    
# 11
def meter_2_feet(met):
    feet =  met*3.28
    return (f"your length in feet is {feet}")

# 12
def printing_pattern_2(lines):
    # 1
    # 12
    # 123
    # 1234
    for i in range(1, lines+1):
        for j in range(1, i+1):
            print(f"{j}", end="")
        print()

# 13
def sum_1_2_100():
    sum = 0
    n = 1
    while n < 100:
        sum = n + sum
        n= n+1
    print(sum)

# 14
def palindrome_num(num):
    rev_num = str(num)[::-1]
    if int(rev_num) == num:
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")

# 15 done
# 16 done

# 17
def dist_bet_pints(pt1,pt2):
    dist = ((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)**(0.5)
    return dist

# 18
def dig_ones(num):
    str_num = str(num)
    rev = str_num[::-1]
    ones_place = rev[0]
    return (f"{num} has {ones_place} at its ones place")

# 19
def time(hrs,min):
    sec = hrs*3600 + min*60
    return (f"there is {sec} in {hrs} hours and {min} minutes")

# 21 done
# 22
def quad(a,b,c):
    D = ((b)**2 - 4*a*c)**(0.5)
    r1 = ((b*(-1)) + D)/(2*a)
    r2 = ((b*(-1)) - D)/(2*a)
    return (f"roots are {r1} and {r2}")

# 23
def rev_num(num):
    str_num = str(num)
    rev = str_num[::-1]
    num_rev = int(rev)
    return (num_rev)

# 24
def leap_years(year):
    if year % 4 == 0 and year % 400 == 0:
        return ("a leap year")
    else:
        return ("not a leap year")

# 25
def name():
    name1 = input("enter the first name: ")
    name2 = input("enter the last name: ")
    print(f"hello {name1} {name2}")
    print("welcome to python")

# 26
def print_lower():
    upper = input("enter the character in uppercase: ")
    lower = upper.lower()
    print(lower)

# 27
def area_circle(radius):
    area = 3.14*((radius)**2)
    return area

# 28
def price(qua, val, disc, tax):
    fin_price = ((val - disc) + tax)*qua
    return fin_price

# 29
def countdown():
    i = 0
    while i < 10:
        print(10-i)
        i = i + 1