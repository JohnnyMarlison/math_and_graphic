import pygame
from pygame import font
import tkinter as tk
from tkinter import messagebox

from game_objects import *

def get_score_text(font_module, snake):
	return font_module.render('Score: ' + str((snake.get_length() - 1) * 10), True, (255, 255, 255))


def redrawWindow(surface, snake, snack, font_module):
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    surface.blit(get_score_text(font_module, snake), (10, 500))
    pygame.display.update()


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass