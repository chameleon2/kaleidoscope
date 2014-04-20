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

references = root.findall('.//ref')
len(references)
print references
for ref in root.iter('ref'):
    print ref.attrib

for element in root.findall('.//ref'): 
    for i in  element.iter():
        print 'Ref Label:',element.find('label').text
        print 'PMID: ', element.find('.//*[@pub-id-type="pmid"]')
    