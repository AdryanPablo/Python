# Faça um programa em python que abra e reproduza um arquivo de áudio mp3.

import pygame

pygame.init()
pygame.mixer_music.load("chef021.mp3")
pygame.mixer_music.play()
pygame.event.wait()
