from cryptography.fernet import Fernet
from tkinter import *
import tkinter as tk
import time

print("Insert E: drive now")
print("="*70)
time.sleep(0.5)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("starting")
time.sleep(1)



root = Tk()
root.title("Encryption")
root.config(bg="White")

top = Frame(root)
top.pack(side=TOP)

bottom = Frame(root)
bottom.pack(side=BOTTOM)

lable1 = Label(top, text="File Path")
lable1.config(fg="Black", bg="White")
lable1.grid(row=0, column=0)

lable2 = Label(top, text="Save")
lable2.config(fg="Black", bg="White")
lable2.grid(row=1, column=0)

path = Entry(top)
path.config(fg="Black", bg="White", relief=SUNKEN, width=30)
path.grid(row=0, column=1)

path2 = Entry(top)
path2.config(fg="Black", bg="White", relief=SUNKEN, width=30)
path2.grid(row=1, column=1)
def generate():
    key = Fernet.generate_key()
    print(key)

    file = open('E:\Keys\key.key', 'wb')
    file.write(key)
    file.close()

def encrypt():
    filepath = path.get()
    filepath2 = path2.get()
    
    of = open(filepath, 'r')
    text = of.read()
    of.close()
    text = text.encode()
    
    file = open('E:\Keys\key.key', 'rb')
    key = file.read()
    file.close()

    f = Fernet(key)
    encrypted = f.encrypt(text)

    ef = open(filepath2, 'wb')
    ef.write(encrypted)
    ef.close()

def decrypt():
    filepath = path.get()
    filepath2 = path2.get()
    
    of = open(filepath, 'rb')
    text = of.read()
    of.close()
    
    file = open('E:\Keys\key.key', 'rb')
    key = file.read()
    file.close()

    f = Fernet(key)
    decrypted = f.decrypt(text)
    decrypted = decrypted.decode()

    ef = open(filepath2, 'w')
    ef.write(decrypted)
    ef.close()
    
b1 = Button(bottom, text="Generate", command=generate)
b1.config(bg="White", relief=RAISED)
b1.grid(row=0, column=0)

b2 = Button(bottom, text="Encrypt", command=encrypt)
b2.config(bg="White", relief=RAISED)
b2.grid(row=0, column=1)

b3 = Button(bottom, text="Decrypt", command=decrypt)
b3.config(bg="White", relief=RAISED)
b3.grid(row=0, column=2)

root.mainloop()
