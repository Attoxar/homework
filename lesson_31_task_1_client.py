import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    while True:
        message = input("Enter message to send: ")
        client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
        response, server_address = client_socket.recvfrom(1024)
        print("Received response from {}: {}".format(server_address, response.decode()))
