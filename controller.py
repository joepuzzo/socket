import socketio
from aiohttp import web

# Create a new socket.io server and aiohttp web application
sio = socketio.AsyncServer(cors_allowed_origins="*")
app = web.Application()
sio.attach(app)


class JSNamespace(socketio.AsyncNamespace):
    async def on_connect(self, sid, environ):
        print("js connected")

    async def on_pulse(self, sid):
        print("js Pulse")

    async def on_disconnect(self, sid):
        print("js disconnected")


class PYNamespace(socketio.AsyncNamespace):
    async def on_connect(self, sid, environ):
        print("py connected")

    async def on_pulse(self, sid, data):
        print("py pulse")

    async def on_disconnect(self, sid):
        print("py disconnected")


sio.register_namespace(JSNamespace('/js'))
sio.register_namespace(PYNamespace('/py'))

if __name__ == '__main__':
    web.run_app(app, port=3000)
