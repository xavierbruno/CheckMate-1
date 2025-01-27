import pygame 
from board import Board
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

board = Board()
pieces = board.getAllPieces()
blackPiecesGroup = pygame.sprite.Group()
whitesPiecesGroup = pygame.sprite.Group()
blackPiecesGroup.add(board.getBlackPieces())
whitesPiecesGroup.add(board.getWhitePieces())

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            for piece in pieces:
                piece.handleSelect(event.pos)
        if event.type == MOUSEBUTTONUP:
            for piece in pieces:
                piece.handleDrop(event.pos)

    display.fill((255, 255, 0))
    blackPiecesGroup.update()
    blackPiecesGroup.draw(display)
    whitesPiecesGroup.update()
    whitesPiecesGroup.draw(display)
    pygame.display.update() 


    
        