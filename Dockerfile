#docker build -t imosudi/rubiks3ubuntufs-kataruntime:v1.4 . && docker run -it -p 9082:9082 -v /home/mosud/Documents/dev3/log_dir:/app/log_dir/ imosudi/rubiks3ubuntufs-kataruntime:v1.4

FROM imosudi/ubuntu-rootfs-osbuilder:v10.0 as builder

#with python3-tk# File Author / Maintainer
MAINTAINER mosudi.pg7331@st.futminna.edu.ng

RUN apt update

#RUN apt install python3.8 python3.8-dev -y

WORKDIR /rubiksapp

COPY requirements.txt  /rubiksapp
RUN pip3 install -r requirements.txt

FROM imosudi/ubuntu-rootfs-osbuilder:v10.0

RUN apt update

RUN apt install apache2 -y

RUN echo "<Directory /var/www/>" >> /etc/apache2/apache2.conf
RUN echo "	Options Indexes FollowSymLinks" >> /etc/apache2/apache2.conf
RUN echo "	AllowOverride All" >> /etc/apache2/apache2.conf
RUN echo "	Require all granted " >> /etc/apache2/apache2.conf
RUN echo "</Directory> " >> /etc/apache2/apache2.conf	 	
     

RUN a2enmod rewrite

COPY /web /var/www/

COPY /web /var/www/html/

CMD ["/etc/init.d/apache2" "start"]

COPY --from=builder /usr/local/lib/python*/dist-packages  /rubiks3app/site-packages

COPY  /rubiks3app .

ENV PORT 80

#CMD ["/usr/bin/python3", "app.py", "/etc/init.d/apache2", "start"]

#CMD ["/etc/init.d/apache2" "start"]
