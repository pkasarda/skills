def lend(db,library_id,copy_id,borrower):
    row=db.execute("UPDATE copies SET state='loaned',borrower=? WHERE id=? AND library_id=? AND state='available' RETURNING id",(borrower,copy_id,library_id)).fetchone()
    if row is None: return 'refused'
    db.execute("INSERT INTO activity VALUES(?,'lent')",(copy_id,))
    db.commit()
    return 'lent'

