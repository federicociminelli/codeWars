'''
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the 
two arrays have the "same" elements, with the same multiplicities. 
"Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
'''


def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    if len(array1) != len(array2):
        return False
    count = 0
    for a in array1:
        for b in array2:
            if b == a*a:
                count += 1
                array2.remove(b)
    return count == len(array1)
