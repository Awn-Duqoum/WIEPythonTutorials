# The purpose of this module is to explain how multidimensional arrays work and how they can be used

# Quick recap on arrays and lets start calling them lists because this is python now

# Lists (One of the greatest things about python)
# List entries could all be the same type 
sameTypeList  = [1,2,3,4]
sameTypeList2 = ['one',"two",'three',"four"]

# List entries could also be anything
whyPythonIsSometimesBetterThenC = [1,"alpha",3.2j,"Pie","MOARPIE"]

# While lists are useful, they can be limited if kept to only one dimension. In python there is no limit to how many dimensions a list can have

# Example of 2D list
m2D = [ [1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0] ]

# Example of using a loop to create a 2D list
m2DLoop = [ 4*[0] for i in range(3) ];

# Now image if run a test and collected 10 results, if we we wanted to sort them into an array we can do something like this 
import random

# Create an empty list
results = []

# Fill the list with random numbers
for i in range(10):
	results.append(random.random()*50);

# Print the results
print results

# What if we did this 5 times? 
results = []
for j in range(5):
	tempResults = []
	for i in range(10):
		tempResults.append(random.random()*50);
	results.append(tempResults)

# Print the results
print results

# How about if we had 10 users and each of them did collected 10 results 5 times ?
results = []
for k in range(10):
	userResults = []
	for j in range(5):
		tempResults = []
		for i in range(10):
			tempResults.append(random.random()*50);
		userResults.append(tempResults)
	results.append(userResults)

# Print the results
print results

# You can now begin to see how easy it is for us to store a lot of data in the same structure 