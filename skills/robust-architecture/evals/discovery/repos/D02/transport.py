import asyncio

async def fetch(account):
    await asyncio.sleep(0)
    return ['feed:'+account]

