'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''

def get_score(word):
    res = 0
    for l in word:
        res = res + (ord(l) - 96)
    return res        

def high(x):
    max = {'st':'', 'score': 0}
    for word in x.split():
        if get_score(word) > max['score']:
            max['st'] = word
            max['score'] = get_score(word)
    return max['st']
        
