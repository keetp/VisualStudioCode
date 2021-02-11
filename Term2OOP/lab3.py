class Person:
    """Person class. creates an object of a person with a first, last name and age.
    
    attributes: first_name, last_name, age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Full Name: {self.first_name} {self.last_name}, Age: {self.age}'

# Employee class with Person parent class
# attributes: employee_number, position, salary
class Employee(Person):

    def __init__(self, first_name, last_name, age, employee_number, position, salary):
        super().__init__(first_name, last_name, age)
        self.employee_number = employee_number
        self.position = position
        self.salary = salary

    def __str__(self):
        return super().__str__() + f' Employee #: {self.employee_number}, Position: {self.position},' \
                                   f' Salary: ${self.salary} annually'

    # increases salary by an inputted amount
    def raise_amt(self, int):
        self.salary += int

    # changes position to the inputted string
    def change_position(self, str):
        self.position = str

# Student class with Person parent class
# attributes: student_number, current_courses
class Student(Person):
    def __init__(self, first_name, last_name, age, student_number, current_courses):
        super().__init__(first_name, last_name, age)
        self.student_number = student_number
        self.current_courses = current_courses

    # didn't like the ugly parentheses around the list so I worked around it
    def __str__(self):
        courses = ''
        for i in range(len(self.current_courses)):
            courses += self.current_courses[i] + '; '
        return super().__str__() + f' Student #: {self.student_number}, Enrolled Courses: ' + courses

    # drops a course
    def drop_course(self, str):
        self.current_courses.remove(str)

    # adds a course
    def add_course(self, str):
        self.current_courses.append(str)


# test inputs/print statements

p = Employee('Keith', 'Rogers', 25, 201030756, 'CEO', 25000)
p1 = Student('Keith', 'Rogers', 25, 201030756, ['Math', 'Biology'])

print(p1)

p1.drop_course('Math')

print(p1)

p1.add_course('Sociology')

print(p1)