import socket

def send_file():
    filename = input("Enter the filename: ")
    ip_address = input("Enter the destination IP address: ")
    port = int(input("Enter the port number: "))

    try:
        with open(filename, 'rb') as file:
            data = file.read()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.sendall(data)

        print(f"File '{filename}' sent successfully to {ip_address}:{port}")
    except Exception as e:
        print(f"Error sending file: {e}")

if __name__ == "__main__":
    send_file()
