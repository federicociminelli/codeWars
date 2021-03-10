'''
Write a function named first_non_repeating_letter that takes a string input, and returns 
the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but 
the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None.
'''


def first_non_repeating_letter(string):
    if len(string) == 0:
        return ""
    for l in string:
        if l.isupper():
            if string.count(l.lower()) == 0 and string.count(l) == 1:
                return l
        elif l.islower():
            if string.count(l.upper()) == 0 and string.count(l) == 1:
                return l
        elif string.count(l) == 1:
            return l
    return ""


print(first_non_repeating_letter("Go hang a salami, I\'m a lasagna hog!"))
print(first_non_repeating_letter("ciao"))
print(first_non_repeating_letter("aaaaaaaaa"))
print(first_non_repeating_letter("sTreSS"))
print(first_non_repeating_letter(""))
