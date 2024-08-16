FROM python:3.10-slim
WORKDIR /app

RUN apt-get update && apt-get -y install tesseract-ocr
RUN apt-get install tesseract-ocr-eng && apt-get install tesseract-ocr-slk
RUN pip install pillow
RUN pip install pytesseract
RUN pip install flask
RUN pip install flask-cors

COPY . .

EXPOSE 5000

ENV FLASK_APP=api.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]