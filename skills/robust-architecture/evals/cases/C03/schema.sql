CREATE TABLE jobs(id INTEGER PRIMARY KEY,account_id INTEGER,payload_hash TEXT,payload TEXT,UNIQUE(account_id,payload_hash));

