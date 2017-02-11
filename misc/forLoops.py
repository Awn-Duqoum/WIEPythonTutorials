shortList = [1,2,3,4]

print str(shortLst)
print "Length = " + str(len(shortList)) 

for i in range( len(shortList) ):
	shortList[i] = shortList[i] + 1
	
print str(shortList)


shortList = [1,2,3,4,5,"pi"]

for i in range(len(shortList)):
	if( shortList[i] == "pi" ):
		print "Found it"
		
		
for i in range(10,20,2):
	print str(i)
	