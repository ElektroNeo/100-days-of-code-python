import socket

# Connect to host
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('w3.org', 80))
cmd = 'GET https://www.w3.org/TR/PNG/iso_8859-1.txt HTTP/1.0\n\n'.encode()
sock.send(cmd)

# Receive text
while True:
    data = sock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
sock.close()