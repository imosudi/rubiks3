#Dockerfile
FROM imosudi/ubuntu-rootfs-osbuilder-pg7331_kata:v0.9
#FROM imosudi/ubuntu-rootfs-osbuilder-pg7331_kata:V0.9
#FROM imosudi/ubuntu-rootfs-osbuilder-pg7331:v0.9
#FROM imosudi/ubuntu-rootfs-osbuilder:v13
#with python3-tk
RUN apt update
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
ADD . /app
ENV PORT 9082
#CMD ["gunicorn", "app:app", "--config=config.py"]
CMD ["/usr/bin/python3", "app.py"]
