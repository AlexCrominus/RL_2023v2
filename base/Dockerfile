FROM ubuntu:22.04

# required for systemd
ENV container docker
ENV TERM xterm-256color
STOPSIGNAL SIGRTMIN+3

# sshd
EXPOSE 22/tcp

# install necessary packages
RUN apt-get update

RUN apt-get install -y --no-install-recommends libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev 
RUN apt-get install -y --no-install-recommends libtk8.6 
RUN apt remove libpython3.10-minimal libpython3.10-stdlib
RUN apt-get install -y dialog apt-utils openssh-server 
RUN apt-get install -y systemd openssl python3-pip
RUN apt-get install -y sudo locales vim dbus nano curl wget bash-completion
RUN apt-get install -y udev ifupdown ssh telnet rsync ftp 
RUN apt-get install -y net-tools iputils-ping iproute2 traceroute tcpdump dsniff 
RUN apt-get install -y dnsutils netcat vsftpd apache2 telnetd 
RUN apt-get install -y --no-install-recommends libpcap-dev libdb4o-cil-dev libgdm-dev
RUN rm -rf /var/lib/apt/lists/*

# Set the locale
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Systemd: disable optional services
RUN find /etc/systemd/system \
	/lib/systemd/system \
	-path '*.wants/*' \
	-not -name '*journald*' \
	-not -name '*systemd-tmpfiles*' \
	-not -name '*systemd-user-sessions*' \
	-exec rm \{} \; && \
	systemctl set-default multi-user.target

CMD ["/lib/systemd/systemd"]
