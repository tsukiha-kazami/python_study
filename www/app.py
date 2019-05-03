import logging; logging.basicConfig(level = logging.DEBUG)
import asyncio,os ,json,time
from datetime import datetime

from aiohttp import web

async  def index(request):
    return  web.Response(body=b'<h1>kazami_tsuhika\' python project</h1>' ,content_type='text/html')

async def init(loop):
    app= web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = await  loop.create_server(app._make_handler(),'127.0.0.1',9000)
    logging.info('server start at http://127.0.0.1:9000')
    return  srv

loop= asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()