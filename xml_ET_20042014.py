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

references = root.find('.//ref')
len(references)
for ref in root.iter('ref'):
    print ref.attrib, ref

pmid = root.findall('.//*[@pub-id-type="pmid"]')

for element in root.findall('ref'): 
    print 'Ref' # Yey print stuff out!
    print 'Name: ', element.find('surname').text
    print 'pmid:', element.find('pmid').text



for article in root.findall('ref'):
    RefID = article.find('ref').attrib
    Ref PMID = article.find('.ref/pmid[@pub-id-type="pmid"]')

tree.write("output.txt")


    


print ArticleID.text


for pubmed_article in root.findall('PubmedArticle'):
    ArticleID = pubmed_article.find('MedlineCitation').find('PMID').text
    year = pubmed_article.find('MedlineCitation').find('DateCreated').find('Year').text
    month = pubmed_article.find('MedlineCitation').find('DateCreated').find('Month').text
    day = pubmed_article.find('MedlineCitation').find('DateCreated').find('Day').text
    CreatedDate = year + month + day
    for mesh_heading in pubmed_article.find('MedlineCitation').find('MeshHeadingList').findall('MeshHeading'):
        MeSH = mesh_heading.find('DescriptorName').text
        IsMajor = mesh_heading.find('DescriptorName').get('MajorTopicYN')
        line_to_write = ArticleID + '|' + CreatedDate + '|' + MeSH + '|' + IsMajor + '\n'
        with open('my_text_file.txt', 'a') as f:
            f.write(line_to_write)
            
            for pa in root.iter('PubmedArticle'):
    ArticleID = pa.find('MedlineCitation/PMID').text
    CreatedDate = pa.find('MedlineCitation/DateCreated/Year').text+\
                  pa.find('MedlineCitation/DateCreated/Month').text.zfill(2)+\
                  pa.find('MedlineCitation/DateCreated/Day').text.zfill(2)
    for mh in pa.iter('MeshHeading'):
        DescriptorName = mh.find('DescriptorName').text
        MajorTopicYN = mh.find('DescriptorName').attrib['MajorTopicYN']
        f.write(ArticleID+'|'+CreatedDate+'|'+DescriptorName+'|'+MajorTopicYN+'\n')
f.close()






