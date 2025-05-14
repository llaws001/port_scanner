import socket
ip = input("Enter the IP you wish to scan: ")


for port in range(20,1024):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print(f"{port} is open")
        s.close()
    except ConnectionRefusedError as e:
        print(f"Connection on {port} refused")
    finally:
        s.close()