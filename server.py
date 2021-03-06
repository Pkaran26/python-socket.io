from aiohttp import web
import socketio

#pip3 install python-socketio
#pip3 install aiohttp
#https://www.botreetechnologies.com/blog/django-websocket-with-socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def FIRST(sid, data):
    print('Received data: ', data)
    await sio.emit('REPLY', data={
        "message": 'hi'
    }, room=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
