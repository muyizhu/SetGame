import pygame
import Constants as consts
pygame.mixer.init()
mixer = pygame.mixer
music = mixer.music

musicIndex = 0


def loadMusic(index):
    music.load(consts.MUSIC_PATH_LIST[musicIndex])
    music.set_volume(consts.MUSIC_VOLUME)

def startMusic():
    global musicIndex
    loadMusic(musicIndex)
    music.play()

def endMusic():
    music.pause()

def continueMusic():
    music.unpause()

def nextMusic():
    global musicIndex
    musicIndex+=1
    musicIndex = musicIndex%len(consts.MUSIC_PATH_LIST[musicIndex])
    endMusic()
    startMusic()

clickSound = mixer.Sound(consts.CLICK_SOUND)
clickSound.set_volume(consts.SOUND_VOLUME)
# setSound = mixer.Sound(consts.FIND_SET_SOUND)
# setSound.set_volume(consts.SOUND_VOLUME)
replaceSound = mixer.Sound(consts.REPLACE_CARD_SOUND)
replaceSound.set_volume(consts.SOUND_VOLUME)
replaceAll = mixer.Sound(consts.REPLACE_ALL)
replaceAll.set_volume(consts.SOUND_VOLUME)

