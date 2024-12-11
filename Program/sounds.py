import pygame
import random

# Initialize the mixer only
pygame.mixer.init()

def click_sound():
    click = pygame.mixer.Sound("C:/Users/jorgi/Desktop/proyecto_final/sounds/mcbuttonsound.mp3")
    click.play()

def background_music():
    music_list: dict = {
        1 : "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Cat.mp3",
        2 : "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Death.mp3",
        3 : "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Living_Mice.mp3",
        4 : "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Moog_City.mp3",
        5 : "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Oxygene.mp3",
        6 : "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Subwoofer_Lullaby.mp3",
        7 : "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Thirteen.mp3",
        8 : "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/C418_Wet_Hands.mp3",
        9 : "C:/Users/jorgi/Desktop/proyecto_final/sounds/Minecraft_OST/Jack_black_song.mp3"
    }

    song_keys = list(music_list.keys())
    odds = [1, 1, 1, 1, 1, 1, 1, 1, 0.1]

    def play_random_song():
        selected_key = random.choices(song_keys, weights=odds, k=1)[0]
        selected_song = music_list[selected_key]
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play()

    play_random_song()
    while True:
        if not pygame.mixer.music.get_busy():  # If no music is playing
            play_random_song()