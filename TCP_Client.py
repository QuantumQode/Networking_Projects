import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local host machine name
host = socket.gethostname()

# set port number
port = 8080

# connect to the server
clientsocket.connect((host, port))

# recieve client number id
ClientNum = str(clientsocket.recv(1024).decode('utf-8'))
print(ClientNum)

# loop to play multiple games
play_again = True
while play_again:
    # prompt user for input
    I = input("Enter an integer between 0 and 9: ")

    # send integer to server
    clientsocket.send(I.encode('utf-8'))

    # receive result from server
    result = int(clientsocket.recv(1024).decode('utf-8'))

    # print result
    if result == 1:
        print("You win!")
    elif result == 0:
        print("You lose!")
    elif result == 2:
        print("Draw!")

    # prompt user to play again
    play_again_input = input("Do you want to play again? (y/n) ")
    if play_again_input.lower() == 'y':
        clientsocket.send(play_again_input.encode('utf-8'))
        play_again = True
    else:
        clientsocket.send(play_again_input.encode('utf-8'))
        play_again = False

# close connection
clientsocket.close()
