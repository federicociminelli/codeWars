

'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!
It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.
'''


# Funzionano entrambe ma non sono abbsatanza efficienti e performanti :(

def find_uniq(arr):
    return [elem for elem in arr if arr.count(elem) == 1][0]


def find_uniq1(arr):
    for e in arr:
        if arr.count(e) == 1:
            return e


find_uniq([0, 0, 0.55, 0, 0])
find_uniq([1, 1, 1, 2, 1, 1])
find_uniq([3, 10, 3, 3, 3])
