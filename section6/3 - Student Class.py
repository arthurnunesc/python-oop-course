"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Student:

    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self._age = age
        self.gpa = gpa

    @property
    def age(self):
        return self._age


student_nora = Student("245AFS", "Nora Nav", 15, 3.96)

print(student_nora.age)  # Throws an error.

print(student_nora.age)  # Can be accessed but it shouldn't be accessed.
