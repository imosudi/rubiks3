#Dockerfile
FROM imosudi/ubuntu-rootfs-osbuilder:11
RUN apt update
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
ADD . /app
ENV PORT 9082
CMD ["gunicorn", "app:app", "--config=config.py"]