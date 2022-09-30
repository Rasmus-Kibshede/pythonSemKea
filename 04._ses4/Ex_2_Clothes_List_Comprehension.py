
# 1.) From 2 lists, using a list comprehension, create a list containing:
# [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

shirts = [(i, j) for i in colors for j in sizes]

print(shirts)


# 2.) If the tuple pair is in the following list, it should not be added to the comprehension generated list.
soled_out = [('Black', 'm'), ('White', 's')]

print([i for i in shirts if i not in soled_out])


