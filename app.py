import socket

def scan_port(target, port):
    try:
        # Try to connect to the given port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second
        result = sock.connect_ex((target, port))  # Try to connect
        if result == 0:
            print(f"Port {port} is open on {target}")
        else:
            print(f"Port {port} is closed on {target}")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def scan_ports(target, ports):
    for port in ports:
        scan_port(target, port)

# Example usage
target = "127.0.0.1"  # Change to your target IP
ports = [22, 80, 443, 21]  # List of ports to scan (SSH, HTTP, HTTPS, FTP)
scan_ports(target, ports)

