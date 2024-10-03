# We can slice a string by giving starting and ending index. to get the characters in a range
#
# txt= "range of characters"
# print(txt[3:7])
# print(txt[:11]) #Slice from start
# print(txt[5:])#slicing to the end
# print(txt[-6:-3])# Negative slicing
#
# #String Methods:
txt= "range of characters "
# print(txt.upper()) # Uppercase
# print(txt.lower())
# print(txt.strip()) # Removes extra spaces from starting and ending of the string
print(txt.replace('range','set'))
print(txt.split("e"))


# #String Concatenation
# txt1 ="Merge variable a"
# txt2=" with variable b"
# combine=txt1+txt2
# print(combine)

#Format Strings: we can combine strings and numbers by using f-strings or the format() method
num=47
txt=f"Python's strings have {num} methods"

# A modifier is included by adding a colon : followed by a legal formatting type,
# like .2f which means fixed point number with 2 decimals:

# txt1=f"Python's strings have {num:.1f} methods" #o/p: 47.0
# txt1=f"Python's strings have {num:.3f} methods" #o/p: 47.000
txt1= f"Python's strings have {20+27} methods" # Arthimetic operators can be used
print(txt1)


#Below are the builtin methods that can be used for strings

# txt= " Python has a set of built-in methods "
# print(txt.capitalize())#	Converts the first character to upper case
# print(txt.casefold())	#Converts string into lower case
# print(txt.center(15))	#Returns a centered string
# print(txt.count('o'))#	Returns the number of times a specified value occurs in a string


# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning


