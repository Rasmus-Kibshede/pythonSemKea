
# 1.) Create a list of capital letters in the english alphabet
print('list of capital letters')
print([chr(i) for i in range(65, 91)])


# 2.) Create a list of capital letter from the english aplhabet, 
# but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
print('exclude 70, 75, 80, 85')
print([chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85]])

# 3.) Create a list of capital letter from from the english aplhabet, but exclude every second between F & O
print('exclude every second between F & O')
#print([chr(i) for i in range(65, 91) if i not in range(71, 79, 2)])

print([chr(i) if i not in range(71, 79, 2) else '-' for i in range(65, 91)])
