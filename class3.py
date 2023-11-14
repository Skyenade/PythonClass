
#utopian tree growth after n cycles
# def Utopian_tree_height(n):
#     height = 1
#     for cycle in range(1,n+1):
#         if cycle%2 == 1:# spring cycle is odd number, check for odd, always spring 
#             height = height *2
#         else: # summer
#             height = height + 1
#     return height        

# n = int(input("How many cicles? "))
    
# resulting_height = Utopian_tree_height(n)
# print(f"The height of the utopian tree after {n} cycles is {resulting_height}")


# read 10 values from the user and print the largest number
# count = 0
# for i in range (10):
#     n = int(input("Please enter a number"))
#     if n > count:
#         count = n
# print(count)

# read 10 values from the user and print the largest number with a function
# n = int(input("Please enter de amount of numbers: "))

# def largestnumber(n):
#     count = 0
#     for i in range (10):
#         num = int(input("Please enter a number: "))
#         if num > count:
#             count = n
#     return count

# result = largestnumber(n)
# print(f"the largest number is {result}")


# find how many times a number is repeated
# n = int(input("Please enter de amount of numbers: "))
# def repeated_number(n):
#     countrepeat = 0
#     for i in range(n):
#         num = [int(input("Please input a number: "))]
#     lenght = len(num)
#     for i in range (lenght-1):
#         if num[i] == num[i+1]:
#             countrepeat = num[i]
#     return countrepeat

# result = repeated_number(n)
# print(result)


# program to count the given number
# target_number = int(input("Enter the target number to record: "))
# # initialize the count
# count = 0
# while True:
#     user_input = input("Enter a number or ('q' to quit): ")
#     if user_input == 'q':
#         break
#     else:
#         number = int(user_input)
#         if number == target_number:
#             count += 1

# print(f"the number {target_number} appers {count} times")


# # enter all the numbers that are being duplicated
# target_number = int(input("Enter the target number to record: "))
# # initialize the count
# count = 0
# while True:
#     user_input = input("Enter a number or ('q' to quit): ")
#     if user_input == 'q':
#         break
#     elif user_input == int:
#         number = int(user_input)
#         if number == target_number:
#             count += 1
#     else:
#         print("not the valid character to quit ")


# print(f"the number {target_number} appers {count} times")


