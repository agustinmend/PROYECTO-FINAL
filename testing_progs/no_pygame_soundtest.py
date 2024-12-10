import tkinter as tk
from playsound import playsound

"""Doesn't work at all, don't try it"""

root = tk.Tk()
root.title("Button")

def sound():
    playsound('C:/Users/jorgi/Desktop/proyecto_final/sounds/mcbuttonsound.mp3', block=False)

button = tk.Button(root,
                   text="Click me",
                   command=sound,
                   font=("Minecraft", 23),
                   fg="#000000",
                   bg="#ffffff",
                   relief="raise"
                )
button.pack()

root.mainloop()