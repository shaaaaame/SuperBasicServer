FROM python:3.7.3-slim
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
RUN pip3 install gdown
 
COPY . /app
WORKDIR /app
 
RUN rm -rf /app/models
RUN mkdir -p /app/models
RUN apt-get update -y
RUN apt-get install -y unzip
#https://drive.google.com/file/d/141cUvpbRqhz7399XN8ze8icCdw78Xqto/view?usp=sharing
#Replace the id down here with your own!
RUN gdown --id 141cUvpbRqhz7399XN8ze8icCdw78Xqto --output /app/models/models.zip
RUN unzip /app/models/models.zip -d /app/models/
RUN rm /app/models/models.zip
 
 
CMD waitress-serve --port=$PORT --call 'app:create_app'