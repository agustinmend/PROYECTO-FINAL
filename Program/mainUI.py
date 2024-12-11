# Importaciones modulares
import pygame
import sounds
import images
# importaciones normales
import tkinter as tk
from threading import Thread

# Initialize pygame in the main thread
pygame.init()

# Function to start music in a separate thread
def start_music():
    sounds.background_music()

# Initialize the Tkinter root window
root = tk.Tk()
root.title("Residencial al cubo")
root.columnconfigure(0, weight=1)  # Centre the first column

images.wallpaper(root)

# Start background music in a separate thread
music_thread = Thread(target=start_music, daemon=True)
music_thread.start()

# Create a label for the UI
holabvnd = tk.Label(root, text="Bienvenido a", font=("Minecraft", 15))
holabvnd.grid(row=0, column=0, sticky="n")
holabvnd.grid_configure(padx=20, pady=20)

# Start the Tkinter main loop (this will keep the window open)
root.mainloop()