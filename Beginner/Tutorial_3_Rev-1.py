# WIE Python Beginners Tutorial, Introduction to loops (part 1 : For Loops)
# Awn Duqoum - Jan 11 2017 

# When coding there comes a time when you need to do something a lot of times
# for example if you wanted to output all numbers from 1 to 10 you could 
print 1
print 2
print 3
print 4
print 5
print 6
print 7
print 8
print 9
print 10
# or if you wanted to increase the numbers in a list by 1 you could 
shortList = [1,2,3,4]
shortList[0] = shortList[0] + 1;
shortList[1] = shortList[1] + 1;
shortList[2] = shortList[2] + 1;
shortList[3] = shortList[3] + 1;

# or you could be smart and use a loop. The basic concept of a for loop is to do 
# something until a condition is met. 

for number in range(10):
	print number
	
# What the above does is loops until number is equal to or more then 10, 
# and increase it by 1  each time it loops

for number in range(-1,10):
	print number

# What the above does is loops until number is equal to or more then 10, 
# and increase it by 1  each time it loops but it starts at -1

for number in range(-5,5,10):
	print number

# What the above does is loops until number is equal to or more then 10, 
# and increase it by 10  each time it loops but it starts at -5


# Instead of a number you can give the loop a List
lunch = ['apple pie',"orange pie","no pie","All the pie"]
for anyNameYouWant in lunch:
	print anyNameYouWant
	
# This is also valid
for index in range(len(lunch)):
	print lunch[index]
	
# len() returns the length of a list, so we are back to giving it just a number
	
	
	
	
