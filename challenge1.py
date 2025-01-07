'''
Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

For example:

sum_to(6)  # returns 21
sum_to(10) # returns 55

'''

def sum_to (num):
    sum=0
    n=1
    while(n<=num):
        sum+=n
        n+=1
    print(sum)

number = int(input("Write a number: "))
sum_to(number)