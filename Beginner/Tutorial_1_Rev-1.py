# WIE Python Beginners Tutorial, Introduction to variables 
# Awn Duqoum - Jan 11 2017

# In python there are 5 types of variables and or ways of defining data and the
# operations that can be performed on the data

# Numbers
a = 10;    # Integers 
b = 10.0;  # Floating Point
c = 3.14j  # Complex Numbers

# Strings 
# Note that d is equal to e
d = 'Hello World !'
e = "Hello World !"

# Lists (One of the greatest things about python)
# List entries could all be the same type 
sameTypeList  = [1,2,3,4]
sameTypeList2 = ['one',"two",'three',"four"]

# List entries could also be anything
whyPythonIsSometimesBetterThenC = [1,"alpha",3.2j,"Pie","MOARPIE"]

# A specail Read-only type of lists are called Tuples 
# A list is dynamic, it's size and content can change at any time
shortList = [1]
shortList[0] = 5

#The same cannot be dont with tuples 
shortTuple = (1)
# The line below is invaild 
# shortTuple[0] = 5

# The last type is a Dictionary, which is nothing more than a list whose index 
# could be anything 
exampleDictionary = {}
exampleDictionary['Pie'] = 'MorePie'
exampleDictionary[1] = 'LessPie'
exampleDictionary[10] = 'PiePiePie' 

# In order to only have one print statement we need to wrap our none string 
# variables # in str() which converts the variable into a string. Note we could've 
# and maybe # should've had 2 print statements and no str()
print 'a = ' + str(a)
print 'b = ' + str(b)
print 'c = ' + str(c)
print 'd = ' + d
print 'e = ' + e
print 'shortTuple = ' + str(shortTuple)
print 'sameTypeList = '+ str(sameTypeList)
print 'sameTypeList2 = ' + str(sameTypeList2)
print 'exampleDictionary = ' + str(exampleDictionary)
print 'whyPythonIsSometimesBetterThenC = ' + str(whyPythonIsSometimesBetterThenC)