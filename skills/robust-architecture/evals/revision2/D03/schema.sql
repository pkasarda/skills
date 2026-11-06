CREATE TABLE parcels(id INTEGER PRIMARY KEY, revision INTEGER NOT NULL, contents TEXT NOT NULL, clearance TEXT);
CREATE TABLE inspection_history(parcel_id INTEGER, revision INTEGER, result TEXT);
CREATE TABLE release_notices(parcel_id INTEGER, revision INTEGER);
