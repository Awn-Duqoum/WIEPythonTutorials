def mean( someList, errCode ):
	sum = 0.0 # Need to declare as a float to avoid integer division
	print "Found mean !"
	for number in someList:
		sum = sum + number
	if(len(someList) != 0):
		return sum/len(someList)
	else:
		errorHappened = True
		return 0


dataSet = [1,2,3,4]
dataSet2 = [21,23,56,3]

errorHappened = False 

print str ( mean(dataSet,errorHappened) )