import xml.etree.ElementTree as ET

tree = ET.parse('AAPS_test1.nxml')

root = tree.getroot()
print root

journaltitle = root.find('.//journal-title')
print journaltitle.text

articletitle = root.find('.//article-title')
print articletitle.text

pmidarticle = root.find('.//article-id')
print pmidarticle.text

abstract = root.find('.//abstract/p')
print abstract.text

for element in root.findall('.//pub-id[@pub-id-type="pmid"]'):
    for i in element.iter():
        print i.tag, i.text, i.attrib

        

        
        

    