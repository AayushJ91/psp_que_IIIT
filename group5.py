# q1 done in grp3 q

# q2
def printing_nums(num1,num2):
    for i in range(num1, num2):
        print(i)

# q3
def each_char(word):
    print(len(word))
    for i in (0, len(word)):
        print(word[i])

# q4 done in grp 3 q3

# q5 
def sum_of_squares(a,b):
    add = 0
    for i in range (a, b+1):
        if i**(0.5)%1 == 0:
            add = add + i
    return add

# 6 done in grp3 8

# 7 done in grp3 9

# 8
def less_than_999(inp):
    if inp > 999:
        return "The number is greater than 3 digit number"
    else:
        return inp

# 9
def cubes(num1,num2):
    for i in range (num1, num2+1):
        if i**(1/3) % 10 == 0:
            print(i)

# 11
def div_check(num1, num2, checkor):
    for i in range (num1, num2+1):
        if i%checkor == 0:
            print(i)

# 12 done in grp3 15

# 13
def armstrong_in_range(num1, num2):
    num = 0
    for i in range(num1, num2):
        str_i = str(i)
        digi = len(str(i))
        for j in range (0, digi):
            x = (int(str_i[j]))**(digi)
            num =+ x
        if i == num:
            print(i)

# 14
def counting_words(sen):
    words = 1
    for i in sen:
        if i == " ":
            words = words + 1
    return words

# 15 done in grp3 19

# 16 done in grp3 20

# 17 done in grp3 21

# 18
def greatest_of_4(a,b,c,d):
    if a > b:
        if a > c:
            if a > d:
                print(f"{a}is gretaest")
            else:
                pass
        else:
            pass
    elif b > c:
        if b > d:
            print(f"{b} is the largest number")
        else:
            pass
    elif c > d:
        print(f"{c} is the largest number")
    else:
        print(f"{d} is the largest number")

# 19
def pass_or_fail(sub1, sub2, sub3):
    if sub1 > 33 and sub2 > 33 and sub3 > 33 and (sub1 + sub2 + sub3 == 120):
        return "the student is passed"
    else:
        return "the student is failed"

# 20
def spam_comments(comment):
    # pure_sen = comment.remove(",")
    list_words = comment.split(" ")
    for i in range(0, len(list_words)):
        if (list_words[i] == "make") and (list_words[i+1] == "a") and (list_words[i+2] == "lot") and (list_words[i+3] == "of") and (list_words[i+4] == "money"):
            return "It is a spam comment"
        elif (list_words[i] == "buy") and (list_words[i+1] == "now"):
            return "It is a spam comment"
        elif (list_words[i] == "subscribe") and (list_words[i+1] == "this"):
            return "It is a spam comment"
        elif (list_words[i] == "click") and (list_words[i+1] == "this"):
            return "It is a spam comment"

# 21
def less_than_10(inp):
    if len(inp) < 10:
        return True
    else:
        return False

# 22
def name_checking(list,name):
    for i in range(0,len(list)):
        if list[i] == name:
            return True

# 23
def post_on_harry(post):
    list_post = post.split(" ")
    for i in list_post:
        if i == "harry":
            return "It is about Harry"

# 24
def square_root(num):
    sqr_root = num**(0.5)
    return sqr_root

# 25
def longest_prefix(comment):
    list_comm = list(comment)
    stri = list_comm[0]
    for i in range(0, len(list_comm)):
        if list_comm[i] == list_comm[i+1]:
            stri = stri + list_comm[i]
        elif list_comm[i] != list_comm[i+1]:
            break
    print(f"the largest prefix is {stri}")

# 26
def int_as_array(num):
    str_num = str(num)
    list_num = list(str_num)
    rev_lis = list_num[::-1]
    for i in range (0, len(rev_lis)):
        rev_lis[i] = str(int(rev_lis[i])+1)
        if rev_lis[i] == "9":
            rev_lis[i] == "0"
            rev_lis[i+1] = str(int())
# 28
def removing_ith(word,i):
    list_word = list(word)
    list_word.remove(list_word[i-1])
    return list_word

# 29
def len_str(stri):
    leng = len(stri)
    return leng

# 30
def len_str_no_space(stri):
    list_stri = list(stri)
    stri = stri.replace(" ","")
    # leng = len(no_space)
    return stri

# 31
def even_words(sent):
    list_sent = sent.split(" ")
    for i in range (0, len(list_sent)):
        if i%2 == 0:
            print(list_sent[i])
        else:
            pass

# 32
def half_up_half_down(stri):
    len_stri= len(stri)
    if len_stri%2 ==0:
        half = len_stri/2
    else:
        half = (len_stri+1)/2
    half2 = int(half)
    stri_list = stri.split("u")
    return stri_list
print(half_up_half_down("aayush"))