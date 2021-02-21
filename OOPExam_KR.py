class Employee:
    ''' Employee class

    attributes: fname, lname, employee_id
    '''
    def __init__(self, fname, lname, employee_id):
        self.fname = fname
        self.lname=lname
        self.employee_id = employee_id

    def __str__(self):
        return f'Employee: {self.fname} {self.lname} ({self.employee_id})'

class WageEmployee(Employee):
    '''WageEmployee class with Employee parent class

    attributes: hourly_wage, weekly_hours
    '''

    def __init__(self, fname, lname, employee_id, hourly_wage, weekly_hours):
        super().__init__(fname, lname, employee_id)
        self.hourly_wage = hourly_wage
        self.weekly_hours = weekly_hours

    # calculates weekly earnings and returns to 2 decimal places
    def weekly_earnings(self):
        weekly_earnings = self.hourly_wage * self.weekly_hours
        return format(weekly_earnings, '.2f')

    def __str__(self):
        return 'Wage' + super().__str__() + f' WEEKLY EARNINGS: ${self.weekly_earnings()}'

class SalaryEmployee(Employee):
    ''' SalaryEmployee class with Employee parent class

    attributes: yearly_salary
    '''

    def __init__(self, fname, lname, employee_id, yearly_salary):
        super().__init__(fname, lname, employee_id)
        self.yearly_salary = yearly_salary

    # calculates weekly earnings and returns to 2 decimal places
    def weekly_earnings(self):
        weekly_earnings = self.yearly_salary / 52
        return format(weekly_earnings, '.2f')

    def __str__(self):
        return 'Salary' + super().__str__() + f' WEEKLY EARNINGS: ${self.weekly_earnings()}'

# instantiations and test print statements
e1 = Employee('Ronnie', 'McDonnie', 200117240)
e2 = WageEmployee('Johnny', 'McDonnie', 200117240, 31.95, 42)
e3 = SalaryEmployee('Donnie', 'McDonnie', 200117240, 50000)
print(e1)
print(e2)
print(e3)