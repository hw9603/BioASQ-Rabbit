#FROM deiis/base-image
FROM docker.lappsgrid.org/deiis/base

RUN pip install nltk sklearn werkzeug lxml diskcache pyquery pika
COPY . /root/

WORKDIR /root

ENTRYPOINT cd deiis/ && python setup.py install && cd .. && ./start.sh && /bin/bash