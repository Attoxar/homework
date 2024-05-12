import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((SERVER_IP, SERVER_PORT))
    print("UDP server is listening...")
    while True:
        data, client_address = server_socket.recvfrom(1024)
        print("Received message from {}: {}".format(client_address, data.decode()))
        server_socket.sendto(data, client_address)
