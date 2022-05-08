import pygame 
from pawn import Pawn
from pygame.locals import * 
from sys import exit


pygame.init()

config = {
    'name': "CheckMate",
    'width': 640,
    'heigh': 480
}

display = pygame.display.set_mode((config['width'], config['heigh']))
pygame.display.set_caption(config['name'])

pawn = Pawn()
pieces = pygame.sprite.Group()
pieces.add(pawn)

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pieces.draw(display)
    pieces.update()
    pygame.display.flip() 