import pygame
import tkinter as tk

pygame.mixer.init()

hover = pygame.mixer.Sound("C:/Users/jorgi/Desktop/proyecto_final/sounds/wii_hover_button_sound.wav")

def play_hover(event):
    hover.play()

root = tk.Tk()
root.title("Test")

button = tk.Button(root, text="Press")
button.pack(expand=True)

button.bind('<Enter>', play_hover)

root.mainloop()