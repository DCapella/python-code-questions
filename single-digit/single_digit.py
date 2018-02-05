"""
The goal of this Kata is to reduce the passed integer to a single digit
(if not already) by converting the number to binary, taking the sum of the
binary digits, and if that sum is not a single digit then repeat the process.

n will be an integer such that 0 < n < 10^20
If the passed integer is already a single digit there is no need to reduce
"""

def single_digit(n):
    if len(str(n)) == 1: return n

    result_binary = '{0:08b}'.format(n)
    result_list = map(int, str(result_binary))
    result_sum = sum(result_list)

    return single_digit(result_sum)
