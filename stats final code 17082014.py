import sqlite3

def main():
    # connect to the database file (create if it doesn't exist)
    conn = sqlite3.connect('pubmed1.db')

    # get a database cursor to perform operations
    curs = conn.cursor()

    # read in DB and create dictionary
    entries = curs.execute("SELECT id, refs FROM papers")
    db_dict = {}
    for entry in entries:
        id, refs = entry
        if len(refs) == 0:
            refs_list = []
        else:
            refs_list = [int(r) for r in refs.split(',')]
        db_dict[id] = refs_list

    # compute stats
    num_papers = 0
    num_refs = 0
    num_refs_found = 0
    for id, refs_list in db_dict.iteritems():
        num_papers += 1
        num_refs += len(refs_list)
        for ref in refs_list:
            if ref in db_dict:
                num_refs_found += 1

    # print statistics
    print 'Num papers:          ', num_papers
    print 'Refs per paper:      ', 1.0 * num_refs / num_papers
    print 'Refs found per paper:', 1.0 * num_refs_found / num_papers
    print '% refs we have:      ', 100.0 * num_refs_found / num_refs

    # commit the changes
    conn.commit()

main()
