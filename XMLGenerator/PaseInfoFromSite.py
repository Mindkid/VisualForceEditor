import XMLBuilder
from bs4 import BeautifulSoup

urlglobal = "https://developer.salesforce.com"
uriInicial = "/docs/atlas.en-us.pages.meta/pages/pages_compref.htm"

class ParseInfoFromSite:
	def __init__(self):
		self.XML = XMLBuilder()
		#TODO
	
	def parseFunction(self, namespace, funtionName):
		#TODO
		self.XML.addFunction(namespace, funtionName)
	
	def parseAttribute(self, funtionName, name, type, description, required, access):
		#TODO
		self.XML.creatElementToAdd(funtionName, name, type, description, required, access)
	
	
	def finishParser(self):
		self.writeToFile('visualforce.xml')