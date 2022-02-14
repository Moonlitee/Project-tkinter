from tkinter import *

root = Tk()

root.title("Test App")

root.geometry("1280x1024")
def purple():
    label = Label(root, text = 'purple', bg='purple')
    text.window_create(INSERT, window = label)

text = Text(root, width=30, height=30)
text.pack()

button = Button(root, text = 'purple', command = purple )
button.pack()


def black():
    label = Label(root, text = 'black', bg='black')
    text.window_create(INSERT, window = label)


button = Button(root, text = 'black', command = black )
button.pack()


def white():
    label = Label(root, text = 'white', bg='white')
    text.window_create(INSERT, window = label)


button = Button(root, text = 'white', command = white )
button.pack()


def blue():
    label = Label(root, text = 'blue', bg='blue')
    text.window_create(INSERT, window = label)


button = Button(root, text = 'blue', command = blue )
button.pack()


def yellow():
    label = Label(root, text = 'yellow', bg='yellow')
    text.window_create(INSERT, window = label)


button = Button(root, text = 'yellow', command = yellow )
button.pack()
root.mainloop()