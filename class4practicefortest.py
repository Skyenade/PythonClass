# identifiers are used to store a variable
# numberprint = 325
# print(numberprint)

# can't start a variable with numbers os special caracters, but you can with underscore
# 4secondnumber = 56  #not possible
# _thirdnumber = 56 #possible
# fourth_number = 152 #possible

# python is case sensitive
# number = 152
# NUMBER = 123

# check the type of the variable
# test = 234
# print(type(test))

# the reference of 50 stored by a, the memory stored, using the same memory
# a = 50
# b = a
# print(a)
# print(id(a))
# print(id(b))
# b = 100
# a = b
# print(id(b))


# calculator
# a = int(input("please enter the first number: "))
# b = int(input("please enter the second number: "))
# c = input("please input the operator: ")
# def operation(a,b,c):
#     result = 0
#     if c == "+":
#         result = a+b
#     elif c == "-":
#         result = a-b
#     elif c == "*":
#         result = a*b
#     elif c == "/":
#         result = a/b
#     return result

# op = operation(a,b,c)
# print(op)


# guess a number
# magicnumber = 79
# num = int(input("Please enter a number: "))
# while(num != magicnumber):    
#     if num > magicnumber:
#         print("The magic number is smaller than ",num)
#         num = input("Please enter a number: ")
#     elif num < magicnumber:
#         print("The magic number is bigger than ",num)
#         num = input("Please enter a number: ")

# can do it with a random number just import math

# import math
# import random
# magicnumber = random.randint(1,100) # generate a number between the assigned range
# while True:
#     guess = int(input("Guess a number between 1 and 100 "))
#     if guess < magicnumber:
#         print("The magic number is smaller than ",guess)
#     elif guess > magicnumber:
#         print("The magic number is bigger than ",guess)
#     else:
#         print("Congratulations")
#         break


# print a string in multiple lines
# str = ''' i can also
# do like
# this to print multiple lines
# '''
# print(str)

# stringtest = 'please test to print this'
# print(stringtest)
# print(stringtest[0:5]) # make it an array and print in a range
# print(stringtest[6]) # only whats on index 6
# # try to find the amount of space in a atring
# # try to find the range


# assign and operator to compare boolean values
# print( 4 == 4 )
# print(True or False) #True
# print(True and False) #False
# print(True == 3) # False 1==3
# print(False == 0) # True 0 == 0
# print(True + True) # True = 1 False = 0 1 + 1
# print(True) # True because it's a boolean
# print(None)
# print(None == 0) # False because None is nothing, zero is an integer
# print(None == True) # False
# print(None == False) # False
# a = None
# b = None
# print(a == b) #True


# what None is used for
# def wow_function():
#     num1 = 12
#     num2 = 343
#     addition = num1 + num2
#     return addition # if there's no return, it will print None

# number = wow_function()
# print(number)

# def try_again(num):
#     if num % 10 == 0:
#         return False # if there's no answer, it wil return None
    
# takenumber = try_again(37)
# print(takenumber)


#look for something inside the string
# contains = "cegep"
# print("s" in contains)  # False
# print("c" in contains)  # True
# print(True is True) # True
# print(None is not None) # False
# print((10*2) is (4*5)) # True


#
# for i in range(10):
#     print(i)

# for i in range(10):
#     print(i,end=" ")    # print and stay in the same line
#     if i == 7:
#         break


# while loop
# i = 0
# while i<10:
#     print("infinite")
#     i +=1

# while i<10:
#     if i == 6: # until it becomes 6 the code will continue
#         continue
#     i += 1
#     print(i)


# while i<20:
#     if i == 11: # until it becomes 11
#         i += 2
#         continue
#     else:
#         print(i + 2)
#     i += 1


#  sum of elements in an array
# numList = [30,5,63,45,565,45,10,12]
# sum = 0

# for a in numList:
#     sum = sum + a
# print(sum)

# maxcount = numList[0]
# for a in numList:
#     if a > maxcount:
#         maxcount = a
# print("biggest num is ",maxcount)

# mincount = numList[0]
# for a in numList:
#     if a < mincount:
#         mincount = a
# print("smallest num is ",mincount)

# oddcount = 0
# evencount = 0
# for a in numList:
#     if a % 2 == 0:
#         evencount += 1
#     elif a % 2 != 0:
#         oddcount += 1
# print("even count is ",evencount)
# print("odd count is ",oddcount)



# sort the list acending or descending
# numberlist = [12,15,90,75,22,34]
# newlist = []
# min = numberlist[0]

# for a in numberlist:
#         if a < min:
#             min = a
#             newlist[a] = min

# print(newlist)


# # delete the index of an array
# numberslist = [12,15,90,75,22,34]
# print(numberslist)
# del numberslist [3] #delete the index 3
# print(numberslist)


s = "people are bored"
for a in s:
    print(a,end=" ")

for a in s:
    if a == "o":
        del s [a]
    print(a,end=" ")

# replace the caracter
# remove the caracters
# splice the string
# armstrongnumber
# string mnipulation
# fibonacci
# while
# range
# interetion
# piramid, all the reverse options as well
# for loop


# conditional loop
# range
# for, if, else if, while
# pyramid
# neste loop 
# string manipulation, repeat, replace, find a caracter
# find the vowel length in a given string
# simple list manipulation
# prime numbers in the range
# fibonacci within the range
### def function
# while, break
# temperature conversion
# palindrome number/string
# armstrong number
# factorial function recursion
# char count, vowel count



