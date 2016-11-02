import XMLBuilder

class ParseInfoFromSite:
	def __init__(self):
		self.XML = XMLBuilder()
		#TODO

	def finishParser(self):
		self.writeToFile('visualforce.xml')