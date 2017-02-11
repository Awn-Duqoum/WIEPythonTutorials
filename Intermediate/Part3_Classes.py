import os 

class files:
	""" The  defult constructor """
	def __init__(self):
		self.length = 0
		self.files = []

	def __str__(self):
		print('Number of files : {0}').format(self.length)
		print('File names : {0}').format(self.files)
		return ('\n')
	
	def append(self,item):
		self.files.append(item)
		self.length = self.length + 1

class dirScrapper:

	""" The defult constructor """
	def __init__(self):
		self.textFiles = files()
		self.codeFiles = files()
		self.miscFiles = files()
		self.path = ""
	
	def setPath (self,path):
		""" Lets do some error checking """
		if(not isinstance(path,basestring)):
			print('Error path must be a string \n')
		else:
			self.path = path
			print('Path set to : {0}').format(path)
	
	def scrap (self,verbose=False):	
		""" Let's make this class useful """
		allFiles = os.listdir(self.path)
		for i in range(len(allFiles)):
			""" Verbose is an optional parameter check if it was set """
			if(verbose): 
				print ('File {0} is called {1}').format(i,allFiles[i])
			
			if(os.path.isdir(allFiles[i])):
				self.miscFiles.append(allFiles[i])
			else:
				filename, file_extension = os.path.splitext(allFiles[i])
				if(file_extension == ".exe"):
					self.codeFiles.append(allFiles[i])
				elif(file_extension == '.txt'):
					self.textFiles.append(allFiles[i])
				else:
					self.miscFiles.append(allFiles[i])
	
	def __str__(self):
		print(self.textFiles)
		print(self.codeFiles)
		print(self.miscFiles)
		return ('\n')
		
if __name__ == "__main__":
	x = dirScrapper();
	x.setPath('C:\\Python27')
	x.scrap()	
	print(x)