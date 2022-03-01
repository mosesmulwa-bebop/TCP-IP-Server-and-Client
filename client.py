import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
#print(f"connecting to %s port %s{server_address}")
print('Connecting to {0} on port:{1}'.format(server_address[0], server_address[1]))

#The client program sets up its socket differently from the way a server does. 
#Instead of binding to a port and listening, it uses connect() to attach the socket directly to the remote address.
sock.connect(server_address)

try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    print(f"sending {message}")

    sock.sendall(message.encode('utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f"received: {data}")

#When the entire message is sent and a copy received, the socket is closed to free up the port.
finally:

    print("closing socket")
    sock.close()
