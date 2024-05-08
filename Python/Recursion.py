def print_odds_rec(an_array, index=0):
# Terminates the recursion if index is invalid (not within the length of the array)
    if index >= len(an_array):
        return
# Checks if remainder of the elelment in the array does not equal 0 when divided by two (odd number)
    if an_array[index] % 2 != 0:
        print(an_array[index])
# Incrementing (+ 1) the index of the array for each repetition (recursion) till index is invalid (termination condition)
    print_odds_rec(an_array, index + 1)

# ------------------------------------------------------------------------------

def countdown(num):
    if num <= 0:
        return 0
    print(num)
    countdown(num - 1)

# ------------------------------------------------------------------------------

def factorial(n):
    if n < 0:
        print(f"Number {n} is undefined")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# ------------------------------------------------------------------------------
    
def countup(number):
    if number <= 0:
        return
    else:
        countup(number - 1)
        print(number)

def main():
# Initialize an array
    an_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Odd numbers in the array:")
# recursion acts as a for loop (printing odd nums each iteration)
    print_odds_rec(an_array)
    print('-' * 50)
    result_1 = countdown(5)
    print("Sum of numbers printed:", result_1)
    print('-' * 50)

# ------------------------------------------------------------------------------

# 100000 ---> [Previous line repeated 995 more times] | RecursionError: maximum recursion depth exceeded
    n = int(input("Enter a number of the factorial: "))
    print(f"The factorial of {n} is equal to:", factorial(n))

# ------------------------------------------------------------------------------

    num = int(input("Enter a value for num: "))
    countdown(num)

# ------------------------------------------------------------------------------

    number = int(input("Enter a number: "))
    countup(number)

main()