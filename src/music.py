# Hide Pygame support message
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer, time as pg_time

mixer.init()

path_prefix = './sounds/'

def playsound(sound_file):
    try:
        sfx = mixer.Sound(path_prefix + sound_file)
        sfx.play()
        pg_time.wait(int(sfx.get_length() * 1000))
    except FileNotFoundError:
        print("Error: File does not exist, continuing")


def startgame_aud():
    playsound('startgame.wav')

def endgame_aud():
    playsound('endgame.wav')

def win_aud():
    playsound('win.wav')

def incorrect_aud():
    playsound('incorrect.wav')

def lose_aud():
    playsound('lose.wav')

def invalid_aud():
    playsound('invalid.wav')

playsound('test.wav')