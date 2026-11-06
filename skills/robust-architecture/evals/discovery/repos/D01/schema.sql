CREATE TABLE copies(id INTEGER PRIMARY KEY,library_id INTEGER,state TEXT,borrower TEXT);
CREATE TABLE activity(copy_id INTEGER,kind TEXT);
INSERT INTO copies VALUES(11,1,'available',NULL),(22,2,'available',NULL),(33,1,'loaned','original');
