class Student:

    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.capitalize()

    def __add__(self, student):
        return Student('Anna the daugther', 1234)

    def __str__(self):
        return f'{self.name}, {self.cpr}'

    def __repr__(self):
        return f'{self.__dict__}'


class PythonStudents:
    def __init__(self, studentList):
        self.index = 0
        self.studentList = studentList

    def __call__(self):
        return iter(self)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.studentList):
            raise StopIteration
        else:
            student = self.studentList[self.index]
            self.index = + 1
            return student


student1 = Student("Rasmus", 12345678)
student2 = Student("Mic", 87654321)

pythonStudents = PythonStudents([student1, student2])

v = pythonStudents()

print(next(v))
print(next(v))
