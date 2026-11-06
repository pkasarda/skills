import asyncio

async def stream(factory):
    reader=await factory.open()
    queue=asyncio.Queue()
    async def pump():
        while True:
            data=await reader.read()
            await queue.put(data)
            if data is None: return
    task=asyncio.create_task(pump())
    while True:
        chunk=await queue.get()
        if chunk is None: break
        yield chunk

