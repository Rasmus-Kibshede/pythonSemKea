#1. Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’]) 
#2. Sort this list by using the sorted() build in function.
#3. Sort the list in reversed order.
#4. Sort the list on the lenght of the name.
#5. Sort the list based on the last letter in the name.
#6. Sort the list with the names where the letter ‘a’ is in the name first.

#1.
l = ['Claus', 'Ib', 'Per', 'Rasmus', 'anders']
#       2       -1      -1      1       0

#2.
print('sorted list: ' + ', '.join(sorted(l)))

#3.
print('reversed sorted list: ' + ', '.join(sorted(l, reverse=True)))

#4.
print('sorted list by names length: ' + ', '.join(sorted(l, key=len)))

#5.
print('sorted list by last letter: ' + ', '.join(sorted(l, key=lambda x: x[-1])))

#6. Printer ikke rigtig rækkefølge: Claus, Rasmus, anders, Ib, Per
print('sorted list by first a: ' + ', '.join(sorted(l, key=lambda x: x.find('a'), reverse=True)))