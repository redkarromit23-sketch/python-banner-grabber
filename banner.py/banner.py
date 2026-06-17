import socket

ip = input("Enter IP: ")
port = int(input("Enter Port: "))

s = socket.socket()

s.connect((ip, port))

s.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

banner = s.recv(1024)

print(banner.decode())

s.close()