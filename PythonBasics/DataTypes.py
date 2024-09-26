# DataTypes with examples

    # Text Type:	str
    # Numeric Types:	int, float, complex
    # Sequence Types:	list, tuple, range
    # Mapping Type:	dict
    # Set Types:	set, frozenset
    # Boolean Type:	bool
    # Binary Types:	bytes, bytearray, memoryview
    # None Type:	NoneType

 #TExt Tpe: using 'str' keyword
fname=str('Victor')
mname='Nischala'
dname="Lilly"
print("Family members name:"+fname, mname ,dname)

 #Numeric Type: using the keywords and without keyword

fage=33
mage=int(33)
dage=6
fhgt=5.8
mhgt=float(5.32)
dhgt=3.2
print("Age and the height of family members:")
print(fage,fhgt, mage,mhgt, dage,dhgt)

 #Sequence Types: List,Tuple, Range
 #Ex1: List
Family=["Victor","Nischala","Lilly"]
 #Ex2: Tuple
Family=("Victor","Nischala","Lilly")
 #Ex3: Range
x=range(3)

x = {"name" : "John", "age" : 36} #dict
x = {"apple", "banana", "cherry"} #set
x = frozenset({"apple", "banana", "cherry"}) #frozenset
x = True #bool
x = b"Hello" #bytes
x = bytearray(5) #bytearray
x = memoryview(bytes(5)) #memoryview
x = None #NoneType

 # Type Keyword
myname="Steffi"
myage=33
myhgt=5.4
print(type(myname),type(myage), type(myhgt))







