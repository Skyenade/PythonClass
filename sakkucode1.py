import math
import random
"""
numberprint = 2342343
print(numberprint)

_secondnumber = 5443

third3number = 4356

fourth_nymdwf = 343
#print(fourth_nym)
print(fourth_nymdwf)
# python is case sensitive
PRINTTHIS = 454
printhis = 333
print(PRINTTHIS)
print(printhis)

n_ = 3
_b = 3

a = 50
b = a
print(a)
print(id(a))
print(id(b))
a = 12
print(id(a))

def mul(w,s):
    print(w*s)

fnumber = int(input("enter the first number"))
snumber = int(input("enter the second number"))
choice = input("enter your choice of operation")
if choice == "add":
    print(fnumber+snumber)
elif choice == "-":
    print(fnumber-snumber)
elif choice == "*":
    mul(fnumber,snumber)

   
magicNumber = random.randint(1,100)
while True:
    guess = int(input("Guess a number between 1 to 100"))
    if guess < magicNumber:
        print("too low")
    elif guess > magicNumber:
        print("too high")
    else:
        print("congratulations, you found it")
        break

   

anynumber = 3
anyString = "sa"
anyfloat = 29.5
print(type(anyfloat))
print(type(anynumber))
print(type(anyString))
str = "i am going to write "

print(str)
str1 = ''' i can also
split and print
in multiple lines
'''
print(str1)

strtest = 'please work hard for python course otherwise you gonna fail'
print(strtest)
print(strtest[0:5])
print(strtest[7])


print(True or False)

print(True == 3)
print(False == 0)
print(True + True)
print(True)

print(None == 0)
print(None == True)
print(None == False)
a = None
b = None
print(a ==b)


def wow_function():
    num1 = 1
    num2 = 3
    addition = num1 + num2


number = wow_function()
print(number)

def try_again(num):
    if num % 3 == 0:
        return False

takenumber = try_again(37)
print(takenumber)

contains =  "cegep"
print("s" in contains)
print("c" in contains)
print(True is True)
print(None is not None)
print((10 * 2) is (4 * 5) )



for i in range(10):
    print(i, end = " ")
    if i == 7:
        break
       


i = 0
while i < 12:
    if i == 6:
        i = i + 2
        continue
    else:
        print(i + 2)
    i = i + 1



sum = 0
for anyindentiifer in numList:
    sum = sum + anyindentiifer
print(sum)


numList = [3, 5 ,63, 45, 565,45]
del numList[3]
print(numList)
max = None
for num in numList:
    if max is None or num > max:
        max = num
print(max)

"""

s = " people are bored"
for a in s:
    print(a, end = "")
