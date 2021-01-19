class Student:
    """ short class that creates a student object. 
        done in oop class on Jan 19th 2021

    """

    def __init__(self, firstname, lastname, id, programofstudy):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.programofstudy = programofstudy 

    def complain(self):
        print("oh man not another assignment")

    def __str__(self):
        return f"{self.firstname} {self.lastname} \nStudent Number: {self.id} \nProgram: {self.programofstudy}"

class Course:
    """ creating courses for students

    """

    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

keet = Student("Keith", "Rogers", 201030756, "Computational Mathematics")
course = Course("OOP", 2)
course.add_student(keet)

print(course.students[0].firstname, course.students[0].lastname)
