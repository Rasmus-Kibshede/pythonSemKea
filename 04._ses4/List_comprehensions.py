
l = []

for i in range(10):
    l.append(i)

print(l)

# Det samme som ovenover
print([i for i in range(10)])


def last(x):
    return x[-1]

print([last(i) for i in ['hello', 'world']])




color = ['♠', '♥', '♦', '♣']

face = [i+1 for i in range(13)]

deck = [(c,f) for c in color for f in face]

print(deck)



