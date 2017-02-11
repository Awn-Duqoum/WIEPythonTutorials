# WIE Python Beginners Tutorial, Introduction to functions
# Awn Duqoum - Jan 11 2017 

# Lastly sometimes you need to run a certain chuck of code in alot of places 
# for example if you need to find the average of a list alot of times you don't 
# want to have to write it everytime. That is where functions are helpful 

def avg(someList):
	sum = 0.0 # Need to declare as a float to avoid integer division
	for number in someList:
		sum = sum + number
	if(len(someList) != 0):
		return sum/len(someList)
	else:
		return 0

# The above chuck will now return the average of a list
# To use the function we just need to call it 
shortList = [1,2,3,4]
print avg(shortList)

anotherList = [1,20,60,80]
print avg(anotherList)

# Functions can accept any number of parameters and could not return anything if 
# it is not needed