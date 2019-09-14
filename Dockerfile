FROM nikolaik/python-nodejs:python3.6-nodejs12

WORKDIR /app
COPY . /app

RUN pip install --trusted-host pypi.python.org -r Requirements.txt

EXPOSE 80

CMD ["python", "back/backend.py"]
CMD ["python", "front/frontend.py"]
