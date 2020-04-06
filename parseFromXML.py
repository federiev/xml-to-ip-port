f1=open("outputFile.txt", "a")
numeroReps=36000
import xml.etree.ElementTree as ET
tree = ET.parse('inputXML.xml')
root = tree.getroot()
for i in range(1, numeroReps):
   ip=root[i][0].attrib
   port=root[i][1][0].attrib
   f1.write(str(ip["addr"]) + ":" + str(port["portid"]) + "\n")
f1.close()