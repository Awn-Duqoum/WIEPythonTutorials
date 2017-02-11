# WIE Python Beginners Tutorial, Introduction to loops (part 2 : While Loops)
# Awn Duqoum - Jan 11 2017 

# For loops are great, but sometimes you want to loop until something happens 
# For example if you are looking for something 

shortList = [1,2,3,4,5,"pi"]

# To find pi you need to search the array, this can be done with a while loop and 
# a simple if statment 

foundIt = False
index = 0
while(foundIt == False):
	if(shortList[index] == "pi"):
		print "FOUND PI, IT WAS AT INDEX = " + str(index)
		foundIt = True # Will make sure we exit the loop
	else:
		index = index + 1;

# We need to be careful we don't get stuck however, for example the below snippit will
# crash our program
# foundIt = False
# index = 0
# while(foundIt == False):
	# if(shortList[index] == "love"):
		# print "FOUND love, IT WAS AT INDEX = " + str(index)
		# foundIt = True # Will make sure we exit the loop
	# else:
		# index = index + 1;