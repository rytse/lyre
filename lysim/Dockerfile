FROM nikolaik/python-nodejs:python3.6-nodejs12

WORKDIR /lysim
COPY . /lysim

RUN pip install --trusted-host pypi.python.org -r Requirements.txt

EXPOSE 80

CMD ["python", "relay.py"]
