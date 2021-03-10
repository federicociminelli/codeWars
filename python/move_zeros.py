'''
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.
'''


def move_zeros(array):
    if len(array) == 0:
        return []
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(0)
    return array
