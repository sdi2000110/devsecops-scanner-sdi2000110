FROM python:3.9-slim-bullseye

LABEL maintainer="sdi2000110"
LABEL description="System info utility for DevSecOps pipeline demo"

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        net-tools \
    && rm -rf /var/lib/apt/lists/*

COPY app.py .

RUN chmod +x app.py

ENTRYPOINT ["python3", "app.py"]
