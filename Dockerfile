FROM python:3.6-alpine
COPY *.txt  /app/
WORKDIR /app

RUN pip install -r requirements.txt
COPY *.py /app/

EXPOSE 9000
CMD ["python", "app.py"]
