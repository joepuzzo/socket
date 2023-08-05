import socketio
import threading
import time

sio = socketio.Client(reconnection=True)

# Add a global flag to control the thread
running = False


def send_pulse():
    while running:
        sio.emit('pulse', 'data', namespace='/py')
        print("py sending pulse")
        time.sleep(5)


@sio.on('connect', namespace='/py')
def on_connect():
    global running
    print("Connected to the server")
    running = True
    threading.Thread(target=send_pulse).start()


@sio.on('disconnect', namespace='/py')
def disconnect():
    global running
    print("Disconnected from the server")
    running = False


if __name__ == "__main__":
    while True:
        try:
            sio.connect('http://localhost:3000', namespaces=['/py'])
            break
        except socketio.exceptions.ConnectionError:
            print("Failed to connect, retrying in 5 seconds...")
            time.sleep(5)
