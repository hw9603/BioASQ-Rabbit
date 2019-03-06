FROM deiis/base-image

RUN pip install nltk sklearn werkzeug lxml diskcache pyquery pika==0.12 pymetamap
COPY *.py /root/

WORKDIR /root

ENTRYPOINT ["python", "service.py"]