'''
Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

For example:

largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231
'''

def largest(nums):
    max = 0
    for num in nums:
        if(num>max):
            max=num
    print(max)

list = input("write a list of numbers separated by space: ")

number_list = []
for num in list.split():
    number_list.append(int(num))
# print(number_list)

largest(number_list)