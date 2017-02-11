# The purpose of this module is to show case some useful system interface operations

import sys,os

# If memory is a concern, a useful function is shown below that'll return the size of any object it is given
intArray = [1,2,3];
sys.getsizeof(intArray)

# When on windows it is often needed to know what OS version you are running 
versionNumber = sys.getwindowsversion().major;

if(versionNumber == 0):
	print ("Current version : Win32s on Windows 3.1")
elif(versionNumber == 1):
	print ("Current version : Windows 95/98/ME")
elif(versionNumber == 2):
	print ("Current version : Windows NT/2000/XP/x64")
elif(versionNumber == 3):
	print ("Current version : Windows CE")
elif(versionNumber == 6):
	print ("Current version : Windows 10")
	
# Another useful operation is to figure out what the largest int the system can support is 

largeSignedInt = sys.maxint
largeUnsignedInt = sys.maxsize

print ("The largest signed int is : {0}\n").format(largeSignedInt)
	
# When calling other scripts and or finding files the OS path is very very important 
print("The system path is :" +str(sys.path))

# Python lets you change the way the command line interface looks 
sys.ps1 = "_-_-_-_-_-_-_"

# You can ask for the current location by using OS functions 
print (os.getcwd())

# You can change print statments to a file instead of the command line
orig_stdout = sys.stdout
file = open('tempOutputFile.txt', 'w')
sys.stdout = file
print ("TEST TEST TEST\n")
file.close()
sys.stdout = orig_stdout

# Most basic method is the exit method, that exits the script and returns a value for the error code
sys.exit();
