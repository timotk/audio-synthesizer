# app/Dockerfile

FROM python:3.11-slim

EXPOSE 8080

WORKDIR /app

# Install Java
RUN apt update && \
    apt install -y 

RUN apt-get update && apt-get install -y \
    default-jdk \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Add non-root user
ARG USERNAME=nonroot
RUN groupadd --gid 1000 $USERNAME && \
    useradd --uid 1000 --gid 1000 -m $USERNAME
## Make sure to reflect new user in PATH
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
USER $USERNAME

COPY . .
RUN pip3 install .
