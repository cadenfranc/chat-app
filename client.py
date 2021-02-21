import socket
import sys
from threading import Thread

# Create a thread that listens for new messages and prints them.
def listen_for_message(server):
    while True:
        message = server.recv(1024).decode()
        print(message)

def main():
    # Connect to the server.
    server = socket.socket()
    ip_address = input("Please input a valid IP address: ")
    server.connect((ip_address, 215))

    client = input("Enter name: ")

    server.send(client.encode())
    print(server.recv(1024).decode())

    thread = Thread(target=listen_for_message, args=(server,))
    thread.daemon = True
    thread.start()

    # Allows the user to send messages to the server.
    while True:
        message = input()

        # Exit code.
        if message == "/exit":
            break

        server.send(("<" + client + "> " + message).encode())

    # Close the server connection when finished.
    server.close()

if __name__ == "__main__":
    main()