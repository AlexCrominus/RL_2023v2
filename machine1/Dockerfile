FROM rl/base:latest

#RUN apt-get install -y python3-pip

#copy config files
COPY configs/ /etc/
COPY ./rockyou.txt /rockyou.txt

#ex_flask
COPY ./ex_flask /app/
RUN python3 -m pip install -r /app/requirements.txt

#configure processes
COPY ./scripts/script.sh /script.sh
#RUN sh /script.sh

ENTRYPOINT [ "sh", "/script.sh" ]
CMD ["/lib/systemd/systemd"]
