from playsound import playsound
import time

sleeptime = 1

def startgame_aud():
    playsound('./sounds/startgame.wav')
    time.sleep(sleeptime)

def endgame_aud():
    playsound('./sounds/endgame.wav')
    time.sleep(sleeptime)

def win_aud():
    playsound('./sounds/win.wav')
    time.sleep(sleeptime)

def incorrect_aud():
    playsound('./sounds/incorrect.wav')
    time.sleep(sleeptime)

def lose_aud():
    playsound('./sounds/lose.wav')
    time.sleep(sleeptime)

def invalid_aud():
    playsound('./sounds/invalid.wav')
    time.sleep(sleeptime)
