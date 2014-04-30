import xml.etree.ElementTree as ET

tree = ET.parse('Biomass_Bioenergy_test.nxml')

root = tree.getroot()
print root

journal = root.find('.//journal-title')
print journal.text

title = root.find('.//article-title')
print title.text

paper_id = root.find('.//article-id')
print paper_id.text

abstract = root.find('.//abstract/p')
print abstract.text

for element in root.findall('.//pub-id[@pub-id-type="pmid"]'):
    for i in element.iter():
        print i.tag, i.text, i.attrib
        
  
import sqlite3

def create_table(curs):
    # create the papers table (if it doesn't already exist)
    curs.execute("CREATE TABLE IF NOT EXISTS papers (id integer primary key, title text, refs text)")

def add_paper(curs, paper_id, title, ref_list):
    # turn ref list into a string
    ref_string = ','.join(str(r) for r in ref_list)

    # add the paper to the database
    curs.execute("INSERT INTO papers VALUES (?,?,?)", (paper_id, title, ref_string))

def main():
    # connect to the database file (create if it doesn't exist)
    conn = sqlite3.connect('pubmed.db')

    # get a database cursor to perform operations
    curs = conn.cursor()

    # create the table
    create_table(curs)

    # add a test paper
    add_paper(curs, 1, 'tree', [2, 3, 4])

    # commit the changes
    conn.commit()

main()