import math
"""
is_true = True
n = 34567
for i in range(2, n):
    if (n % i) == 0:
        is_true = False
        break
   

if is_true:
    print("prime")
else:
    print("Not prime")

# PRACTIcing functions


def is_even(num):
    if num % 2 == 0:
     return True
    else:
     return False
result = is_even(4)
print(result)
result = is_even(7)
print(result)

def area_of_circle(radius):
   return math.pi * (radius ** 2)
area = area_of_circle(5)
print(area)

def sum_of_numbers(n, n1, n2):
   return n + n1 + n2
a = int(input("enter the first "))
g = int(input("enter the second "))
z = int(input("enter the thrid "))
sum = sum_of_numbers(a,g,z)
print(sum)

# define a function to calculate the factorial of any given number
def factorial(number):
   if number == 0:
      return 1
   else:
      return number * factorial(number - 1)
   
any_number = int(input("Enter a number"))
factorial = factorial(any_number)
print(factorial)

def fibonnaci_series(series):
    firstnumber = 0
    secondnumber = 1
    print(firstnumber)
    print(secondnumber)
    for i in range(2, series):
        thirdnumber = firstnumber + secondnumber
        print(thirdnumber)
        firstnumber = secondnumber
        secondnumber = thirdnumber


n = 15
fibonnaci_series(n)

def printme(message, n):
    for i in range(n):
        print(f"{message} is {i + 1} times")
printme("hello", 10)


def reverseString(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1

originalString = "Wednesday"
print("the reversed string is ", reverseString(originalString))

origin = "hello"
reverse = ""
count = len(origin)
while count > 0:
    reverse = reverse + origin[count - 1]
    count = count - 1

print(reverse)


# Utopian tree problem
def Utopian_tree_height(num):
    height = 1
    for cycle in range(1, num + 1):
        if cycle % 2 == 1:
            height = height * 2
        else:
            height = height + 1
    return height


n = int (input("enter the number of cycles"))
resulting_height = Utopian_tree_height(n)
print(f" The height of utopian tree after {n} cycles is {resulting_height}")


# find and print the largest of  N numbers

n = int (input("enter the number of series you want to compute"))
largest = None

for i in range(n):
    num = int(input("enter the nummbers "))
    if largest is None or num > largest:
        largest = num

print(largest)
"""
# Program to count the given number
target_number = int(input("enter the target number to be counted : "))
#initialize the count
count = 0
while True:
    user_input = input("Enter a number or ('q' to quit)")
    if user_input == 'q':
        break
    else:
        number = int(user_input)
        if number == target_number:
            count = count + 1
print(f"the number {target_number} appears {count} times ")
