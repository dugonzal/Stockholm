FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends mysql-client \
    && rm -rf /var/lib/apt/lists/* \
	apt install -y python3-pip \
COPY ../stockholm /home/stockholm/

WORKDIR /home/stockholm/

RUN pip3 install -r requirements.txt

RUN virtualenv venv

RUN . venv/bin/activate

ENTRYPOINT ["mysql"]

