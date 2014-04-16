import xml.etree.ElementTree as ET
tree = ET.parse('ACS_Chem_Biol_test.nxml')

root = tree.getroot()
print root, root.attrib, root.tag

journaltitle = root.find('.//journal-title')
print journaltitle.text

articletitle = root.find('.//article-title')
print articletitle.text

pmidarticle = root.find('.//article-id')
print pmidarticle.text

abstract = root.find('.//abstract')
print abstract.text

references = root.findall('.//ref')
len(references)
for ref in root.iter('ref'):
    print ref.attrib

referencesp = root.findall('.//pub-id')
print referencesp
len(referencesp)

pmidarticle = root.find('.//article-id')
print pmidarticle, pmidarticle.text
