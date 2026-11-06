"""Sanity probes for supplied broken fixtures, not tests of an implemented design."""
from pathlib import Path
import asyncio,importlib.util,json,sqlite3,tempfile
R=Path(__file__).parent

def load(case,file):
 spec=importlib.util.spec_from_file_location(case,R/'cases'/case/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def auth_race():
 db=sqlite3.connect(':memory:');db.executescript("CREATE TABLE notes(id,org_id,status); CREATE TABLE members(user_id,org_id,active); INSERT INTO notes VALUES(7,2,'draft'); INSERT INTO members VALUES(3,2,1);")
 result=load('C01','notes.py').publish(db,3,7,lambda:db.execute('UPDATE members SET active=0 WHERE user_id=3'))
 row=db.execute('SELECT status FROM notes').fetchone()[0];assert result=='published' and row=='published';return {'revoked_actor_still_publishes':True,'probe':'controlled sequential interleaving, not concurrent load'}

def historic():
 db=sqlite3.connect(':memory:');db.executescript((R/'cases/C02/schema.sql').read_text());db.execute('INSERT INTO people VALUES(1,10)');db.execute("INSERT INTO releases VALUES(2,1,'2025-01-01')")
 q=(R/'cases/C02/read.sql').read_text();before=db.execute(q).fetchone()[2];db.execute('UPDATE people SET team_id=20');after=db.execute(q).fetchone()[2];assert (before,after)==(10,20);return {'historic_display_changes_with_current_membership':True}

def duplicate_intent():
 db=sqlite3.connect(':memory:');db.executescript((R/'cases/C03/schema.sql').read_text());enqueue=load('C03','enqueue.py').enqueue
 a=enqueue(db,1,{'label':'same'});b=enqueue(db,1,{'label':'same'});assert a==b;return {'two_identical_intentions_collapse':True}

async def retained_stream():
 m=load('C04','download.py');readers=[]
 class Reader:
  closed=False;reads=0
  async def read(self):
   self.reads+=1;await asyncio.sleep(0);return b'x'
  async def close(self):self.closed=True
 class Factory:
  async def open(self):r=Reader();readers.append(r);return r
 iterator=m.stream(Factory());await anext(iterator);r=readers[0];before=r.reads
 for _ in range(20):await asyncio.sleep(0)
 after=r.reads;assert after>before and not r.closed
 tasks=[t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
 for t in tasks:t.cancel()
 await asyncio.gather(*tasks,return_exceptions=True);await iterator.aclose();await r.close()
 return {'retained_abandoned_iterator_keeps_reading':True,'probe_cleanup_completed':True,'memory_benchmark':False}

def partial_export():
 m=load('C07','export.py');m.decode=lambda x:b'new';m.resize=lambda x,s:x
 def bad_write(dst,data):Path(dst).write_bytes(b'partial');raise RuntimeError('simulated interrupted encoder')
 m.write_image=bad_write
 with tempfile.TemporaryDirectory() as td:
  target=Path(td)/'image';target.write_bytes(b'old good')
  try:m.export('source',target,{})
  except RuntimeError:pass
  assert target.read_bytes()==b'partial'
 return {'failed_write_destroys_previous_completed_file':True,'probe':'injected encoder failure; not power-loss proof'}

out={'C01':auth_race(),'C02':historic(),'C03':duplicate_intent(),'C04':asyncio.run(retained_stream()),'C07':partial_export()};(R/'results/fixture-probes.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
