s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'

#1. Count the number of characters including blank spaces.
#2. Count the number of characters excluding blank spaces.
#3. Count the number of words

count = len(s)

print(count)

count = len(s.replace(" ", ""))

print(count)