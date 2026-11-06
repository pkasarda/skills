import sqlite3,unittest
from pathlib import Path
from library.commands import lend
from vendor import apply_manifest

class Flows(unittest.TestCase):
    def setUp(self):
        self.db=sqlite3.connect(':memory:');self.db.executescript(Path('schema.sql').read_text())
    def test_lend(self): self.assertEqual(lend(self.db,1,11,'reader'),'lent')
    def test_vendor(self): self.assertEqual(apply_manifest(self.db,1,[{'copy_id':11,'borrower':'reader'}]),['lent'])

