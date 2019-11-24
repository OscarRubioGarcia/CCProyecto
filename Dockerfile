FROM python:3.7-alpine
MAINTAINER Oscar Rubio Garcia 
WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code

CMD [ "python" , "app.py" ]
