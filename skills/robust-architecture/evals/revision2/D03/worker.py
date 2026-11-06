def complete(db, parcel_id, revision, result):
    db.execute('INSERT INTO inspection_history VALUES(?,?,?)', (parcel_id, revision, result))
    db.execute('UPDATE parcels SET clearance=? WHERE id=?', (result, parcel_id))
    if result == 'clear':
        db.execute('INSERT INTO release_notices VALUES(?,?)', (parcel_id, revision))
    db.commit()
