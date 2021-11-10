import asyncio
from base import ZmqBase
import keyboard
from keyboard import KeyboardEvent
from asyncio import QueueEmpty


addr = lambda p: f'tcp://*:{p}'

class Client(ZmqBase):

    def __init__(self, port=5556):
        # Create Socket
        super().__init__(port=port)
        self.socket.bind(addr(port))
        
        self.tlmQueue = asyncio.Queue()

        
    def start(self):
        super().start()

    
    async def _runner(self):
        await asyncio.gather(
            self.cmd_loop(),
            self.tlm_loop(),
            self.key_runner(),
        )
        

    async def cmd_loop(self):
        while True:
            cmd = await self.recv()
            print(cmd)


    async def tlm_loop(self):
        while True:
            try:
                item = self.tlmQueue.get_nowait()
                self.send(item)
            except QueueEmpty:
                await asyncio.sleep(0.1)
            

    async def key_runner(self):
        keyboard.on_press(self.handle_key)


    def handle_key(self, event: KeyboardEvent):
        self.tlmQueue.put_nowait(event.to_json())


if __name__ == '__main__':
    app = Client()
    app.start()