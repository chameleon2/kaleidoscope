import xml.etree.ElementTree as ET

tree = ET.parse('AAPS_test1.nxml')

root = tree.getroot()

journaltitle = root.find('.//journal-title')
print journaltitle.text

articletitle = root.find('.//article-title')
print articletitle.text

pmidarticle = root.find('.//article-id')
print pmidarticle.text

abstract = root.find('.//abstract/p')
print abstract.text

references = root.find('.//ref')
len(references)
for ref in root.iter('ref'):
    print ref.attrib, ref

pmid = root.findall('.//pub-id')
print pmid




    







