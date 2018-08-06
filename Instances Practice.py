class Employee():
    raise_amount = 1.04
    
    def __init__(self, first, last, job, pay):
        self.first = first
        self.last = last
        self.job = job
        self.pay = pay

    def statement(self):
        return(self.first + " " + self.last + " is a " + self.job +
               " that makes " + str(self.pay) + " annually")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return(self.pay)
                    
#Instances of the class employee
emp1 = Employee("Farres", "Maruf", "Intern", 50000)
emp2 = Employee("Hunter", "Phillips", "Head Data Scientist", 100000)

print(emp1.statement())
print(emp2.statement())

emp1.raise_amount = 1.1
emp1.apply_raise()
emp2.apply_raise()

print(emp1.statement())
print(emp2.statement())
