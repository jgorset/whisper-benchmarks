FROM ubuntu

WORKDIR /src

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install git -y
RUN apt-get install python3 python3-pip -y
RUN apt-get install wget -y
RUN apt-get install ffmpeg -y
RUN pip3 install -r requirements.txt

COPY . .
