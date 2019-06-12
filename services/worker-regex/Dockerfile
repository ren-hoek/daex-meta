FROM alpine
WORKDIR /root
COPY requirements.txt .
RUN apk update && apk add --no-cache python3 && \
	pip3 install --no-cache-dir --upgrade pip && \
	pip3 install --no-cache-dir -r requirements.txt
COPY worker_files .
EXPOSE 9998
ENTRYPOINT ["python3"]

