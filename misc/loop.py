i = 0

while (i < 10):
	i = i + 1
	print ( str(i) )
	
shortList = [1,2,3,4,5,"pi"]
foundit = False
i = 0

# while( !foundit)
while (foundit == False):
	if( shortList[i] == "pi"):
		print ("Found it")
		print (str(i))
		foundit = True
	elif ( i >= len(shortList) ):
		foundit = True
	else:
		i = i + 1

print shortList[0] 