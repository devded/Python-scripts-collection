import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(f"Your Computer Name is:{hostname}")
print("\nYour Computer IP Address is:" + IPAddr)