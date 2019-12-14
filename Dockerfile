#Dockerfile
FROM mosudi/ubuntu-rootfs-osbuilder-kataruntime:vrequirments
#FROM mosudi/ubuntu-rootfs-osbuilder-kataruntime
#FROM imosudi/ubuntu-rootfs-osbuilder:11
#FROM imosudi/ubuntu-rootfs-osbuilder:v13
#with python3-tk
RUN apt update
RUN apt install vim -y
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
ADD . /app
ENV PORT 9082
#RUN alias python=python3
#CMD ["gunicorn", "app:app", "--config=config.py"]
#RUN which python
#CMD ["/usr/bin/python3 -V"]
CMD ["/usr/bin/python3", "app.py"]
