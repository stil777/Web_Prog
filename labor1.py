#lab_1.echo-server

import socket

host = "127.0.0.1"
port = 5003
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print "Listen to the port: ", port

conn, address = s.accept()
print "Connection address: ", address

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print "Received data: ", data
    conn.send(data)  # echo
conn.close()