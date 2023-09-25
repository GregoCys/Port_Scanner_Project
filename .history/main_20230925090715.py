import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK.STREAM)
    sock.settimeout(1) 
    result = sock.connect_ex((ip, port))
