FROM nikolaik/python-nodejs:python3.6-nodejs12

WORKDIR /app
COPY . /app

RUN apt update && apt -y upgrade && apt install -y portaudio-dev

RUN pip install --trusted-host pypi.python.org -r Requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
