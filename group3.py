def sum_of_evn_nums_in50():
    sum = 0
    for i in range (1,51):
        if i%2 == 0:
            sum = sum+i
    print(f"The sum of all even numbers upto 50(icluding 50 is) {sum}")

def digits_in_a_num(num):
    dig = 0
    while num>0:
        num = num//10
        dig = dig + 1
    print(f"The digits in the given number is {dig}")

def sums_for_evenno_btw_1(n):
    sum = 0
    for i in range (1, n+1):
        if i%2 == 0:
            sum = sum + i
    print(f"sum of all even numbers till {n} is {sum}")

def sum_of_digits(num):
    y = num
    sum = 0
    while num>0:
        x = num%10
        num = num//10
        sum = sum+x
    print(f"the sum of digits of {y} is {sum}")

def printing_prime_nos(num):
    for i in range (2,num+1):
        for j in range (2,i):
            if i%j != 0:
                break
                print(i)

def sum_of_squares(num):
    sum = 0
    for i in range (1,num+1):
        sum = sum + (i**2)
    print(f"The sum of squares of all numbers upto {num} is {sum}")

def div_by_3_5(num):
    if (num%3 == 0) and (num%5 == 0):
        print(f"{num} is divisible by both 3 and 5")
    else:
        print(f"{num} is not divisible by both 3 and 5")

def GCD(a,b):
    gcd = 0
    if a > b:
        for i in range (1,b+1):
            if (a%i == 0) and (b%i == 0):
                gcd = i
    else:
        for i in range (1, a+1):
            if (a%i == 0) and (b%i == 0):
                gcd = i
    print(f"the GCD of {a}, {b} is {gcd}")

def perfect_sq(n1,n2):
    checker = 0
    for i in range (n1, n2+1):
        checker = i**(0.5)
        if checker%1 == 0:
            print(i)

def permutation(n,r):
    