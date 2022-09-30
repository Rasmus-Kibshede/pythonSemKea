#['Hello', 'World', 'Huston', 'we', 'are', 'here'] 
#should become -> 
#['World', 'Huston', 'we', 'are']

from operator import indexOf


l = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
lr = l[1:len(l)-1]

print(lr)



# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] 
# -> 
# ['Hello', 'World']

l2 = l[:2]

print(l2)


# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] 
# -> 
# ['are', 'here']

l3 = l[-2:]

print(l3)


# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] 
# -> 
# ['are']

l4 = l[-2:-1]

print(l4)

# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] 
# -> 
# ['Hello', 'Huston', 'are']

l5 = l[::2]

print(l5)

# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] 
# -> 
# ['here', 'are', 'we', 'Huston', 'World', 'Hello']

l6 = l[::-1]

print(l6)

# ('Hello', 'World', 'Huston', 'we', 'are', 'here') 
# should become -> 
# ['World', 'Huston', 'we', 'are']

t = ('Hello', 'World', 'Huston', 'we', 'are', 'here')

t1 = list(t[1:-1])

print(t1)

# 'Hello World Huston we are here' 
# -> 
# 'World Huston we'

s = 'Hello World Huston we are here'

#Lav færdig på en dynamisk måde

s1 = s[s.find(' '):s.find('are')]
print(s1)
