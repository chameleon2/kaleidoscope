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


for element in root.findall('.//ref'):
    for i in element.getchildren():
      print 'Ref tag: ', element.find('label').text 
    for i in  element[1].getchildren():
        print 'PMID: ', element[1].find('pub-id [@pub-id-type="doi"]').text
        print i.tag, i.text

        

        
        

    