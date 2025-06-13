
import socket
import os
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
client.connect(('localhost', 1234))

picture = open('pic.jpg', 'rb')  
if not os.path.exists('pic.jpg'):
    print(f"File not found!")
    client.close()
    exit()

with open('pic.jpg', 'rb') as file:
    picture_data = file.read()  

picture_size = len(picture_data)
client.sendall(str(picture_size).encode()) 
readymessage = client.recv(1024) 
print(f"Friend says: {readymessage.decode()}")
bytes_sent = 0
chunk_size = 4096

print(f"Sending {picture_size} bytes of data...")

while bytes_sent < picture_size:
    chunk = picture_data[bytes_sent:bytes_sent + chunk_size]
    client.sendall(chunk)  
    bytes_sent += len(chunk)
    print(f"Sent {bytes_sent} bytes out of {picture_size} bytes")

thanks_message = client.recv(1024)  # Wait for the server's acknowledgment
print(f"Friend says: {thanks_message.decode()}")
print("Image sent successfully!")
client.close()  # Close the socket connection


# import socket
# import os

# # Create a TCP/IP socket
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# try:
#     # Connect to the server
#     client.connect(('localhost', 1234))
#     print("Connected to server")
    
#     # Wait for server's initial question
#     server_question = client.recv(1024).decode()
#     print(f"Server says: {server_question}")
    
#     # Send response (always 'yes' in this case since we're sending a file)
#     client.sendall(b"yes")
    
#     # Check if picture exists
#     picture_path = 'pic.jpg'
#     if not os.path.exists(picture_path):
#         print(f"Error: File '{picture_path}' not found!")
#         client.close()
#         exit()
    
#     # Read picture data
#     with open(picture_path, 'rb') as file:
#         picture_data = file.read()
    
#     # Send picture size first
#     picture_size = len(picture_data)
#     client.sendall(str(picture_size).encode())
#     print(f"Sent picture size: {picture_size} bytes")
    
#     # Wait for server to be ready
#     ready_message = client.recv(1024).decode()
#     print(f"Server says: {ready_message}")
    
#     # Send picture data in chunks
#     bytes_sent = 0
#     chunk_size = 4096
    
#     print(f"Sending {picture_size} bytes of data...")
#     while bytes_sent < picture_size:
#         chunk = picture_data[bytes_sent:bytes_sent + chunk_size]
#         client.sendall(chunk)
#         bytes_sent += len(chunk)
#         print(f"Sent {bytes_sent} bytes out of {picture_size} bytes")
    
#     # Get final acknowledgment
#     thanks_message = client.recv(1024).decode()
#     print(f"Server says: {thanks_message}")
#     print("Image sent successfully!")

# except Exception as e:
#     print(f"Error occurred: {e}")
# finally:
#     client.close()
#     print("Connection closed")


import socket
import os

# Create a TCP/IP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
connection_success = True
if client.connect_ex(('localhost', 1234)) != 0:
    print("Failed to connect to server")
    connection_success = False

if connection_success:
    print("Connected to server")
    
    # Wait for server's initial question
    server_question = client.recv(1024)
    if not server_question:
        print("Server disconnected unexpectedly")
        client.close()
        exit()
    
    print(f"Server says: {server_question.decode()}")
    
    # Send response
    client.sendall(b"yes")
    
    # Check if picture exists
    picture_path = 'pic.jpg'
    if not os.path.exists(picture_path):
        print(f"Error: File '{picture_path}' not found!")
        client.close()
        exit()
    
    # Read picture data
    with open(picture_path, 'rb') as file:
        picture_data = file.read()
    
    # Send picture size first
    picture_size = len(picture_data)
    if client.sendall(str(picture_size).encode()) is not None:
        print("Failed to send picture size")
        client.close()
        exit()
    
    print(f"Sent picture size: {picture_size} bytes")
    
    # Wait for server to be ready
    ready_message = client.recv(1024)
    if not ready_message:
        print("Server disconnected unexpectedly")
        client.close()
        exit()
    
    print(f"Server says: {ready_message.decode()}")
    
    # Send picture data in chunks
    bytes_sent = 0
    chunk_size = 4096
    
    print(f"Sending {picture_size} bytes of data...")
    while bytes_sent < picture_size:
        chunk = picture_data[bytes_sent:bytes_sent + chunk_size]
        if client.sendall(chunk) is not None:
            print("Failed to send picture data")
            client.close()
            exit()
        bytes_sent += len(chunk)
        print(f"Sent {bytes_sent} bytes out of {picture_size} bytes")
    
    # Get final acknowledgment
    thanks_message = client.recv(1024)
    if not thanks_message:
        print("Server disconnected unexpectedly")
    else:
        print(f"Server says: {thanks_message.decode()}")
        print("Image sent successfully!")

client.close()
print("Connection closed")

               