import pygame as p
from Chess import engine

...
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT //DIMENSION
MAX_FPS = 15
IMAGES= {}
...
def loadImages():
    pieces = ['pawn','king','knight','queen','rook','bishop']
    for piece in pieces :
        IMAGES[piece]=p.image.loade()






def drawGameState (screen, gs):
    drawboard(screan) #dessiner les carre sur leechiquier
    # ajjouter les suggesion de mouvement
    drawPieces(screan,gs.board)


def drawBoard(screen):
    colors = [p.Color("white"] , p.Color("gray")]
    ...

def drawPiece(screen,board)
    pass



if __name=="main":
    main()

