import xml.etree.ElementTree as ET

tree = ET.parse('AAPS_test1.nxml')

root = tree.getroot()

references = root.findall('.//ref')
print references
len(references)
for ref in root.iter('ref'):
    print ref.attrib, ref
for elem in ref.iter():
    print  elem.text, elem.tag, elem.attrib




