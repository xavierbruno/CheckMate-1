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

game_states = [
    'choosing_a_piece', # espera o jogador escolher qual peça (botao do mouse ser clicado)
    'choosing_a_move',  # espera o jogador escolher qual movimento (botao do mouse ser solto)
    'validating_move',  # valida 
    'evaluating_move'
    ]

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
        if event.type == MOUSEBUTTONDOWN:
            pawn.handleSelect(event.pos)
        if event.type == MOUSEBUTTONUP:
            pawn.handleDrop(event.pos)

    display.fill((0, 0, 0))
    pieces.update()
    pieces.draw(display)
    pygame.display.update() 


    
        