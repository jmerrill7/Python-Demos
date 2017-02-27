def letsAdd(x,y):
    addition = x + y
    return addition

print letsAdd (3,5)

someValue = 5

def letsAdd(x,y):
    addition = x + y
    someValue = 10
    return addition

print letsAdd (3,5)
print someValue

#make function called subtraction

def subtraction(x,y):
    subtract = x-y
    return subtract

print subtraction (10, 4)

def moreSubtraction (x,y,z):
    subtract = x - y - z
    return subtract

print moreSubtraction (40, 3, 11)

#make function called multiplication

def multiplication (x,y,z):
    multiply = x * y * z
    return multiply

print multiplication (45, 4, 67)

#make function called division

def division (x,y):
    divide = float(x)/float(y)
    return divide

print division (54,2)
print division (65,64)

#length function

length = len("how epic are built-in functions, eh?")

print length

#turn anything into a string

x = 23
print str(x)

''' or '''

x = 2.32
print str(x)

#float function

y = float(40)/float(7)
print y

#convert float to integer

yInt = int(y)
print yInt

#convert float and round

print round(y)
