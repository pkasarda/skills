import sqlite3, unittest
from pathlib import Path
from worker import complete

class InspectionTest(unittest.TestCase):
    def test_clear(self):
        db=sqlite3.connect(':memory:')
        db.executescript(Path('schema.sql').read_text())
        db.execute("INSERT INTO parcels VALUES(1,1,'books',NULL)")
        complete(db,1,1,'clear')
        self.assertEqual(db.execute('SELECT clearance FROM parcels WHERE id=1').fetchone()[0], 'clear')
