#Assigning strings to a variable

name='cognizant'
print(name)

 #Multiline Strings
para="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt, 
ut labore et dolore magna aliqua"""
print(para)


 #Looping through a string and 'Len' keyword
lang=['English','Telugu','Hindi']
size=len(lang)
for i in lang:
    print("Languages:"+i)
print("Length of the string is:")
print(size)

 #Checking for the text in the string
my_name= "Matcha Nischala"
val='Nischala'
if val in my_name:
    print("yes,it's present")
else:
    print("No, it's missing")





