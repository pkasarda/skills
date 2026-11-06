def apply_manifest(db,library_id,rows):
    outcomes=[]
    for row in rows:
        changed=db.execute("UPDATE copies SET state='loaned',borrower=? WHERE id=?",(row['borrower'],int(row['copy_id']))).rowcount
        db.commit()
        outcomes.append('lent' if changed else 'missing')
    return outcomes

