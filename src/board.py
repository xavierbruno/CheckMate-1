from enums import PlayerColor
from pawn import Pawn
from tower import Tower
from bishop import Bishop
from knight import Knight
from queen import Queen
from king import King



class Board():
    currentPlayer = PlayerColor.white
    pieces = {}
    

    def __init__(self):
        
        for color in PlayerColor:
            self.pieces[color] = self.instantiatePieces(color.name) 

    
    
    def instantiatePieces(self, color):
        pieces = []
        piecesData = {
            Pawn: {
                "amount": 8,
                "startPosition": (1,2)
            },
            Tower: {
                "amount": 2,
                "startPosition": (1,1)
            },
            Bishop: {
                "amount": 2,
                "startPosition": (3,1)
            },
            Knight: {
                "amount": 2,
                "startPosition": (2,1)
            },
            Queen: {
                "amount": 1,
                "startPosition": (4,1)
            },
            King: {
                "amount": 1,
                "startPosition": (5,1)
            },
        }

        for pieceClass, data in piecesData.items():
            for _amount in range(data['amount']):
                pieces.append(pieceClass(color, self.calculateWorldPos(color, data['startPosition']) ))
        
        return pieces

    def getAllPieces(self):
        return self.getWhitePieces() + self.getBlackPieces()

    def getWhitePieces(self):
        return self.pieces[PlayerColor.white]
    
    def getBlackPieces(self):
        return self.pieces[PlayerColor.black]

    def calculateWorldPos(self, color, pos):
        return (pos[0] * 60, pos[1] * 60)

    

    