import asyncio,cache,transport

class Refresh:
    def __init__(self): self.timer_running=False
    def start(self,account,on_result):
        self.timer_running=True
        async def once():
            data=await transport.fetch(account)
            cache.latest=data
            on_result(data)
        asyncio.create_task(once())
    def stop(self): self.timer_running=False

