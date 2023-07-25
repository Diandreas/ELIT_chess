import pygame as p
import engine

...

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
...


def loadImages():
    pieces = ['/white/pawn', '/white/king', '/white/knight', '/white/queen', '/white/rook', '/white/bishop',
              '/black/pawn', '/black/king', '/black/knight', '/black/queen', '/black/rook', '/black/bishop']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("assets\model\piece_model_1" + piece + ".png"),
                                          (SQ_SIZE, SQ_SIZE))


...


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = engine.GameState()
    loadImages()
    running = True
    sqSelected = ()  # selectioner les sq seelectionner
    playerClicks = []  # surveiller les click
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = engine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = ()
                    playerClicks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

    # print(gs.board)


...


def drawGameState(screen, gs):
    drawBoard(screen)  # dessiner les carre sur leechiquier
    # ajjouter les suggesion de mouvement
    drawPiece(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("light green")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPiece(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "main":
    main()

main()
