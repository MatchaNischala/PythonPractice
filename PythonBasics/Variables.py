# Variables are the containers to store the value

 # Creating Variables

    # Ex1:
x=5
y=6
print(x,y)

    # Ex2: No need to declare the data type of the variable
    # int x= 4 / string x ="Lilly"
x="Lilly"
print(x)

 #Casting : if you want to specify the data type of the variable
x=int(4)
y=str("Lilly")
z=str(1234)
a=float(2.3)
print(x, y, z, a)

 #Type - gives the type of the variable

name= "Lilly"
age=6
print("Name and age of the child: ")
print(name,age)
print( type(name), type(age))


 # Variables are case-sensitive
    #Strings can be given in ''/""

name='Lilly'
Name= "Meenu"
print(name,Name)

 #Varaible Names: Naming convention types

     #Valid
mynum=23
_mynum=24
my_num=25

    #Invalid
     #2mynum, my my_num, y-num

    # Types of naming conventions
    #   Camel case - mynum
    #   Pascal case - MyNum
    #   Snake case - my_num

 #Many values to Mutiple variables

x,y,z='mango','lilly','grapes'
print(z)

 #One value to multiple variables
b = c = "lilly"
print(b,c)

 #Unpack a collection
fruits=['grapes','mango','kiwis']
a,b,c=fruits
print(b)

 # Global Variables: when we create a variable outside a function is considered as Global variable,
 # even if we want to mention the variable inside the function as global we need to use a key word 'Global'
print("\nExample1 for Global Variables: ")

 #Ex1: Variable outside the Function
x="Programming Language" #Global varaible
def myfunc():
    print("Python is a "+ x)

myfunc()

#Ex2:  variable name inside the function same as global variable

print("\nExample2 for Global Variables: ")
x='fantastic'
def myfunc():
    x='programming language'
    print("python is a "+x)

myfunc()
print("python is a "+x)

 #Ex3: Variable inside the function using "Global" keyword

print("\nExample3 for Global Variables: ")
x='fantastic'
def myfunc():
    global x
    x='programming language'
    print("python is a "+x)

myfunc()
print("python is a "+x)







