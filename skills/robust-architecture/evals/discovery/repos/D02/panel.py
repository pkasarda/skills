import cache
from refresh import Refresh

class Panel:
    def __init__(self): self.refresh=Refresh();self.account=None;self.feed=[]
    def open(self,account):
        self.account=account
        self.feed=cache.latest or []
        self.refresh.start(account,self.on_result)
    def close(self):
        self.refresh.stop();self.account=None
    def on_result(self,data): self.feed=data

