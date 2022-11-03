import random

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def randomStudent(index):
    return {
        'id': index,
        'name': names[random.randint(0, len(names)-1)],
        'major': majors[random.randint(0, len(majors)-1)]
    }


def students_list(num_students):
    listOfStudents = []
    for i in range(num_students):
        listOfStudents.append(randomStudent(i))
    return listOfStudents


def students_generator(num_students):
    for i in range(num_students):
        yield randomStudent(i)


#people = students_list(10)
# print(people)

people = students_generator(2)

for p in people:
    print(p)
    print()
