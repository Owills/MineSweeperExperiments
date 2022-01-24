import sys
import pygame
#test

pygame.init()

#contsants:
tileSize = 25 # in pixels
width = 750;
height = 750;
screen = pygame.display.set_mode((width, height))


#represents an individual tile on a board
#a tile is a pygame button
class tile:
    #-1 is flag
    #posx, posy represent grid numbers
    #visible refers to if the tile has been discovered by player
    def __init__(self, num, posx, posy, visible, font):
        self.num = num
        self.posx = posx
        self.posy = posy
        self.visible = visible
        self.color = "azure4"
    def update(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.posx * tileSize, self.posy * tileSize, tileSize, tileSize))
        pygame.draw.rect(screen, "gray", pygame.Rect(self.posx*tileSize, self.posy*tileSize, tileSize, tileSize), 1)
    def setColor(self):
        self.color = "blue"
        self.update()





#represents a grid of tiles
class board:
    #sizex and sizey represent the width and height of the board in number of tiles
    #tilesize is the size of a single tile on the board
    def __init__(self, sizex, sizey):
        self.sizex = int(sizex / tileSize)
        self.sizey = int(sizey / tileSize)
        self.tilesL = [[0 for x in range(self.sizey)] for y in range(self.sizex)]
    def buildBoard(self):
        for i in range(len(self.tilesL)):
            for j in range(len(self.tilesL[i])):
                self.tilesL[i][j] = tile(0,i,j,True,font=30)
    def showTiles(self):
        for i in range(len(self.tilesL)):
            for j in range(len(self.tilesL[i])):
                self.tilesL[i][j].update()
    def getTile(self, pos):
        self.tilesL[int(pos[0]/tileSize)][int(pos[1]/tileSize)].setColor()
    def setMines(self):
        print("soon")





def main():
    #pygame setup
    background_colour = (234, 212, 252)
    pygame.display.set_caption('MineSweeper')
    screen.fill(background_colour)
    pygame.display.flip()

    #game mechanics setup
    mainBoard = board(width, height)
    mainBoard.buildBoard()
    mainBoard.showTiles()

    #main game -loop
    running = True
    while running:

        pygame.display.flip()

        # for loop through the event queue
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                mainBoard.getTile(pos)




main();