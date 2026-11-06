import json,sys

def finish(path):
    print(json.dumps({"path":path,"ok":True},separators=(",",":")))
    print("Saved",file=sys.stderr)

