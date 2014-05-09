import sqlite3
import xml.etree.ElementTree as ET

# This is the Paper class.
# Create one of these to hold all the information about a paper.
class Paper:
    def __init__(self, id, doi, title, journal, refs):
        self.id = int(id)
        self.doi = doi
        self.title = title.replace('\n', ' ')
        self.journal = journal
        self.refs = refs

# Read in a paper from an XML file, and return a new Paper object.
def read_paper_from_xml(filename):
    tree = ET.parse(filename)

    root = tree.getroot()
    #print root

    paper_id = root.find('.//article-id')
    doi = root.find('.//article-id[@pub-id-type="doi"]')
    title = root.find('.//article-title')
    journal = root.find('.//journal-title')
    abstract = root.find('.//abstract/p')

    refs = []
    for element in root.findall('.//pub-id[@pub-id-type="pmid"]'):
        for i in element.iter():
            refs.append(int(i.text))

    print 'Filename:', filename
    print 'Paper id:', paper_id.text
    print 'DOI:     ', doi.text
    print 'Title:   ', title.text
    print 'Journal: ', journal.text
    print 'Ref list:', refs
    print ''

    # Create and return a new Paper object.
    return Paper(paper_id.text, doi.text, title.text, journal.text, refs)
        
def create_table(curs):
    # create the papers table (if it doesn't already exist)
    curs.execute("CREATE TABLE IF NOT EXISTS papers (id integer primary key, doi text, title text, refs text)")

def add_paper(curs, paper):
    # turn ref list into a string
    ref_string = ','.join(str(r) for r in paper.refs)

    # add the paper to the database
    curs.execute("INSERT INTO papers VALUES (?,?,?,?)", (paper.id, paper.doi, paper.title, ref_string))

def main():
    # connect to the database file (create if it doesn't exist)
    conn = sqlite3.connect('pubmed.db')

    # get a database cursor to perform operations
    curs = conn.cursor()

    # create the table
    create_table(curs)

    # read in and add papers
    input_papers = [
        'Biomass_Bioenergy_test.nxml',
        'AAPS_test1.nxml',
        'ACS_Chem_Biol_test.nxml',
    ]
    for filename in input_papers:
        paper = read_paper_from_xml(filename)
        add_paper(curs, paper)

    # commit the changes
    conn.commit()

main()
