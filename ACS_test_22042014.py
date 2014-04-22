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

pmidarticle = root.find('.//article-id')
print pmidarticle, pmidarticle.text

for element in root.findall('.//pub-id[@pub-id-type="pmid"]'):
    for i in element.iter():
        print i.tag, i.text, i.attrib

