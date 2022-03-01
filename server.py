import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# First parameter: IP address
# Second parameter: Port to be used
server_address = ('localhost', 10000)

#print(f"starting up on %s port: {server_address}")
print('Starting up {0} on port:{1}'.format(server_address[0], server_address[1]))


#The bind() method of Python's socket class assigns an IP address and a port number to a socket instance.
#The bind() method is used when a socket needs to be made a server socket.
sock.bind(server_address)

# Listen for incoming connections, Calling listen() puts the socket into server mode
sock.listen(1)

try:
    while True:
        # Wait for a connection

        print("waiting for a connection")
        # accept() waits for an incoming connection.
        #accept() returns an open connection between the server and client, along with the address of the client.
        connection, client_address = sock.accept()

        try:
            #Data is read from the connection with recv() and transmitted with sendall().
            print(f"connection from {client_address}")

            # Receive the data in small chunks and retransmit it
            while True:
                #recv arguments - receive_size
                #here we use 16 meaning we can receive at most 16 bytes
                data = connection.recv(16)
                print(f"Received: {data}")

                if data:

                    print("Sending data back to the client")
                    connection.sendall(data)
                else:
                    print(f"No more data from {client_address}")
                    break

        # When communication with a client is finished, the connection needs to be cleaned up using close(). 
        # This example uses a try:finally block to ensure that close() is always called, even in the event of an error.            
        finally:
            # Clean up the connection
            connection.close()
except KeyboardInterrupt:
    #if you press CTRL-C
    print("Server stopped by the user")
    pass
