'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''

import re
def square_digits(num):
    res = ''
    for d in re.findall('[0-9]', str(num)):
        d = str(int(d)**2)
        res += d
    return int(res)
