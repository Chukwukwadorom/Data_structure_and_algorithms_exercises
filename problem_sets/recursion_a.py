"""
power
Write a function called power which accepts a base and an exponent.
 The function should return the power of the base to the exponent. 
This function should mimic the functionality of Math.pow()
- do not worry about negative bases and exponents.
"""

def my_power(base, exp):
    if exp == 0:
        return 1
    # if exp == 1:
    #     return base ## redundant

    new_exp = exp - 1
    
    return base * my_power(base, new_exp)


print(my_power(3,1))

"""
factorial
Write a function factorial which accepts a number and returns the factorial of that number. 
A factorial is the product of an integer and all the integers below it; e.g., 
factorial four ( 4! ) is equal to 24, because 4 * 3 * 2 * 1 equals 24.  factorial zero (0!) is always 1.
"""

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    m = n - 1
    return n * factorial(m)


print(".............................factorial..............................................")
print(factorial(4))



"""
productOfArray
Write a function called productOfArray which takes in an array of numbers and returns the product of them all.
"""

print(".........................................productOfArray....................................")


def product_of_array(lst:list):
    if len(lst) == 1:
        return lst[-1]
    
    return lst[-1] * product_of_array(lst[:-1])


print(product_of_array([1,2,3]))
print(product_of_array([1,2,3,10])) 




"""
recursiveRange
Write a function called recursiveRange which accepts a number and adds up all the numbers 
from 0 to the number passed to the function
"""
print(".........................................recursiveRange....................................")

def recursive_range(n):
    if n == 0:
        return 0
    
    m = n-1
    return n + recursive_range(m)

print(recursive_range(6))
print(recursive_range(10))


"""
fib
Write a recursive function called fib which accepts a number and returns the nth number in the Fibonacci sequence. 
Recall that the Fibonacci sequence is the sequence of whole numbers 1, 1, 2, 3, 5, 8, 
... which starts with 1 and 1, and where every number thereafter is equal to the sum of the previous two numbers.
// fib(4) // 3
// fib(10) // 55
// fib(28) // 317811
// fib(35) // 9227465
"""

print(".........................................Fibonacci.......................................................")

def fib(n):
    lst  = [1,1]

    def helper(n):
        if n == len(lst):
            return 
        
        new_num = lst[-1] + lst[-2]
        lst.append(new_num)
        helper(n)

    helper(n)

    return lst, lst[-1]


print(fib(4))
print(fib(10))
print(fib(28))
print(fib(35))


print(".........................................Fibonacci b....................................................")

def fibb(n):
    if n <= 2: return 1
    return fibb(n-1) + fibb(n-2)

print(fibb(4))
print(fibb(10))
print(fibb(28))
print(fibb(35))