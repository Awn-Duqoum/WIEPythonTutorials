# WIE Python Beginners Tutorial, Introduction to if statements 
# Awn Duqoum - Jan 11 2017

# When coding there comes a time when the code needs to make a decision based on 
# the value of a variable. To do this we need if statements

pieIsGood = True

if(pieIsGood == True):
	print "Pie is always good"

# There are two important things to note about the if statement above, the first is 
# the == sign. When equating two things we used the single = symbol but when we want
# compare the value of two things we use == 

# For example 
A = 5 
# Sets the variable A to 5 while
print A == 5
# Returns true

# The second thing that is important to note is the fact that the second line 
# is indented. Unlike other languages, spaces in python matter ... a lot. 
# the if statement ends when the indentation ends

if(pieIsGood == False):
	print "This will not print"

#if(pieIsGood == False):
#print "This will throw an error"

# In addition to the if statement there is an else if. Which checks the first statement
# and if it's false moves on to the else 

if(pieIsGood == 90):
	print "This will not print"
elif(pieIsGood == True):
	print "This will print"

# And an else statment, which will also excute if all that is above it is false

if(A == 4):
	print "This will not print"
else:
	print "Much print"
	
# You can use else and else if together and are not limited to the number of 
# checks you have. The only rule is you need to start with an if and if you have 
# and else it must be the last check 