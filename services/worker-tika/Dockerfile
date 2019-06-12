FROM alpine
WORKDIR /root
COPY install_tika.py .
COPY requirements.txt .
RUN apk update && apk add --no-cache zlib-dev jpeg-dev gcc python3-dev musl-dev openjdk8-jre tesseract-ocr poppler-utils libreoffice ttf-liberation
RUN pip3 install -U --no-cache-dir pip
RUN pip3 install --no-cache-dir -r requirements.txt && ./install_tika.py
COPY worker_files .
EXPOSE 9998
ENTRYPOINT ["python3"]
