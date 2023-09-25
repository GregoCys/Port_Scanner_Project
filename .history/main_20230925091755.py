import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) 
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open.")
    else:
        print(f"Port {port} is closed.")
    sock.close()

def scan_ports(ip, port_list):
    for port in port_list:
        scan_port(ip, port)
        
common_ports = [21, 22, 25, 53, 80, 110, 143, 443, 587]

scan_ports("google.com", common_ports)  