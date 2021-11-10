from abc import ABCMeta
import asyncio
import zmq
from zmq.asyncio import Context


context = Context()

class ZmqBase(metaclass=ABCMeta):

    def __init__(self, port=5556):
        self.port = port
        self.socket = context.socket(zmq.PAIR)


    def start(self):
        asyncio.run(self._runner())


    async def _runner(self, *args):
        await asyncio.gather(
            self.cmd_loop(),
            self.tlm_loop(),
            *args
        )

    async def cmd_loop(self):
        pass


    async def tlm_loop(self):
        pass


    def send(self, json, **kwargs):
        self.socket.send_json(json, **kwargs)

    
    async def recv(self):
        return await self.socket.recv_json()
