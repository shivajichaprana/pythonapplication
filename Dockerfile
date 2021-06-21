FROM python:latest
MAINTAINER shivaji

COPY app.py /
RUN pip3 install web.py==0.60

CMD ["python", "./app.py"]
EXPOSE 8080
