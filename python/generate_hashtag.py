'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''


def generate_hashtag(s):
    if len(s) == 0:
        return False
    s = s.title().replace(" ", "")
    if s.count("#") == 0:
        s = "#" + s
    return s if len(s) < 140 else False


print(generate_hashtag("ciao"))
print(generate_hashtag("    ciao      "))
print(generate_hashtag("#ciao"))
print(generate_hashtag("ciao come va"))
print(generate_hashtag("Ciao Come Va"))
print(generate_hashtag("Ciao come va"))
print(generate_hashtag("c i a o"))
print(generate_hashtag(""))
print(generate_hashtag("Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat"))
