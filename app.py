from flask import Flask, escape, request, Blueprint, current_app, session, url_for, render_template
from flask_socketio import SocketIO, emit
import uuid
import wave
import threading,json
from rev_ai.models import MediaConfig
from rev_ai.streamingclient import RevAiStreamingClient
import random
from six.moves import queue
access_token="02JSL03hWx0zEaKt6OGElI4YsK0MWkEnYKuOzn5QFlXsB_gqKdACoLwPC_1STxfeZd4wXsyIZ5PlVlvG-uadrWWZyczz0"
example_mc = MediaConfig('audio/x-raw', 'interleaved', 44100, 'S16LE', 1)
streamclient = RevAiStreamingClient(access_token, example_mc)

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def mainpage():
    return render_template('flask_test.html')

@app.route('/update/', methods=['GET'])
def hello():
    return f'Hello! {random.random()}'


# bp = Blueprint('audio', __name__, static_folder='static',
#                template_folder='templates')

@app.route('/indata/')
def index():
    """Return the client application."""
    # print(0)
    return render_template('main.html')


@socketio.on('start-recording')
def start_recording(options):
    """Start recording audio from the client."""
    pass
    # print(1)

dataq=queue.Queue()
def genq():
    while 1:
        chunk = dataq.get()
        if chunk is None:
            return
        data = [chunk]
        while True:
            try:
                chunk = dataq.get(block=False)
                data.append(chunk)
            except queue.Empty:
                break
        yield b''.join(data)
dq=genq()


@socketio.on('write-audio')
def write_audio(data):
    """Write a chunk of audio from the client."""
    # print(2)
    for i in data:
        dataq.put(i)
    print(data)

@socketio.on('end-recording')
def end_recording():
    """Stop recording audio from the client."""
    # print(3)

def stt():
    # Uses try method to allow users to manually close the stream
    try:
        # Starts the server connection and thread sending microphone audio
        response_gen = streamclient.start(dq)

        # Iterates through responses and prints them
        for response in response_gen:
            response_dict=json.loads(response)
            if response_dict['type']=='final':
                msg=""
                for i in response_dict["elements"]:
                    msg+=i['value']
                if(msg.strip()):
                    print(msg.strip())

    except KeyboardInterrupt:
        # Ends the websocket connection.
        streamclient.client.send("EOS")
        pass

if __name__ == '__main__':
    t=threading.Thread(target=stt)
    t.start()
    socketio.run(app,use_reloader=True, debug=True)