#Dockerfile
FROM imosudi/ubuntu-rootfs-osbuilder-pg7331_kata:v0.9

#with python3-tk# File Author / Maintainer
MAINTAINER mosudi.pg7331@st.futminna.edu.ng

RUN apt update

# Apache2
#RUN apt-get install -y apache2

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
ADD . /app
ENV PORT 9082

#EXPOSE 80


#CMD ["gunicorn", "app:app", "--config=config.py"]

CMD ["/usr/bin/python3", "app.py"]
#CMD [ "apache2ctl -D FOREGROUND"]
