# Networking_Projects
This repository contains a series of networking tasks completed as part of the Computer Networking module at university.

Socket Programming - Client-Server Game
This project implements a networked game using Python sockets over TCP. The server coordinates a game between two clients, where each client sends a chosen integer (0-9).
The game rules determine a winner based on modulo operations, similar to rock-paper-scissors.

Project Details

Features: 
- Client and Server Communication: Each client connects to the server over TCP, sending a number (0-9).
  The server then calculates the result using modulo 3 and sends back the game outcome.
- Game Logic: The game result depends on the remainder of each client’s number divided by 3, with rules as follows:
  - 1 wins over 0, 2 wins over 1, and 0 wins over 2.
  - If both clients have the same result, the game is a draw.
- Outcome Handling: Based on the calculation, each client receives a message—W (win), L (lose), or D (draw)—and displays the corresponding
  message (“You win!”, “You lose!”, or “Draw!”).

Code Structure
- Client Code: Prompts the user for an integer input, connects to the server, sends the integer, and waits for the result.
  Once received, it displays the appropriate message and disconnects.
- Server Code: Waits for two clients to connect, collects their inputs, computes the winner based on modulo rules, and sends
  each client their result.

Execution Flow
1. Client Connection: Each client initiates a connection and submits a number.
2. Result Calculation: The server computes the result after receiving both inputs.
3. Response and Termination: Each client receives and displays the result before disconnecting.

This project demonstrates skills in Python networking, TCP protocol usage, client-server architecture, and network communication.


