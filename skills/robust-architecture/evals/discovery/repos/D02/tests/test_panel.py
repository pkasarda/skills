import asyncio,unittest,cache
from panel import Panel

class Flows(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self): cache.latest=None
    async def test_first_load(self):
        p=Panel();p.open('a');await asyncio.sleep(0);await asyncio.sleep(0)
        self.assertEqual(p.feed,['feed:a']);p.close()

