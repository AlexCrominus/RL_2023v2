import socket
import random
import hashlib

def udp_server():
    host = '0.0.0.0'
    port = random.randint(10000, 65535)
    flag = "RL{" + str(hashlib.sha256('admin'.encode('utf-8')).hexdigest()) + "}"

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    while True:
        data, address = server_socket.recvfrom(1024)
        server_socket.sendto(flag.encode(), address)

    server_socket.close()

if __name__ == "__main__":
    udp_server()

