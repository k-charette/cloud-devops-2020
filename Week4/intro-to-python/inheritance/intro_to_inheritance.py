#   Intro to Inheritance in Python

# Syntax for inheriting a class

class ParentClass:
    pass


class ChildClass(ParentClass):
    pass


# ChildClass is inheriting the functionality of ParentClass


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def __init__(self, first_name, last_name, course, enrolled):
        self.course = course
        self.enrolled = enrolled
        self.graduated = False
        super().__init__(first_name, last_name)


student_one = Student("Max", "Power", 'Intro to Python', True)
print("{} {} is a student taking the {} course. ".format(student_one.first_name, student_one.last_name, student_one.course))
