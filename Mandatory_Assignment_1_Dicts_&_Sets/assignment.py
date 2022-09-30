
# Model an organisation of employees, management and board of directors in 3 sets.
# Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren

# Management: Tine, Trunte, Rane

# Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars


directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}

management = {'Tine', 'Trunte', 'Rane'}

employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent','Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

# who in the board of directors is not an employee?
print('who in the board of directors is not an employee?')
print(employees.difference(directors))
print()

# who in the board of directors is also an employee?
print('who in the board of directors is also an employee?')
print(directors.intersection(employees))
print()

# how many of the management is also member of the board?
print('how many of the management is also member of the board?')
print(len(management.intersection(directors)))
print()

# All members of the managent also an employee
print(management.intersection(employees))
print('All members of the managent also an employee')
print()

# All members of the management also in the board?
print(management.intersection(directors))
print('All members of the management also in the board?')
print()

# Who is an employee, member of the management, and a member of the board?
print(employees.intersection(management, directors))
print('Who is an employee, member of the management, and a member of the board?')
print()

# Who of the employee is neither a memeber or the board or management?
print('Who of the employee is neither a memeber or the board or management?')
print(employees.difference(directors, management))
print()



# 2. Using a list comprehension create a list of tuples from the folowing datastructure

print('2. Using a list comprehension create a list of tuples from the folowing datastructure')

alphabet = {'a' : 'Alpha', 'b' : 'Beta', 'g' : 'Gamma'}

tupleAlphabet = alphabet.items()

print(tupleAlphabet)



# 3. From these 2 sets:

print('3. From these 2 sets:')

set1 = {'a', 'e', 'i', 'o', 'u', 'y'}

set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}


set_union = set1.union(set2)

print('Union: ')
print(set_union)


set_symmetric_difference = set1.symmetric_difference(set2)

print('Symmetric difference: ')
print(set_symmetric_difference)


set_difference = set1.difference(set2)

print('Difference: ')
print(set_difference)

set_disjoint = set1.isdisjoint(set2)

print('Disjoint: ')
print(set_disjoint)

# 4. Date Decoder:
print('4. Date Decoder')

# 8-MAR-85

months = {
    'JAN' : 1,
    'FEB' : 2,
    'MAR' : 3,
    'APR' : 4,
    'MAY' : 5,
    'JUN' : 6,
    'JUL' : 7,
    'AUG' : 8,
    'SEP' : 9,
    'OCT' : 10,
    'NOV' : 11,
    'DEC' : 12 
}


def convert(date):
    l = date.split('-')
    month = months.get(l[1])
    return l[0] + str(month) + l[2]

print(convert('8-MAR-85'))

