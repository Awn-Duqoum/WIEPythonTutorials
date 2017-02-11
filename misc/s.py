import os

class files: 

	def __init__(self):
		self.length = 0
		self.names = []
		
	def __str__(self):
		print('Number of file: {0}').format(self.length)
		print('File name : {0}').format(self.names)
		return('\n')
	
	def addFile (self, item):
		self.names.append(item)
		self.length = self.length + 1

class dirScrapper:
	
	def __init__(self):
		self.textFiles = files()
		self.codeFiles = files()
		self.miscFiles = files()
		self.path = ""
	
	def setPath(self,path):
		if(not isinstance(path, basestring)):
			print ("Error path must be string\n")
		else:
			self.path = path
			print ('Path set to {0}').format(path)
	
	def __str__(self):
		print(self.textFiles)
		print(self.codeFiles)
		print(self.miscFiles)
		return ('\n')
	
	def scrap (self, verbose=False):
		allFiles = os.listdir(self.path)
		
		for i in range(len(allFiles)):
			if(verbose):
				print ('File {0} is called {1}').format(i,allFiles[i])
				
			if(os.path.isdir(allFiles[i])):
				self.miscFiles.addFile(allFiles[i])
			else:
				filename, file_extension = os.path.splitext(allFiles[i])
				if(file_extension == ".exe"):
					self.codeFiles.addFile(allFiles[i])
				elif(file_extension == '.txt'):
					self.textFiles.addFile(allFiles[i])
				else:
					self.miscFiles.addFile(allFiles[i])

if __name__ == "__main__":
	x = dirScrapper()
	x.setPath('c:\\Python27')
	x.scrap()
	print(x)
		
		
		
		
		
		
		
		
		
		
		
		
		
		