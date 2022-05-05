import tkinter as tk
from tkinter import *
from tkinter import ttk

from pyparsing import White
import caesarCipher
import vigenere
import randomCipher

class window(Frame) :
    c = ""
    e = ""
    inputText = ""

    def __init__(self) :
        self.win = Tk()
        self.win.geometry('800x400')
        color = "#222222"
        fontcolor = "#ffffff"
        self.win.configure(bg=color)
        
        tk.Frame.__init__(self)
        self.configure(bg=color)
        self.pack()
        self.master.title("Crypto Cipher")
        
        self.cipherLabel = tk.Label(self, text="Cipher", bg=color, fg=fontcolor, font=('Arial', 12))
        self.eDLabel = tk.Label(self, text="Action", bg=color, fg=fontcolor, font=('Arial', 12))

        self.cipherLabel.grid(column=0, row=1, padx=2, pady=5)
        self.eDLabel.grid(column=0, row=3, padx=2, pady=5)
        
        self.cipherEntry = tk.Label(self, text="Enter plaintext", bg=color, fg=fontcolor, font=('Arial', 12))
        self.cipherKey = tk.Label(self, text="Enter key", bg=color, fg=fontcolor, font=('Arial', 12))
        self.result = tk.Label(self, text="Result", bg=color, fg=fontcolor, font=('Arial', 12))

        self.cipherEntry.grid(column=2, row=0, padx=15, pady=(80, 0))
        self.cipherKey.grid(column=2, row=2, padx=15, pady=(15, 0))
        self.result.grid(column=3, row=1, padx=15, pady=(15, 0))

        self.cipherSelection = tk.StringVar()
        self.ciphers = ttk.Combobox(self, textvariable=self.cipherSelection)
        self.ciphers ['values'] = ('Caesar Cipher',
                                   'Vignere Cipher',
                                   'Random Cipher')
        self.ciphers.grid(column=1, row=1, padx=15, pady=1)
        self.eD = tk.StringVar()
        self.encryptDecrypt = ttk.Combobox(self, textvariable=self.eD)
        self.encryptDecrypt ['values'] = ('Encrypt', 'Decrypt')
        self.encryptDecrypt.grid(column=1, row=3, padx=15, pady=1)

        self.inputMsg = tk.Entry(self, width=30)
        self.inputKey = tk.Entry(self, width=30)
        self.result = tk.Entry(self, width=30)
        
        self.inputMsg.grid(column=2, row=1, padx=15)
        self.inputKey.grid(column=2, row=3, padx=15)
        self.result.grid(column=3, row=2, padx=15)

        def getCipher() :
            c = self.ciphers.get()
            e = self.eD.get()
            m = self.inputMsg.get()
            k = self.inputKey.get()
            if c == "Caesar Cipher" :
                if e == "Encrypt" :
                    cipher = caesarCipher.shiftEncrypt(m, k)
                    print(cipher)
                    self.result.delete(0, END)
                    self.result.insert(0, str(cipher))
                else :
                    cipher = caesarCipher.shiftDecrypt(m, k)
                    print(cipher)
                    self.result.delete(0, END)
                    self.result.insert(0, str(cipher))

            if c == "Vignere Cipher" :
                if e == "Encrypt" :
                    cipher = vigenere.encrypt(m, vigenere.createKey(m, k))
                    print(cipher)
                    self.result.delete(0, END)
                    self.result.insert(0, str(cipher))
                else :
                    cipher = vigenere.decrypt(m, vigenere.createKey(m, k))
                    print(cipher)
                    self.result.delete(0, END)
                    self.result.insert(0, str(cipher))

            if c == "Random Cipher" :
                if e == "Encrypt" :
                    cipher = randomCipher.randEncode(m)
                    print(cipher)
                    self.result.delete(0, END)
                    self.result.insert(0, str(cipher))
                else :
                    fileName = k + ".txt"
                    cipher = randomCipher.randDecode(m, fileName)
                    print(cipher)
                    self.result.delete(0, END)
                    self.result.insert(0, str(cipher))
        # photo = PhotoImage(file = r"images/4600.jpg")
        self.goButton = tk.Button(self, height=2, width=12, text = "Go!", font=('Arial', 15), command=getCipher)
        self.goButton.grid(column=1,row=4, padx=15, pady=20)

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