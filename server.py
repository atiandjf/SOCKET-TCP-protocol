# we are going to define a socket, and use the socket function.
# def socket() == the function takes 2 input of IP address which is either IP4 or IP 6,
# and protocol including TCP or UDP
import socket
s = socket.socket()
print("Socket Created")

# we are going to bind the IP address and port number with
# port number is 9999 which is free and local host is for IP address
# FYI port number range change from 0 to 65535
# remember pass (IP, port number) as one object not two, by putting (())
s.bind(('localhost', 9999))

# we have to define how many clients we will need?let say 3 clients
s.listen(3)
print("waiting for connections:")

# we are going to make server to keep accepting the clients
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with:", addr, name)

    c.send(bytes('Welcome to Atia Server', 'utf-8'))
    print("successful connection")
    c.close()



