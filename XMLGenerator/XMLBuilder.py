from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

class XMLBuilder:
	def __init__(self):
		self.root = Element('XML')
	
	def addNameSpace(self, namespace):
		if not self.root.find(namespace):
			SubElement(self.root, namespace)
			self.namespace = namespace
	
	def addFunction(self, namespace, funtionName):
		self.addNameSpace(namespace)
		element2Add = Element(funtionName)
		self.root.find(namespace).append(element2Add)
		
		
	def creatElementToAdd(self, funtionName, name, type, description, required, access):
		element2Add = Element(name)
		element2Add.append(self.buildAttribute('Type', type))
		element2Add.append(self.buildAttribute('Description', description))
		element2Add.append(self.buildAttribute('Required', required))
		element2Add.append(self.buildAttribute('Access', access))
		self.root.find(self.namespace).find(funtionName).append(element2Add)
	
	
	def buildAttribute(self, type, value):
		elem = Element(type)
		elem.text = value
		return elem

	def writeToFile(self, filename):
		ElementTree(self.root).write(filename)


def createXML():
	xml = XMLBuilder()
	xml.addFunction('Apex', 'ActionFunction')
	xml.creatElementToAdd('ActionFunction', 'Id', 'Number', 'Spec', 'True', 'Global')
	xml.creatElementToAdd('ActionFunction', 'Value', 'String', 'Valor', 'True', 'Global')
	xml.addFunction('Apex', 'Istobla')
	xml.creatElementToAdd('Istobla', 'Id', 'Number', 'Spec', 'True', 'Global')
	xml.creatElementToAdd('Istobla', 'Value', 'String', 'Valor', 'True', 'Global')
	xml.writeToFile('visualforce.xml')
	
	
createXML()

