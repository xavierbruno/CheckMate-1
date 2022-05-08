import pygame
from abc import ABC, abstractmethod

class Piece(ABC, pygame.sprite.Sprite):
    
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