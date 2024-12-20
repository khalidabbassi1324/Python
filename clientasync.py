import socket
import threading

# Handle receiving messages from the server
def receive_messages(client_socket):
    """Continuously receive and display messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                # Server closed the connection
                break
        except:
            print("Connection lost")
            break

# Send messages to the server
def send_message(client_socket):
    """Continuously read user input and send it to the server."""
    while True:
        try:
            message = input()
            if message:
                client_socket.send(message.encode('utf-8'))
        except:
            print("Connection lost")
            break

# Connect to the server
def start_client():
    """Initialize the client, connect to the server, and handle communication."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('127.0.0.1', 5555))  # Connect to the server
        print("Connected to the server")
    except:
        print("Unable to connect to the server")
        return

    # Start the receive and send threads
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    send_message(client_socket)

if __name__ == "__main__":
    start_client()
