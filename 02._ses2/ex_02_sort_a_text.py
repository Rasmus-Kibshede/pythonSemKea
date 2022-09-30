#Create a function that takes a string as a parameter and returns a list.
#The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

def sort_a_text(s):
    vocals = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']

    for element in vocals:
         if(element in s):
            s = s.replace(element, '')
    return ''.join(sorted(s))

print(sort_a_text('hello world'))

