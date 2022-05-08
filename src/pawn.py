from piece import Piece

class Pawn(Piece): 
    image_path = 'sprites/pawn_white.png'

    def __init__(self):
        super().__init__(self.image_path)
        print('pawn')
    
    def move():
        print('move')

    def attack():
        print('atk')