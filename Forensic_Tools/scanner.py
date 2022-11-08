import socket

host = input("enter host to scan: ")

for port in range(1,65535):
    socky = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = socket.gethostbyname(host)
    #print(f"Testing {port}....")
    try:
        results = socky.connect_ex((ip, port))
    except:
        print("Error")
    if results == 0:
        print(f"{port}: OPEN")

