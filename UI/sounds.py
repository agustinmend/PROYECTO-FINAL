import pygame

pygame.mixer.init()

def click_sound():
    click = pygame.mixer.Sound("C:/Users/jorgi/Desktop/proyecto_final/sounds/mcbuttonsound.mp3")
    click.play()

def background_music():
    music_list: dict = {
        1 : ""
    }

print("sounds.py working perfectly")