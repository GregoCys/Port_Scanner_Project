import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK.STREAM)
    sock.settimeout(1) 
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open.")
    else:
        print(f"Port {port} is closed.")
    sock.close()
    
scan_port("google.com", 80)