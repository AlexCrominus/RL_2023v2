FROM rl/base:latest

#RUN apt-get install -y python3.8

#WORKDIR /tmp
#RUN wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
#RUN tar zxvf Python-3.8.0.tgz 
#RUN ./Python-3.8.0/configure --prefix=$HOME/opt/python-3.8.0
#RUN make
#RUN make install
#ENV PATH=$HOME/opt/python-3./bin:$PATH

EXPOSE 8080

#copy config files
COPY configs/ /etc/
COPY ./rockyou.txt /rockyou.txt

#ex_flask
COPY ./ex_flask /app/
RUN pip3 install -r /app/requirements.txt

#ex_udp
COPY ./ex_udp /tmp


#configure processes
COPY ./scripts/script.sh /script.sh

ENTRYPOINT [ "sh", "/script.sh" ]
CMD ["/lib/systemd/systemd"]
