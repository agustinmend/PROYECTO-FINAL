import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Importar Pillow
import pygame

pygame.mixer.init()

vaporeon = "Hey guys, did you know that in terms of male human and\nfemale Pokemon breeding, Vaporeon is the most compatible Pokemon for humans?"

def clicksound():
    click = pygame.mixer.Sound("C:/Users/jorgi/Desktop/proyecto_final/sounds/mcbuttonsound.mp3")
    click.play()

# Variables globales
menu_frame = None
current_widget = None
main_button = None  # Definimos la variable de main_button globalmente para accederla en go_back()

def configure_menu_grid(frame):
    """Configura pesos para filas y columnas de un marco."""
    for i in range(3):  # Tres filas (botones y espacio)
        frame.rowconfigure(i, weight=1)
    for j in range(2):  # Dos columnas
        frame.columnconfigure(j, weight=1)

def menu():
    global menu_frame, main_button

    # Ocultamos el botón "Start"
    main_button.pack_forget()

    if menu_frame is None:
        # Crear el marco solo la primera vez
        menu_frame = tk.Frame(root)
        configure_menu_grid(menu_frame)

        bg_label = tk.Label(menu_frame, image=wallpaper)
        bg_label.place(relwidth=1, relheight=1)

        # Botón "Pokemon"
        btn_show_text = tk.Button(menu_frame, 
                                  text="Pokemon", 
                                  command=lambda: (show_text(), clicksound()), 
                                  font=("Minecraft", 14),
                                  bg="#777777",
                                  fg="#ffffff"
                                  )
        btn_show_text.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Botón "R34"
        btn_show_image = tk.Button(menu_frame, 
                                   text="R34", 
                                   command=lambda: (show_text(), clicksound()), 
                                   font=("Minecraft", 14),
                                   bg="#777777",
                                   fg="#ffffff"
                                   )
        btn_show_image.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Botón "Back"
        btn_back = tk.Button(
            menu_frame,
            text="Back",
            command=lambda: (go_back(), clicksound()),
            font=("Minecraft", 14),
            bg="#777777",
            fg="#ffffff"
        )
        btn_back.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)

    # Mostrar el marco del menú
    menu_frame.pack(fill="both", expand=True)

def show_image():
    global current_widget

    # Ocultar el marco del menú
    menu_frame.pack_forget()

    if current_widget is not None:
        current_widget.destroy()

    # Mostrar la imagen
    current_widget = tk.Label(root, image=image_troleo)
    current_widget.pack(pady=15)

    # Botón "Back"
    back_button = tk.Button(
        root,
        text="Back",
        command=lambda: (go_back_to_menu(back_button), clicksound(back_button)),
        font=("Minecraft", 14),
        bg="#777777",
        fg="#ffffff"
    )
    back_button.pack(pady=10)

def show_text():
    global current_widget

    # Ocultar el marco del menú
    menu_frame.pack_forget()

    if current_widget is not None:
        current_widget.destroy()

    # Mostrar el texto
    current_widget = tk.Label(
        root,
        text=vaporeon,  # Changed text to display the Vaporeon message
        font=("Minecraft", 14),
        bg="#777777",
        fg="#ffffff"
    )
    current_widget.pack(pady=15)

    # Botón "Back"
    back_button = tk.Button(
        root,
        text="Back",
        command=lambda: (go_back_to_menu(back_button), clicksound(back_button)),
        font=("Minecraft", 14),
        bg="#777777",
        fg="#ffffff"
    )
    back_button.pack(pady=10)

def go_back():
    global current_widget, main_button

    if current_widget is not None:
        current_widget.destroy()
        current_widget = None

    menu_frame.pack_forget()  # Ocultar el menú

    # Volver a mostrar el botón "Start"
    main_button.pack(expand=True)

def go_back_to_menu(back_button):
    global current_widget

    if current_widget is not None:
        current_widget.destroy()
        current_widget = None

    back_button.destroy()
    menu_frame.pack(fill="both", expand=True)

# Configurar la ventana principal
root = tk.Tk()
root.title("UI Test")
root.geometry("400x400")

# Cargar la imagen de fondo usando PIL para redimensionarla
wallpaper = Image.open("C:/Users/jorgi/Desktop/proyecto_final/images/minecraft_dirt_wallpaper.png")
wallpaper = wallpaper.resize((root.winfo_screenwidth(), root.winfo_screenheight()))  # Redimensionar al tamaño de la pantalla
wallpaper = ImageTk.PhotoImage(wallpaper)

image_troleo = PhotoImage(file="C:/Users/jorgi/Desktop/proyecto_final/images/baile_del_troleo_xd.gif")

# Crear el fondo y ajustarlo al tamaño de la ventana
background_label = tk.Label(root, image=wallpaper)
background_label.place(relwidth=1, relheight=1)

hellotext = tk.Label(root, 
                     text="This is a main menu test", 
                     font=("Minecraft", 24), 
                     bg="#777777", 
                     fg="#ffffff")
hellotext.pack(pady=(5, 20))

# Definir el botón "Start" globalmente para que esté disponible en go_back()
main_button = tk.Button(root, 
                        text="Start", 
                        command=lambda: (menu(), clicksound()), 
                        width=7, 
                        height=2, 
                        font=("Minecraft", 18), 
                        bg="#777777", 
                        fg="#ffffff",
                        compound="center"
                        )
main_button.pack(expand=True)

root.mainloop()