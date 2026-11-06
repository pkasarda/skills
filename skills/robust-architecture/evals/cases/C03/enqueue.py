import hashlib,json

def enqueue(db, account_id, payload):
    h=hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()
    existing=db.execute("SELECT id FROM jobs WHERE account_id=? AND payload_hash=?",(account_id,h)).fetchone()
    if existing: return existing[0]
    return db.execute("INSERT INTO jobs(account_id,payload_hash,payload) VALUES(?,?,?) RETURNING id",(account_id,h,json.dumps(payload))).fetchone()[0]

