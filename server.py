from config import allowed_connections, ip_address, port
from threading import Thread
import socket
import time
import sys

# Initialize the server and specify the connection type.
def initialize_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    server.bind((ip_address, port))

    # Define the number of connections to listen for.
    server.listen(allowed_connections)
    return server

# Listen for new messages.
def listen_for_message(conn, client_list):
    while True:
        try:
            message = conn.recv(1024).decode()
        except:
            client_list.remove(conn)
        
        send_message_to_all(message, client_list)

# Send message to each of the connected clients.
def send_message_to_all(message, client_list):
    for client in client_list:
        client.send(message.encode())
    print(message)

def main():

    server = initialize_server()    # Initialize the server.
    client_list = []                # Initializing an empty list of client connections.

    while True:
        # Listen for new connections to add to client list.
        conn, addr = server.accept()
        print("Recieved connection.")
        username = conn.recv(1024).decode()
        client_list.append(conn)

        # Display a welcome message when a new user enters the room.
        welcome_message = username + " has joined the chat room."
        send_message_to_all(welcome_message, client_list)

        # Start a thread that will listen for new messages from the connection.
        thread = Thread(target=listen_for_message, args=(conn, client_list,))
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    main()




