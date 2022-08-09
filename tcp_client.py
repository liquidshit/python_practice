from xmlrpc import client
import socket
target_url = 'google.com'
target_port = 80
#target_url = input('target url: ')
#target_port = input('target port: ')

#socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#est. connection
client.connect((target_url, target_port))

# send data
client.send(b'GET  /  HTTP/1.1\r\nHOST: google.com\r\n\r\n')

# receive data
response = client.recv(4096)

print(response.decode())
client.close()
