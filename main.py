# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
ancho = int(input("Ancho de la ventana: "))
alto = int(input("Alto de la ventana: "))
size = (ancho, alto)
color = (50, 120, 130)
titulo = input("¿Cómo se llama tu simluador?: ")
main2(size, titulo, color)
