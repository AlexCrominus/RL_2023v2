#!/bin/bash

#add users 
KEY=$(shuf -n 1 /rockyou.txt)

#delete this in production :P
echo $KEY > /key
#also shorten the list cuz rockyou would take to long

adduser cr0minus
mkdir -p /home/cr0minus/.ssh
chown -R cr0minus:cr0minus /home/cr0minus/.ssh
sudo -u cr0minus chmod 700 /home/cr0minus/.ssh
sudo -u cr0minus ssh-keygen -t rsa -f /home/cr0minus/.ssh/id_rsa -N "$KEY"
sudo -u cr0minus cp /home/cr0minus/.ssh/id_rsa.pub /home/cr0minus/.ssh/authorized_keys
sudo -u cr0minus chmod 600 /home/cr0minus/.ssh/authorized_keys
echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
echo "AuthorizedKeysFile %h/.ssh/authorized_keys" >> /etc/ssh/sshd_config
echo "CONGRATULATIONS!!! HERE IS YOUR FLAG: RL{$(sha256sum /key | awk '{print $1}' )}" > /etc/motd
#create ftp exercise
mkdir -p /srv/ftp/.../
echo "Draga student la RL,\nNu stiu ce am facut, dar mi-am pierdut pe undeva cheia de la cont :P\n~cr0minus" > /srv/ftp/notes
cp /home/cr0minus/.ssh/id_rsa /srv/ftp/.../id_rsa
rm /home/cr0minus/.ssh/id_rsa
chmod 666 /srv/ftp/.../id_rsa

sudo sudo chsh -s /bin/false cr0minus

#enable services
systemctl enable vsftpd
systemctl enable ssh
systemctl enable apache2

#delete all shells so that docker exec no longer works
#hopefully it works
mkdir -p /bin/.../
cp /bin/sh /bin/.../c0nn3ct
#rm /bin/bash /bin/rbash /bin/dash /bin/sh

#TO DO 
# add iptables rules to deny requests to the internet 
# remove python3 wget curl and any other clients
# make sure ftp doesnt have write permissions

sudo openssl genrsa -out /app/private.pem 2048
sudo openssl rsa -in /app/private.pem  -out /app/public.pem -RSAPublicKey_out -outform PEM
nohup python3 /app/src/server.py > log.txt 2>&1 &

exec "$@"