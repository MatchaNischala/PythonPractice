class Employees:
    def __init__(self,name,age):
        self.emp_name=name
        self.emp_age=age

    def __str__(self):
        return f'{self.emp_name},{self.emp_age}'
str1=Employees("Nischala",33)
print(str1)
emp1=Employees("Liliya",6)
print(emp1.emp_name,emp1.emp_age)


