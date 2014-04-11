import xml.etree.ElementTree as ET

tree = ET.parse('AAPS_test1.nxml')
root = tree.getroot()
print root
for child_of_root in root:
    print child_of_root.tag, child_of_root.attrib
for elem in tree.iter():
    print elem.tag, elem.attrib
    
    