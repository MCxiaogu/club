import pickle as pickle
import socket
import subprocess
from rot13 import Rot13
import base64
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 6666))
s.listen(100)
try:
    conn, addr = s.accept()
except KeyboardInterrupt:
    exit()
print('connection from: ' + str(addr))

global password
try:
    f = open(os.getcwd() + '/password.pass', 'r+')
    password = f.read()
except Exception as e:
    raise e
print(password)
def main():
    try:
        data = conn.recv(1024)
        if str(data).startswith('Y29tbWFuZA=='):
            raw_command = str(data).split('Y29tbWFuZA==')[1]
            command = raw_command.split(' ')
            print('executing: ' + raw_command)
            try:
                output = subprocess.check_output(command)
                print(output)
            except Exception as e:
                output = str(e)
            conn.send('b3V0cHV0Cg==' + output)
            return
        if pickle.loads(base64.b64decode(data)) == pickle.loads(base64.b64decode(password)):
            conn.send(pickle.dumps('correct'))
            print('correct password')
            return
        else:

            conn.send('incorrect')
            print('wrong password')
            return
    except KeyboardInterrupt:
        s.close()
        print('Connection Closed')
        exit()


while True:
        main()
