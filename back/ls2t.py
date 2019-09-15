import json
import wave
import sys
import io

import pyaudio

from rev_ai.models import MediaConfig
from rev_ai.streamingclient import RevAiStreamingClient

from six.moves import queue


# Sample rate constants
CHUNK = 1028
SR = 44100

# rev.ai API constants
TOKEN = '02JSL03hWx0zEaKt6OGElI4YsK0MWkEnYKuOzn5QFlXsB_gqKdACoLwPC_1STxfeZd4wXsyIZ5PlVlvG-uadrWWZyczz0'

media_config = MediaConfig('audio/x-raw', 'interleaved', SR, 'S16LE', 1)
rev = RevAiStreamingClient(TOKEN, media_config)

with io.open('../data/output.raw', 'rb') as media:
    generator = [media.read()]

rresp = rev.start(generator)

for response in rresp:
    print(response)


rev.end()
