import tkinter
from PIL import Image, ImageTk


root = tkinter.Tk()
root.geometry('480x480')

image = Image.open('C:\\Users\\Takezaki\\Desktop\\242640.jpg')
image = image.resize((160, 160), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(image)
tkinter.Label(root, image=icon).pack()

canvas = tkinter.Canvas(root, width=300, height=300, bg='blue')
canvas.pack()
canvas.create_image(30, 15, anchor=tkinter.NW, image=icon)

root.mainloop()
