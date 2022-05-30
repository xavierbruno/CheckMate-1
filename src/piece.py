import pygame
from abc import ABC, abstractmethod

class Piece(ABC, pygame.sprite.Sprite):

    states = ['free', 'selected']
    state = 'free'
    
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        
    
    @abstractmethod
    def move():
        pass

    @abstractmethod
    def attack():
        pass

    def update(self):
        self.handleMove()

    def handleMove(self):
        if self.state == 'selected': 
           self.rect.center = pygame.mouse.get_pos()

    def handleSelect(self, pos):
        if self.rect.collidepoint(pos) and self.state == 'free': 
            print('selected!')
            self.state = 'selected'

    def handleDrop(self, pos):
        if self.rect.collidepoint(pos) and self.state == 'selected': 
            print('free!')
            self.state = 'free'