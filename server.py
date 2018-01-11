import pickle as pickle
import socket
import subprocess
from rot13 import Rot13
import base64
import os
import traceback
rot = Rot13()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # initiallize socket
s.bind(('127.0.0.1', 6666))
s.listen(100)
print('Server listening on %s:%s') % ('127.0.0.1', 6666)
try:
    conn, addr = s.accept()
except KeyboardInterrupt:
    exit()
print('connection from: ' + str(addr))

global password
try:
    f = open(os.getcwd() + '/password.pc', 'r+')
    raw_password = f.read()
    password = rot.decodes(pickle.loads(base64.b64decode(raw_password)))
except Exception as e:
    print(e)
    print("Please set password use 'change password.py'")
    exit(1)


def main():
    try:
        data = conn.recv(1024)
        if str(data).startswith('ZXhpdCgp=='):
            s.close()
            print('Connection Closed')
            exit()
        if str(data).startswith('Y29tbWFuZA=='):
            if not log:
                conn.send('b3V0cHV0Cg==' + 'You are not logged in, please login first.')
                print('Not logged in')
                return False
            raw_command = str(data).split('Y29tbWFuZA==')[1]
            command = raw_command.split(' ')
            print('executing: ' + raw_command)
            try:
                output = subprocess.check_output(command, stderr=subprocess.STDOUT)
            except (subprocess.CalledProcessError, OSError) as e:
                if type(e) == OSError:
                    output = e
                else:
                    output = e.output
            conn.send('b3V0cHV0Cg==' + str(output))
            return True
        if rot.decodes(pickle.loads(base64.b64decode(data))) == password:
            conn.send('correct')
            print('correct password')
            return True
        else:
            conn.send('incorrect')
            print('incorrect password')
            return False
    except KeyboardInterrupt:
        s.close()
        print('Connection Closed')
        exit()


log = False
while True:
    log = main()  # Continuously get return value True or False to verify login.
    continue
