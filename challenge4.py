'''
Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
(HINT: Review your notes on *args).

For example:
product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0
'''

def product(*args):    
    result =1
    for n in args:
        result*=n
    return result

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0