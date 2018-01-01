import pickle
from Tkinter import *
import tkMessageBox as Messagebox
import tkFileDialog as Filedialog
import os


def change_password():
    global _file
    if os.path.exists(os.getcwd() + '/pass.password') == False:
        open(os.getcwd() + '/pass.password', mode='w')
        Messagebox.showinfo(title='Created file',
                            message='Successfully created password file in ' + os.getcwd() + '/pass.password. Please change the password.')
        return
    else:
        try:
            _file = open(os.getcwd() + '/pass.password', mode='w+')
        except Exception as e:
            Messagebox.showerror(title='Error', message=e)
        new = e1.get()
        if new == '':
            Messagebox.showwarning(title='Input password', message='Please input new password.')
            return
        try:
            pickle.dump(new, _file)
            _file.close()
            Messagebox.showinfo(title='Successful', message='Successfully saved password, your password is: ' + new)
        except Exception as e:
            Messagebox.showerror(title='Error', message=e)
        return


root = Tk()
l1 = Label(root, text='Change Password Tool', font=('', 28))
l2 = Label(root, text='New password:')
e1 = Entry(root, show='*')
b1 = Button(root, text='Change password', command=change_password)
l1.pack()
l2.pack()
e1.pack()
b1.pack()
root.title('Change Password Tool')
root.resizable(width=False, height=False)
root.mainloop()
