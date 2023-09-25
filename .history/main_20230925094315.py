import socket

def scan_port(ip, port):
    """_summary_
    Args:
        ip (_type_): _address_
        port (_type_): _any_
    """
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
    """_summary_
    Args:
        ip (0.0.0.0): Address
        port_list (00000): Any
    """
    for port in port_list:
        scan_port(ip, port)
        
def main():
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    port_range = range(start_port, end_port + 1)

    print(f"Scanning {target_ip} from port {start_port} to {end_port}")
    scan_ports(target_ip, port_range)

if __name__ == "__main__":
    main()