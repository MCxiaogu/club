import socket
import pickle
import tkMessageBox as messagebox
from Tkinter import *
from functools import partial
from tkinter.scrolledtext import *
import time
from rot13 import Rot13
import base64
import traceback
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
global port
port = 6666
rot = Rot13()
def pass_auth():
    password = e2.get()
    try:
        if password == '':
            messagebox.showinfo('Input password', 'Please input password.')
            return
        s.send(base64.b64encode(pickle.dumps(rot.encodes(password))))
    except Exception, e:
        messagebox.showwarning(title='Error', message=e)
        return
    auth = s.recv(1024)
    if auth != 'correct':
        messagebox.showwarning(title='incorrect password', message='Incorrect password!')
        return
    else:
        messagebox.showinfo(title='Successful', message='Successfully login')
        return


def connect():
    ip = e1.get()
    if not ip == '':
        pass
    else:
        messagebox.showwarning(title='Invalid input', message='Please input the right ip.')
        return
    try:
        s.settimeout(4)
        s.connect((str(ip), port))
        messagebox.showinfo(title='connected', message='Successfully connected!')
        s.settimeout(0)
    except Exception as e:
        messagebox.showwarning(title='Error', message=sys.exc_info()[1])


def execute():
    command = e3.get()
    if not command == '':
        pass
    else:
        messagebox.showinfo(title='input command', message='Please input command.')
        return
    try:
        s.send('Y29tbWFuZA==' + str(command))
    except Exception as e:
        messagebox.showwarning(title='Error', message=e)
        return
    raw_output = s.recv(1024)
    if raw_output.startswith('b3V0cHV0Cg=='):
        timee = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        t1.config(state=NORMAL)
        output = timee + ' command: ' + str(command) + '\n' + raw_output.split('b3V0cHV0Cg==')[1] + '\n'
        t1.insert(END, output)
        t1.config(state=DISABLED)


def show_password():
    if not e2.get() == '':
        messagebox.showinfo(title='password', message=e2.get())
    else:
        messagebox.showinfo(title='input password', message='Please input password.')


def quit():
    try:
        s.send('ZXhpdCgp==')
    except Exception as e:
        pass
    s.close()
    print('Connection Closed')
    exit()

root1 = Tk()
root1.title('Server Login')
l1 = Label(root1, text='Server Login', font=('', 30))
l2 = Label(root1, text='Input server ip here:')
l3 = Label(root1, text='Input server password here:')
l4 = Label(root1, text='Command execute on server')
l5 = Label(root1, text='Execute log', font=('', 25))
e1 = Entry(root1)
e2 = Entry(root1, show='*')
e3 = Entry(root1)
b1 = Button(text='connect', command=connect)
b2 = Button(text='login', command=partial(pass_auth))
b3 = Button(text='exit', command=quit)
b4 = Button(text='Execute on server', command=execute)
b5 = Button(text='Show password', command=show_password)
t1 = ScrolledText(root1, bg='black', fg='white', height=10, width=70)
l1.pack()
l2.pack()
e1.pack()
b1.pack()
l3.pack()
e2.pack()
b2.pack()
b5.pack()
l4.pack()
e3.pack()
b4.pack()
l5.pack()
t1.pack()
b3.pack()
try:
    t1.config(state=DISABLED)
    root1.resizable(width=False, height=False)
    root1.mainloop()
except KeyboardInterrupt:
    pass
    s.close()
    print('Connection Closed')
