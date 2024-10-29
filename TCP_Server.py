import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local host machine name
host = socket.gethostname()

# set port number
port = 8080

# bind the socket to a public host and a port
serversocket.bind((host, port))

# set the number of clients the server can listen to
serversocket.listen(2)

print("Waiting for connections...")

# wait for connections from clients
client1, address1 = serversocket.accept()
print("Client 1 connected from %s:%s" % address1)
client1.send(str("You are client 1").encode('utf-8'))

client2, address2 = serversocket.accept()
print("Client 2 connected from %s:%s" % address2)
client2.send(str("You are client 2").encode('utf-8'))

play_again = True

while play_again:
    # receive integers from both clients
    I1 = int(client1.recv(1024).decode('utf-8'))
    I2 = int(client2.recv(1024).decode('utf-8'))

    # determine the winner
    if I1 == I2:
        result1 = 2
        result2 = 2
    elif abs(I1 - I2) <= 3:
        if I1 > I2:
            result1 = 1
            result2 = 0
        else:
            result1 = 0
            result2 = 1
    else:
        if I1 > I2:
            result1 = 0
            result2 = 1
        else:
            result1 = 1
            result2 = 0

    # send results to both clients
    client1.send(str(result1).encode('utf-8'))
    client2.send(str(result2).encode('utf-8'))

    p1 = str(client1.recv(1024).decode('utf-8'))
    p2 = str(client2.recv(1024).decode('utf-8'))
    if p1=='n' or p2=='n':
        play_again=False
    else:
        play_again=True



# close connections
client1.close()
client2.close()
serversocket.close()
