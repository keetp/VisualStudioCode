class Student:


    def __init__(self, firstname, lastname, id, programofstudy):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.programofstudy = programofstudy 

    def __str__(self):
        return f"{self.firstname} {self.lastname} \nStudent Number: {self.id} \nProgram: {self.programofstudy}"


keet = Student("Keith", "Rogers", 201030756, "Computational Mathematics")

print(keet)