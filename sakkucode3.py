import math
"""
print("hello world!")

num1 = 10
num2 = 20
sum = num1 + num2
print(sum)

# calculate the area of a rectangle
length = 5
width = 4
area = length * width
print(area)

# find the maximum of two numbers
num1 = 556
num2 = 3243
maximum = max(num2, num1) # max is the inbuild function to calculate the max of two numbers
print(maximum)

# calculate the square of a number
num = 4
square = num ** 2 # ** represents the exponential
print("Square of the given number is : ", square)

# average of three numbers
n1 = 34
n2 = 3545
n3 = 31
avg = (n1 + n2 + n3) / 3
print(avg)
avg1 = (n1 + n2 + n3) // 3
print(avg1)

# calculate the simple interest
principal = 1000000
rate = 1 # 5%
time = 1
interest = (principal * rate * time) / 100
print(interest)

# check a number is odd
num = 44
if num % 2 == 0:
    print("even")
else :
    print("odd")

# square root of a number
num = 64
square_root = math.sqrt(num)
print(square_root)

# swapping two numbers
firstnumber = 12
secondnumber = 445
print("before swapping - num1 :", firstnumber, "num2 : ", secondnumber)
firstnumber, secondnumber = secondnumber, firstnumber
print("after swapping - num1 :", firstnumber, "num2 : ", secondnumber)

# multiplication table
num = 7
for i in range (1, 11):
    result = i * num
    print(f"{num} X {i} = {result}")

# max of three numbers
n1 = 34
n2 = 342
n3 = 1000
maximum = max(n1,n2,n3) # i am using the max function
print(maximum)

# max of three numbers without using the max function
a = 232
b = 22000
c = 231
if a > b and a > c:
   largest = a
if b > a and b > c:
   largest = b
if c > b and c > a:
   largest = c

print(largest)

# count the number of words in  a sentence
text = " I am going to find the count words"
words = text.split()
count = len(words)
print(count)


# count the number of given character in a sentence
text = " I am going to find the count words ooooe e a a"
vowels = "aeiou"
counta = 0
counte = 0
for i in text:
    if i =='a':
        counta= counta + 1
    if i == 'e':
        counte = counte + 1


print(counta)
print(counte)

# print the half pyramid
"""
k = 1
for i in range (5):

    for j in range(i + 1):
        print(k, end = " ")
        k = k + 1
   
    print("\n")

text = "sakku"
reverse = ""
for i in text:
    reverse = i + reverse
print(reverse)

# another formal way of reversing a string

s = "LearnPython"
reverseString = []
index = len(s)
while index > 0 :
    reverseString +=  s[ index - 1 ]
    index = index - 1
print(listToString(reverseString))
