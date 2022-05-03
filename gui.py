import tkinter as tk
from tkinter import *
from tkinter import ttk
import caesarCipher
import vigenere
import randomCipher

class window(Frame) :
    c = ""
    e = ""
    inputText = ""

    def __init__(self) :
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Crypto Cipher")
        # self.dropDown = ttk.Combobox(   )
        # self.geometry('800x600+50+50')
        self.cipherSelection = tk.StringVar()
        self.ciphers = ttk.Combobox(self, textvariable=self.cipherSelection)
        self.ciphers ['values'] = ('Caesar Cipher',
                                   'Vignere Cipher',
                                   'Random Cipher')
        self.ciphers.grid(column=1, row=1)
        self.eD = tk.StringVar()
        self.encryptDecrypt = ttk.Combobox(self, textvariable=self.eD)
        self.encryptDecrypt ['values'] = ('Encrypt', 'Decrypt')
        self.encryptDecrypt.grid(column=1, row=2)

        self.inputMsg = tk.Entry(self)
        self.inputKey = tk.Entry(self)
        self.result = tk.Entry(self)

        self.inputMsg.grid(column=2, row=1)
        self.inputKey.grid(column=2, row=2)
        self.result.grid(column=3, row=2)

        def getCipher() :
            c = self.ciphers.get()
            e = self.eD.get()
            m = self.inputMsg.get()
            k = self.inputKey.get()
            if c == "Caesar Cipher" and e == "Encrypt" :
                print(caesarCipher.shiftEncrypt(m, k))
                self.result.insert(0, str(caesarCipher.shiftEncrypt(m, k)))

        self.goButton = tk.Button(self, text = "Go!", command=getCipher)  
        self.goButton.grid(column=1,row=3)

# def window():
#     window = tk.Tk()
#     window.title("Crypto Cipher")
#     window.geometry('800x600+50+50')
#     cipherSelection = tk.StringVar()
#     ciphers = ttk.Combobox(window, textvariable=cipherSelection)
#     ciphers ['values'] = ('Caesar Cipher',
#                           'Vignere Cipher',
#                           'Random Cipher')
#     ciphers.grid(column=1,row=10)

#     eD = tk.StringVar()
#     encryptDecrypt = ttk.Combobox(window, textvariable=eD)
#     encryptDecrypt ['values'] = ('Encrypt', 'Decrypt')
#     encryptDecrypt.grid(column=2,row=10)

#     print(cipherSelection.get())
#     print(eD.get())

#     goButton = tk.Button(window, text = "Go!", command=getCipher(cipherSelection.get(), eD.get()))
    
#     goButton.grid(column=1,row=15)
    
        
#     # if cipherSelection == "Caesar Cipher" and eD == "Encrypt":
#     #     goButton = tk.Button(window, text = "Go!", command=caesarCipher.shiftEncrypt("hello", 2))
#     #     goButton.grid(column=1,row=11)
#     #     goButton.place(x=10, y=10)
#     #     goButton.pack()
#     ciphers.current()
#     window.mainloop()

def main() :
    window().mainloop()

if __name__ == '__main__':
    main()

# class karl( Frame ):
#     def __init__( self ):
#         tk.Frame.__init__(self)
#         self.pack()
#         self.master.title("Karlos")
#         self.button1 = Button( self, text = "CLICK HERE", width = 25,
#                                command = self.new_window )
#         self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
#     def new_window(self):
#         self.newWindow = karl2()
# class karl2(Frame):     
#     def __init__(self):
#         new =tk.Frame.__init__(self)
#         new = Toplevel(self)
#         new.title("karlos More Window")
#         new.button = tk.Button(  text = "PRESS TO CLOSE", width = 25,
#                                  command = self.close_window )
#         new.button.pack()
#     def close_window(self):
#         self.destroy()
# def main(): 
#     karl().mainloop()
# if __name__ == '__main__':
#     main()