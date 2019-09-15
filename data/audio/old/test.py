from rev_ai.models import MediaConfig
from rev_ai.streamingclient import RevAiStreamingClient
import io


# Name of file to be transcribed
#filename = 'p1.raw'
filename = 'english_test.raw'

# String of your access token
#access_token = '02JSL03hWx0zEaKt6OGElI4YsK0MWkEnYKuOzn5QFlXsB_gqKdACoLwPC_1STxfeZd4wXsyIZ5PlVlvG-uadrWWZyczz0'
access_token = '021RBqj26AzVFWw7gkJ_mYOTBxdQoDikYFCDdyGFznouU9tioCAwqRgQOW2-iihk0ZhQ06vS0lxB1RsybMGSr7B0iwhL4'

# Media configuration of audio file.
# This includes the content type, layout, rate, format, and # of channels
#config = MediaConfig("audio/x-raw", "interleaved", 44100, "S16LE", 1)
config = MediaConfig("audio/x-raw", "interleaved", 16000, "S16LE", 1)

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
    for response in response_generator:
        print(response)

        # Ends the connection early. Not needed as the server will close the connection
        # upon receiving an "EOS" message.
        streamclient.end()
