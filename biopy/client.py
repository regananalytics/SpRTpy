# import vsdbg_ez
import asyncio
from base import ZmqBase
import keyboard

addr = lambda p: f'tcp://*:{p}'


class Client(ZmqBase):

    def __init__(self, port=5556):
        # Create Socket
        super().__init__(port=port)
        self.socket.bind(addr(port))
        

    def start(self):
        keyboard.on_press(self.handle_key)
        super().start()


    async def cmd_loop(self):
        while True:
            cmd = await self.recv()
            print(cmd)


    async def tlm_loop(self):
        while True:
            await asyncio.sleep(1)
            pass


    def handle_key(self, event):
        self.send(event.to_json())


if __name__ == '__main__':
    app = Client()
    app.start()