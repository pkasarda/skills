import json,sqlite3,sys
from vendor import apply_manifest

def run(db,rows):
    cfg=json.load(open('config.json'))
    return apply_manifest(db,cfg['library_id'],rows)

if __name__=='__main__':
    db=sqlite3.connect(sys.argv[1]);print(run(db,json.load(open(sys.argv[2]))))

