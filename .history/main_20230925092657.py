import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open.")
        else:
            print(f"Port {port} is closed.")
        sock.close()
    except Exception as e:
        print(f"An error occurred: {e}")
        
def scan_ports(ip, port_list):
    for port in port_list:
        scan_port(ip, port)
        
common_ports = [21, 22, 25, 53, 80, 110, 143, 443, 587]

scan_ports("google.com", common_ports)  

target_ip = input("Enter the target IP address: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

port_range = range(start_port, end_port + 1)

scan_ports(target_ip, port_range)