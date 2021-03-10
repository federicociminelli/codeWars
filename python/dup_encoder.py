

'''
The goal of this exercise is to convert a string to a new string where each character 
in the new string is "(" if that character appears only once in the original string, 
or ")" if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.
'''

#! non funziona come doverbbe


def duplicate_encode(word):
    res = ""
    for c in word.lower():
        if word.count(c) > 1:
            res += ")"
        else:
            res += "("
    print(res)


duplicate_encode("din")
duplicate_encode("recede")
duplicate_encode("Success")
duplicate_encode("(( @")