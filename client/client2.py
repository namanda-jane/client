import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
client.connect(('localhost', 1234))

# Check if file exists
if not os.path.exists('pic.jpg'):
    print("File not found!")
    client.close()
    exit()

# Read file data
with open('pic.jpg', 'rb') as file:
    file_data = file.read()  

# Send file size first
file_size = len(file_data)
client.sendall(str(file_size).encode()) 

# Wait for server ready message
ready_msg = client.recv(1024) 
print(f"Server says: {ready_msg.decode()}")

# Send file in chunks
bytes_sent = 0
chunk_size = 4096

print(f"Sending {file_size} bytes of data...")
while bytes_sent < file_size:
    chunk = file_data[bytes_sent:bytes_sent + chunk_size]
    client.sendall(chunk)  
    bytes_sent += len(chunk)
    print(f"Sent {bytes_sent} bytes out of {file_size} bytes")

# Get final confirmation
confirmation = client.recv(1024)
print(f"Server says: {confirmation.decode()}")
print("File sent successfully!")

client.close()
print("Connection closed")