import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 1234))
server.listen(1)
print("Server ready. Waiting for connection...")

conn, addr = server.accept()
print(f"Connected to {addr}")

# Receive file size first
size_data = conn.recv(1024)
file_size = int(size_data.decode())
print(f"Receiving file of size: {file_size} bytes")

# Send ready confirmation
conn.sendall(b"Ready to receive file")

# Receive file data
received_data = b""
bytes_received = 0

print(f"Receiving {file_size} bytes of data...")
while bytes_received < file_size:
    chunk = conn.recv(4096)
    if not chunk:
        break
    received_data += chunk
    bytes_received += len(chunk)
    print(f"Received {bytes_received} bytes out of {file_size} bytes")

# Save the file
with open("received_image.jpg", "wb") as f:
    f.write(received_data)

print("File received successfully!")
conn.sendall(b"File received successfully")
conn.close()
server.close()
print("Server connection closed")