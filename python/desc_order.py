

'''
Your task is to make a function that can take any non-negative integer as an argument 
and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
'''


def descending_order(num):
    print(int("".join(sorted(str(num), reverse=True))))


descending_order(0)
descending_order(15)
descending_order(1234)
descending_order(5678)
