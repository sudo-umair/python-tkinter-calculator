from operator import iconcat
from tkinter import *

root = Tk()
root.title("Calculator by Umair")
root.geometry("400x515")
root.resizable(width=False, height=False)


def click(event):
    global screen_value
    text = event.widget.cget("text")
    if text == "=":
        if screen_value.get().isdigit():
            value = int(screen_value.get())
        else:
            value = eval(screen_value.get())

        screen_value.set(value)
        screen.update()
    elif text == "C":
        screen_value.set(screen_value.get()[0:-1])
        screen.update()
    else:
        screen_value.set(screen_value.get() + text)


screen_value = StringVar()

screen = Entry(
    root,
    textvariable=screen_value,
    bg="grey",
    fg="white",
    font="Lucida 34 italic",
    relief=SUNKEN,
)
screen.pack(side=TOP, fill=X, ipadx=2, ipady=2, padx=12, pady=8)

buttons_list = [
    "1",
    "2",
    "3",
    "C",
    "4",
    "5",
    "6",
    "+",
    "7",
    "8",
    "9",
    "-",
    "0",
    "(",
    ")",
    "*",
    "%",
    ".",
    "/",
    "=",
]


def addbuttons(buttons_list):
    f = Frame(root)
    f.pack()

    for i in buttons_list:
        if i == "C":
            bgcolor = "red"
        elif i == "+" or i == "-" or i == "/" or i == "*" or i == "%" or i == ".":
            bgcolor = "teal"
        elif i == "=":
            bgcolor = "green"
        elif i == "(" or i == ")":
            bgcolor = "yellow"
        else:
            bgcolor = "orange"

        b = Button(
            f, text=i, height=1, width=3, bg=bgcolor, font="Lucida 19", padx=12, pady=8
        )
        b.pack(side=LEFT, padx=9, pady=9)
        b.bind("<Button-1>", click)


addbuttons(buttons_list[0:4])
addbuttons(buttons_list[4:8])
addbuttons(buttons_list[8:12])
addbuttons(buttons_list[12:16])
addbuttons(buttons_list[16:])

bar = Label(root, text="Ready", bg="lightgrey", anchor=W, padx=4, pady=2, relief=SUNKEN)
bar.pack(side=BOTTOM, fill=X)

root.mainloop()
