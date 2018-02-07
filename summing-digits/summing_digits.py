"""
Write a function named sumDigits which takes a number as input and returns the
sum of the absolute value of each of the number's decimal digits.
"""

def sum_digits(number):
    numberList = [int(i) for i in str(abs(number))]
    return sum(numberList)
