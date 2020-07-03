import tkinter

root = tkinter.Tk()
root.geometry('480x480')

mainMenu = tkinter.Menu()
root.config(menu=mainMenu)

fileMenu = tkinter.Menu(mainMenu)
mainMenu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New File')
fileMenu.add_command(label='Open')
fileMenu.add_command(label='OpenModule')
fileMenu.add_separator()
fileMenu.add_command(label='Recent Files')

editMenu = tkinter.Menu(mainMenu)
mainMenu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo')
editMenu.add_command(label='Redo')

underMenu = tkinter.Menu(editMenu)
editMenu.add_cascade(label='Male', menu=underMenu)
underMenu.add_command(label='Undo')
underMenu.add_command(label='Redo')

root.mainloop()
