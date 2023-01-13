# app/Dockerfile

FROM python:3.11-slim

EXPOSE 8080

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip3 install .

ENTRYPOINT ["streamlit", "run", "synthesizer/main.py", "--server.port=8080", "--server.address=0.0.0.0"]
