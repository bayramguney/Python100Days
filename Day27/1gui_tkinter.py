# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# https://tcl.tk/man/tcl8.6/TkCmd/entry.htm

from  tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

# label
my_label = Label(text="I Am a Label",font=("Arial",24,"bold"))
my_label.pack()
# my_label["text"] = "New Text"
my_label.config(text="New Text")

# button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
button = Button(text="Click me",command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
input.get()








window.mainloop()