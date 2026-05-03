import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 3000))
server.listen(1)
print("Server started...")
conn, addr = server.accept()
print("Connected:", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Received:", data.decode())
