# Creating class and Objects
    # In the below examples we have created objects str1,str2,emp1 for each class
# Note:
    # The __init__() function is called automatically every time the class is being used to create a new object.
    # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

class Employees:
    def __init__(self,name,age): #Defining a class
        self.emp_name=name
        self.emp_age=age

str1=Employees("Nischala",33)
print(str1.emp_age)
print(str1.emp_name)

# Without __Str__()
class EmployeesWithoutStr:
    def __init__(self,name,age): #Defining a class
        self.emp_name=name
        self.emp_age=age

    # def __str__(self): #When the return value is String
    #     return f'{self.emp_name},{self.emp_age}'
print("\n Example for without __Str__")
str2=EmployeesWithoutStr("Nischala",33)
print(str2)

# emp1=Employees("Liliya",6)
# print(emp1.emp_name,emp1.emp_age)


# With __Str__()
class EmployeesWithStr:
    def __init__(self,name,age): #Defining a class
        self.emp_name=name
        self.emp_age=age

    def __str__(self): #When the return value is String
        return f'{self.emp_name},{self.emp_age}'
print("\n Example for with __Str__")
emp1=EmployeesWithStr("Liliya",6)
print(emp1)
print(emp1.emp_name,emp1.emp_age)

#Object Methods

class Employee:
    def __init__(self,name,age): #Defining a class
        self.emp_name=name
        self.emp_age=age

    def emp_intro(self):    #Defining the function
        print("Hello my name is "+ self.emp_name)

emp1=Employee("Nischala",33)
emp1.emp_intro() # Calling the function

# Modify Object paramaters
print("Before Modifying the parameters")
print(emp1.emp_name,emp1.emp_age)
print("After Modifying the parameters")
emp1.emp_name="Lilly"
print(emp1.emp_name,emp1.emp_age)

# # del: we can delete the objects and its properties by using 'del' Keyword
# print("Before deleting the parameter")
# print(emp1.emp_age)
# del emp1.emp_age
# print("After deleting the parameters")
# print(emp1.emp_age)

#Delete Object
print("Before deleting the object")
print(emp1.emp_age)
del emp1
print("After deleting the object")
print(emp1.emp_age)
