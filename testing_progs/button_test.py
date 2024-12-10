import tkinter as tk
import pygame
import threading

# Initialize pygame mixer
pygame.mixer.init()

# Load the sound
click_sound = pygame.mixer.Sound("C:/Users/jorgi/Desktop/proyecto_final/sounds/Fart.wav")
hover_sound = pygame.mixer.Sound("C:/Users/jorgi/Desktop/proyecto_final/sounds/wii_hover_button_sound.wav")

def play_sound_when_click():
    click_sound.play()

def hover_on(event):
    hover_sound.play()

    # Get the bounding box of the button
    button_bbox = canvas.bbox(button_id)
    
    # Create the aura with a thicker highlight around the button
    aura = canvas.create_rectangle(
        button_bbox[0] - 2, button_bbox[1] - 2,  # Extend aura size outward
        button_bbox[2] + 2, button_bbox[3] + 2,  # Use button_bbox[3] (correct bounding box index)
        outline="#009ac7", width=5  # Thicker outline for the aura
    )
    
    # Lower the aura behind the button
    canvas.tag_lower(aura, button_id)
    
    # Store the aura ID for removal
    canvas.hover_aura = aura


def hover_off(event):
    if hasattr(canvas, "hover_aura"):
        # Remove the aura when mouse leaves
        canvas.delete(canvas.hover_aura)

def run_pygame_events():
    while True:
        pygame.event.pump()

# Create the Tkinter window
root = tk.Tk()
root.title("Press to make le epic sound effect")

canvas = tk.Canvas(root, width=400, height=300, bg="#ffffff")
canvas.pack(fill="both", expand=True)

# Create a button and attach the sound-playing function
button = tk.Button(root, 
                   text="Le epic sound!!1!.wav", 
                   command=play_sound_when_click, 
                   width=20, 
                   height=5, 
                   bg="#ffffff", 
                   fg="#000000", 
                   font=("Comic Sans MS", 14, "bold"),
                   relief="solid",
                   highlightthickness=1,
                   highlightbackground="#0373fc",
                   highlightcolor="#0373fc"  
                )
button_id = canvas.create_window(200, 150, window=button)

button.bind("<Enter>", hover_on)
button.bind("<Leave>", hover_off)

pygame_thread = threading.Thread(target=run_pygame_events, daemon=True)
pygame_thread.start()
# Run the Tkinter main loop
root.mainloop()