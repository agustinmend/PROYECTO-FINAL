import tkinter as tk
import pygame
import threading

# Initialize pygame mixer
pygame.mixer.init()

# Load sound files
click_sound = pygame.mixer.Sound("C:/Users/jorgi/Desktop/proyecto_final/sounds/Fart.wav")
hover_sound = pygame.mixer.Sound("C:/Users/jorgi/Desktop/proyecto_final/sounds/wii_hover_button_sound.wav")

# Function to play sound on click
def play_sound_when_click():
    click_sound.play()

# Function to play sound on hover and show aura
def play_hover_sound_and_aura(event):
    hover_sound.play()
    # Add aura effect
    aura_item = canvas.create_rectangle(
        button_bbox[0] - 5, button_bbox[1] - 5, 
        button_bbox[2] + 5, button_bbox[3] + 5, 
        outline="#f1c40f", width=5
    )
    canvas.tag_lower(aura_item, "all")  # Send aura to the back
    canvas.hover_aura = aura_item  # Store reference for removal later

# Function to remove aura effect
def remove_aura(event):
    if hasattr(canvas, "hover_aura"):
        canvas.delete(canvas.hover_aura)

# Function to continuously check for Pygame events without blocking the Tkinter loop
def run_pygame_events():
    while True:
        pygame.event.pump()  # Handle Pygame events

# Create the Tkinter window
root = tk.Tk()
root.title("Press to make le epic sound effect")

# Create a canvas for the aura effect
canvas = tk.Canvas(root, width=400, height=300, bg="#34495e")
canvas.pack(fill="both", expand=True)

# Create a button on the canvas
button = tk.Button(canvas, text="Click Me", 
                   width=20, height=2,
                   bg="#3498db", fg="#ffffff", font=("Comic Sans MS", 14, "bold"),
                   command=play_sound_when_click)

# Add button to the canvas
button_id = canvas.create_window(200, 150, window=button)
button_bbox = canvas.bbox(button_id)  # Get button bounding box for aura effect

# Bind hover events to the button
button.bind("<Enter>", play_hover_sound_and_aura)
button.bind("<Leave>", remove_aura)

# Create a separate thread to handle Pygame events
pygame_thread = threading.Thread(target=run_pygame_events, daemon=True)
pygame_thread.start()

# Run the Tkinter main loop
root.mainloop()