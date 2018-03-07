# Echo client program
import socket
nick = str(input('Digite sua mensagem: '))
HOST = '10.24.4.102'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    enc = nick.encode('utf-8')
    s.sendall(b'Joallison: %s'% (enc))
    data = s.recv(1024)
print('Recebido: ', repr(data))
