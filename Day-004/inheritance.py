# Create Person class
class Person:
    _name = ''
    _birthDate = 0
    _year = 2020

    # Define init function
    def __init__(self, name, birthDate):
        self._name = name
        self._birthDate = birthDate
        print(self._name, "constructed.")

    # Define getAge function to calculate age from birth date
    def getAge(self):
        return self._year - self._birthDate

    # Define setYear function to change current year
    def setYear(self, year):
        self._year = year

# Create Student class with Person inheritance
class Student(Person):
    _grade = 0

    def getGrade(self):
        return self._grade

    def setGrade(self, grade):
        self._grade = grade

# Define sam
sam = Student('Sam', 1990)

# Print
print(sam._name, 'is', sam.getAge(), 'years old.')
sam.setGrade(3)
print('Grade:', sam._grade)

sam.setYear(2030)
print(sam._name, 'is', sam.getAge(), 'years old.')