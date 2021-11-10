import asyncio
from base import ZmqBase


addr = lambda p: f'tcp://localhost:{p}'

class Server(ZmqBase):

    def __init__(self, port=5556):
        super().__init__(port)
        self.socket.connect(addr(self.port))


    async def tlm_loop(self):
        while True:
            tlm = await self.recv()
            self.handle_tlm(tlm)


    async def cmd_loop(self):
        while True:
            await asyncio.sleep(1)
            # self.send(self.package_cmd())


    def package_cmd(self):
        return 'Test CMD'


    def handle_tlm(self, tlm):
        print(tlm)


if __name__ == '__main__':
    srv = Server()
    srv.start()