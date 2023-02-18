import asyncio
import yappi
from calls import cpu_intensive_call

async def foo():
    await asyncio.sleep(1.0)
    await baz()
    cpu_intensive_call(num_iterations=10000000)
    await asyncio.sleep(0.5)

async def baz():
    await asyncio.sleep(1.0)

yappi.set_clock_type('wall')
with yappi.run():
    asyncio.run(foo())
yappi.get_func_stats().print_all()
yappi.get_func_stats()._save_as_PSTAT('out/asyncio_yappi.prof')
