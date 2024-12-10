import tkinter as tk

def create_button_with_shadow(root, text, command):
    # Create the frame to hold both the canvas and the button
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    # Create the button widget
    button = tk.Button(frame, text=text,
                       command=command,
                       font=("Minecraft", 16),
                       bd=1,
                       highlightthickness=1,
                       relief="raised",
                       bg="#777777",
                       fg="#ffffff"
                       )
    
    # Create the canvas for the shadow effect
    canvas = tk.Canvas(frame, bd=0, highlightthickness=0, relief="flat")
    canvas.pack()

    def create_shadow():
        # Get the size of the button after packing it
        button_width = button.winfo_width()
        button_height = button.winfo_height()

        # Adjust the canvas size based on the button's dimensions
        canvas.config(width=button_width, height=button_height)

        # Position the canvas correctly behind the button
        canvas.place(x=button.winfo_x(), y=button.winfo_y())

        # Draw the shadow text (slightly offset in black color)
        canvas.create_text(102, 32, text=text, font=("Minecraft", 16), fill="black", tags="shadow_text")
        # Draw the main text (white)
        canvas.create_text(100, 30, text=text, font=("Minecraft", 16), fill="white", tags="main_text")

    # Pack the button and adjust shadow after the button is rendered
    button.pack()

    # Schedule shadow creation after button is rendered
    button.after(10, create_shadow)

    return button

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Button with Text Shadow")

# Create the custom button with shadow effect
button = create_button_with_shadow(root, "Click Me", on_button_click)

root.mainloop()