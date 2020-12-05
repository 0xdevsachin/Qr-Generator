from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.title("QR Generator")
root.minsize(500, 700)
root.maxsize(500, 700)
root.maxsize(500, 700)
root.wm_iconbitmap('ico/qr.ico')
global link
def qr():
    global link
    new_link = link.get()

    # Generate QR code
    QR = pyqrcode.create(new_link)

    # Generating Qr Image and saving it
    QR.png('qr.png', scale=6)

    #Loading Image
    try:

        load = Image.open("qr.png")

        render = ImageTk.PhotoImage(load)

        img = Label(root, image=render)
        img.image = render
        img.place(x=140, y=380)
        messagebox.showinfo('Message', "QR Generated Successfully")


    except:
        messagebox.showerror('Oops!', 'Something Went Wrong!')


Label(root, text='QR Generator', font='lucida 20 bold').place(x=150, y=40)

link = StringVar()

link.set('')

Entry(root, textvariable=link, font='lucida 20 bold',bd=5).place(x=100, y=130)

Button(root, text="Generate QR",font='lucida 15 bold',bd=5, command=qr).place(x=170, y=230)


root.mainloop()