import socket
import threading
import asyncio

# Server configuration
HOST = '127.0.0.1'
PORT = 5555
clients = []

async def counter():
    """Asynchronous counter that broadcasts messages."""
    count = 0
    while True:
        print(f"Counter: {count}")
        broadcast_message(f"Counter: {count}")
        count += 1
        await asyncio.sleep(1)

async def counter2():
    """Second asynchronous counter for demonstration."""
    count = 0
    while True:
        print(f"Counter2: {count}")
        broadcast_message(f"Counter2: {count}")
        count += 1
        await asyncio.sleep(1)

def start_server():
    """Initialize the server and start listening for clients."""
    server_socket = setup_server()
    print(f"Server listening on {HOST}:{PORT}...")
    threading.Thread(target=accept_clients, args=(server_socket,)).start()
    asyncio.run(start_counters())

def setup_server():
    """Set up the server socket."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    return server_socket

def accept_clients(server_socket):
    """Continuously accept and handle new clients."""
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"New client connected: {client_address}")
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

def handle_client(client_socket, client_address):
    """Handle communication with a single client."""
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from {client_address}: {data.decode()}")
    except:
        pass
    finally:
        disconnect_client(client_socket, client_address)

def broadcast_message(message):
    """Broadcast a message to all connected clients."""
    for client in clients:
        try:
            client.sendall(message.encode())
        except:
            clients.remove(client)

def disconnect_client(client_socket, client_address):
    """Remove a client and close its connection."""
    if client_socket in clients:
        clients.remove(client_socket)
    client_socket.close()
    print(f"Client disconnected: {client_address}")

async def start_counters():
    """Start both asynchronous counters."""
    await asyncio.gather(counter(), counter2())

# Start the chat server
if __name__ == "__main__":
    start_server()
