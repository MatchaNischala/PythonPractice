# Inheritance: Allows us to inherit all the methods and properties from a Parent Class to Child class
# from socket import send_fds


#We can inherit the methods and properties in 3 ways without mentioning any properties in child class
      # 1. By using 'Pass' keyword,it inherits the parent class properties or methods,
      #      when you do not want to add any other properties or methods to the class.
      # 2. By calling Parent's __init__() function
      # 3. By using 'Super' function,which will make the child class inherit all the methods and properties from its parent
#We can inherit the methods of parents class and defining properties in child class init() function / over riding the parents init() function
# Examples:


class Employees: # class creation
    def __init__(self,name,age): # Defining the properties
        self.emp_name=name
        self.emp_age=age
    def emp_info(self): # Function/Method definition in Parent class
        print(" Method From Parent class")
        print(f" Employee details: "+self.emp_name,self.emp_age)

employee=Employees("Liliya",6) # Creating object 'emp1'
print(employee.emp_name,employee.emp_age)

#Creating Child class and inheriting the Parent properties
class emp(Employees):
# 1. By using 'Pass' keyword:
 pass
print("Example for Pass keyword")
print("\n In CHILD CLASS")
emp1=emp("Meenu",6)
emp1.emp_info()

# 2. By calling Parent's __init__() function
print("\n Example for Parent's init function")
class emp(Employees):
    def __init__(self,name,age):
        Employees.__init__(self,name,age)
emp2=emp("Nischala",33)
emp2.emp_info()

# 3. By using 'Super' function
print("\n Example for Super function")
class Emp(Employees):
    def __init__(self,name,age):
        super().__init__(name,age)
emp3=emp("Angelina",33)
emp3.emp_info()

#
class Employees: # class creation
    def __init__(self,name,age): # Defining the properties
        self.emp_name=name
        self.emp_age=age
    def emp_info(self): # Function/Method definition in Parent class
        print(" Method From Parent class")
        print(f" Employee details: "+self.emp_name,self.emp_age)


class Employee(Employees): # Created'Employee' child class,which inherits from 'Employees' parent class
    def __init__(self, name, age,gender):
        super().__init__(name, age)
        self.gender=gender
emp3=Employee("Victor",33,"Male")
print("Employee gender:"+emp3.gender)
emp3.emp_info()




