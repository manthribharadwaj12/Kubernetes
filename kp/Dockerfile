# FROM python:3.7

# RUN mkdir /app
# WORKDIR /app
# ADD . /app/
# RUN pip install -r requirements.txt

# EXPOSE 5000
# CMD ["python", "/app/main.py"]
FROM ubuntu

RUN apt update

RUN apt install python3-pip -y

RUN pip3 install flask

RUN pip3 install pandas

RUN pip3 install yfinance

WORKDIR /app

COPY . .

CMD flask run -h 0.0.0.0 -p 8083