'''class Employee:
    salary = 90
    name = "junaid"

    def getsalary(self):
        return self.salary()


junaid = Employee()
print(junaid.salary)
print(junaid.name)'''


# Using Constructor

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getsalary(self):
        '''return self.name
        return self.salary'''
        print(self.salary)

malik = Employee("malik", "1000")
'''print(malik.name)
print(malik.salary)'''
malik.getsalary()

idrees = Employee("idrees", "1200")
'''print(idrees.name)
print(idrees.salary)'''
idrees.getsalary()