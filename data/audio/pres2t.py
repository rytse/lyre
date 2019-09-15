import json
import sys

from rev_ai.models import MediaConfig
from rev_ai.streamingclient import RevAiStreamingClient
import io

target = sys.argv[1]
print(f'Target: {target}')

filename = f'{target}.raw'

# String of your access token
access_token = '021RBqj26AzVFWw7gkJ_mYOTBxdQoDikYFCDdyGFznouU9tioCAwqRgQOW2-iihk0ZhQ06vS0lxB1RsybMGSr7B0iwhL4'

# Media configuration of audio file.
# This includes the content type, layout, rate, format, and # of channels
#config = MediaConfig("audio/x-raw", "interleaved", 16000, "S16LE", 1)
config = MediaConfig("audio/x-raw", "interleaved", 44100, "S16LE", 1)

# Create client with your access token and media configuration
streamclient = RevAiStreamingClient(access_token, config)

# Open file and read data into array.
# Practically, stream data would be divided into chunks
with io.open(filename, 'rb') as stream:
    MEDIA_GENERATOR = [stream.read()]

# Starts the streaming connection and creates a thread to send bytes from the
# MEDIA_GENERATOR. response_generator is a generator yielding responses from
# the server
response_generator = streamclient.start(MEDIA_GENERATOR)

# Iterates through the responses from the server when obtained
print(type(response_generator))
msg = ''
tmsg = ''
c = 0
with open(f'{target}.csv', 'w+') as fo:
    for response in response_generator:
        rdict = json.loads(response)
        if rdict['type'] != 'partial':
            for el in rdict['elements']:
                msg += el['value']
        if c % 5 == 0:
            fo.write(f'{c},{msg}\n')
            tmsg += msg
            print(msg)
            msg = ''

        c += 1

streamclient.end()
