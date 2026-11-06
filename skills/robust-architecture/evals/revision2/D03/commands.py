def revise(db, parcel_id, contents):
    db.execute('UPDATE parcels SET revision=revision+1, contents=?, clearance=NULL WHERE id=?', (contents, parcel_id))
    db.commit()

def request_scan(db, scanner, parcel_id):
    row = db.execute('SELECT revision, contents FROM parcels WHERE id=?', (parcel_id,)).fetchone()
    scanner.submit(parcel_id, row[0], row[1])
