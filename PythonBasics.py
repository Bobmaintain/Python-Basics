# Python Basics
"""
Operators in Python:
1.  Arithmetic Operators
2. Assignment Operator
3.Comparison Operator
4.Logical Operators
5. Bitwise Operators
6. Identity Operator
7. Membership Operator
"""

# Arithmetic Operators
num1 = 10
num2 = 10

print(num1 + num2)

print("Num1 + Num2 = ", num1 + num2)
print("Num1 - Num2 = ", num1 - num2)
print("Num1 * Num2 = ", num1 * num2)
print("Num1 / Num2 = ", num1 / num2)
print("Num1 // Num2 = ", num1 // num2)

print("5^3 = ", 5**3)
print("20 % 3 = ", 20 % 3)              # Modulus
print("print 22//7 =", 22//7)           # float division


# Assignment Operator
num3 = num1 + num2
print(num3)

num3 += num2
print(num3)


# Comparison Operator
# the output of the assignment operator is always a boolean value

print("Is num1 > num2 = ", num3 > num2)
print("Is num1 == num2 = ", num2 == num3)
print("Is num1 == num2 = ", num1 * num2)
print("Is num1 != num2 = ", num1 != num2)
print("Is num1 < num2 = ", num1 < num2)


# Logical Operators
x = True
y = False

print("X and Y",  x and y)
print("X or Y", x or y)
print("not of X", not x)


# Bitwise Operators
num4 = 6         # 110
num5 = 2         # 010

print("Bitwise and =", num4 & num5)
print("Bitwise or =", num4 | num5)
print("Bitwise xor =", num4 ^ num5)

print("Num4 right shift by 2 positions = ", num4 >> 2)
print("Num5 left shift by 2 positions = ", num5 << 2)


# Identity Operator
x = 5       # True if the operands are identical (refer to the same object)
             # Not true if the operands are not identical (do not refer to the same object)


# Membership Operator
x = [1,2,3,4,5]       # True if it finds elements in the specified sequence
                      # True if it does not find elemnts in the specified sequence


# Datatypes
"""
 Datatypes in python can be divede into two:
 1. Immutable types, which are: Numbers, Strings and Tuples
 2. mutable types, which are: Lists, Dictionaries and Sets 
"""


# Strings
Sample = "Welcome to Python Tutorial"               # Double Quotes
Sample = 'Welcome to Python Tutorials'              # Single Quotes


sample = '''
            This is a                                # Single Quotes
            multi-line string
            '''
sample = """
            This is also                             # Double Qoutes
            multiline string
            """

'''
String Operations:
1. Concatenation
2. Repetition
3. Slicing
4.and Other Specific Operations
'''

string1 = "Python "
string2 = "Tutorials"

# Concatenation
print(string1 + string2)

# Repetition
print(string2*3)

# Slicing
print(string1[3:6])
print(string2[3:6])
print(string2[2:-3])

# String Specific Operations
print(string1.count('P',0,5))

print(string1.find("thon"))
print(string2.isupper())
print(string2.isalnum())
print(string2.isalpha())
print(string2.isascii())
print(string1.isdecimal())
print(string2.isprintable())
print(string2.istitle())
print(string2.isspace())
print(string2.isnumeric())


# Tuples
'''
Tuple Operations
1. Concatenation
2. Repetition
3. Slicing
4.and Other Specific Operations
'''


myTuple = ("Python", 2, 3, 4, 'Tutorial')

# Concatenation
# print(myTuple + ("Ron"))
print(myTuple + ("Ron", "Bob"))
print(myTuple)

# Repetition
print(myTuple*3)

# Slicing
print(myTuple[-5])
print(myTuple[-1])
print(myTuple[1:4])
print(myTuple[1:-5])


# List
myList = ["Hello", 5, 6, 7, 6, 7, 7, 'World']
print(myList)


# List Specific Operations
print(myList.count(7))
print(myList.count(6))
print(myList.count(5))

print(myList.copy())

print(myList.pop(5))
print(myList)

print(myList.pop(0))
print(myList)

print(myList.pop(5))
print(myList)

myList.sort()
print(myList)

myList.append("Bob")
print(myList)

myList.reverse()
print(myList)

myList.insert(6, "Nelson")
print(myList)

myList.extend([myList])
print(myList)


# Dictionary
myDict = {1:"Josh", 2:"Blue", 3:"Joy", 4:"Green"}

# Accessing Dictionary
# by key index
print(myDict[3])
print(myDict.keys())

# by get method
print(myDict.get(2))


# Dictionary Methods/Operators

print(myDict.values())

print(len(myDict))

print(myDict.items())

myDict.copy()
print(myDict)

print(myDict.get(1))

print(myDict.get(1))
print(myDict.get(2))
print(myDict.get(3))
print(myDict.get(4))
print(myDict.get(5))

myDict.pop(3)
print(myDict)

myDict.setdefault(3)
print(myDict)

myDict.update({3: 'joy', 5: 'Purple'})
print(myDict)


# Set
mySet1 = {1,2,3,4,5}
mySet2 = {'red', 'blue', 3, 'green', 'magenta'}


print(mySet1)
print(mySet2)


# Set Mwhtods
# union
print("Union = ", mySet1 | mySet2)

# intersection
print("Intersection = ", mySet1 & mySet2)

# difference
print("Difference = ", mySet1 - mySet2)
print("Difference = ", mySet2 - mySet1)


# Flow Control
'''
Conditional Statements:
1. If Statement
2. If - Else Statement
3,If - Elif - Else Statement 
4. For Loop
5. While Loop
6. Break
7. Continue
'''


# If Statement
marks = 95

if marks > 80 :
    print("Grade A")


# If- Else Statement

marks = 75
if marks > 80:
    print("Grade A")
else:
    print("Grade B")


# If - Elif - Else Statement

marks = 55
if marks > 80:
    print("Grade A")
elif marks > 60 <= 80:                  # this means: (marks > 60) and ( marks <= 80)
    print("Grade B")
elif marks > 40 <= 60:                  # this means: (marks > 40) and ( marks <= 60)
    print("Grade C")
else:
    print("Grade D")


# While Loop
# Repeats things until the loop condition is true.

num = int(input(" Enter the value of n = "))
if num <= 0:
    print("Enter a valid number")
else:
    mySum = 0
    while num > 0:
        mySum += num
        num -= 1
print(mySum)


# For Loop
# Repeats things till the given number of times is reached.

for quantity in range(99, 0, -1):
    if quantity > 1:
        print(quantity, "Bottles of beer on the wall,", quantity, "bottles of beer")
        if quantity > 2:
            suffix = str(quantity) + " bottles of beer on the wall"
        else:
            suffix = "1 bottle of bear on the wall"
    elif quantity == 1:
        print("1 bottle of bear on the wall, 1 bottle of beer")
        suffix = "No more beer on the wall"

    print("Take one down and pass it around", suffix)
    print("----")


# Break
count = 0
while True:
    print(count)
    count += 1
    if count > 10:
        break


# Continue

for x in range(20):
    if (x % 2) == 0:
        continue
    print(x)


# Functions
''' 
# Functions
There are two types of functions: 
1. Built-in functions and 
2. user defined functions.
'''

def addNum(num1, num2):
    return num1 + num2

print(addNum(10,20))


def dcMarvelCrossover(inputList):
    inputList = ["Dark Claw", "Hyena"]
    return inputList


print(dcMarvelCrossover(inputList=1))


heroVillain = ["Batman", "Wolverine", "Sabertooth"]
dcMarvelCrossover(heroVillain)
print(heroVillain)


print(dcMarvelCrossover(heroVillain))


def fibo(n):
    a = 0
    b = 1
    for x in range(n):
        a = b
        b = a + b
        print(a, '\n')
    return b


num = int(input("Please enter the value of n: "))
print(fibo(num))


# File Handling and I/O Methods
"""
File Operations in Python:
1. Opening a file.
2. Reading a file.
3. Writing in a file.
4.Closing a file.
"""
'''
# Opening a file
fileObject = open("D:\\myprojects.txt", "r")      # read only
fileObject = open("D:\\myprojects.txt", "W")      # write only
fileObject = open("D:\\myprojects.txt", "r+")      # read and write
fileObject = open("D:\\myprojects.txt", "w+")      # read and write


# Reading a file
fileObject.read()


# Writing in a file
fileObject.write("Python is fun")
fileObject.write("\nYes it is fun")
fileObject.seek(0)


# Closing a file
fileObject.close()
'''''