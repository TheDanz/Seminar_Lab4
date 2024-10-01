FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y git python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER jenkins