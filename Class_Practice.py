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


keet = Student("Keith", "Rogers", 201030756, "Computational Mathematics")

print(keet)
keet.complain()
