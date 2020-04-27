FROM imosudi/ubuntu-rootfs-osbuilder:v10.0

#with python3-tk# File Author / Maintainer
MAINTAINER mosudi.pg7331@st.futminna.edu.ng

RUN apt update


WORKDIR /rubiksapp

COPY requirements.txt  /rubiksapp
RUN pip3 install -r requirements.txt

COPY  /app .

ENV PORT 9082

CMD ["/usr/bin/python3", "app.py"]



#docker build -t imosudi/rubiks3ubuntufs-kataruntime:v1.4 . && \
# docker run -it -p 9082:9082 \-v /home/mosud/Documents/dev3/log_dir:/app/log_dir/ \ 
# imosudi/rubiks3ubuntufs-kataruntime:v1.4
#FROM imosudi/ubuntu-rootfs-osbuilder-pg7331_kata:v0.9
#FROM imosudi/ubuntu-rootfs-osbuilder:v10.0

#with python3-tk# File Author / Maintainer
#MAINTAINER mosudi.pg7331@st.futminna.edu.ng

#RUN apt update

# Apache2
#RUN apt-get install -y apache2

#WORKDIR /app


#ADD requirements.txt /app/requirements.txt
#RUN pip3 install -r /app/requirements.txt
#ADD . /app

#Logging
#RUN mkdir -p /app/log_dir


#ENV PORT 9082

###EXPOSE 80


###CMD ["gunicorn", "app:app", "--config=config.py"]

#CMD ["/usr/bin/python3", "app.py"]
####CMD [ "apache2ctl -D FOREGROUND"]

#FROM node:alpine as builder

#WORKDIR '/app'

#COPY package.json

#RUN npm run build

#FROM nginx

#COPY --from=builder /app/build
