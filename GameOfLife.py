from graphics import *
import time

tileSize = 10
screenXLength = 100
screenYLength = 75

win = GraphWin("Game of Life", screenXLength * tileSize, screenYLength * tileSize)

screen = [[[Rectangle(Point(x * tileSize, y * tileSize), Point((x + 1) * tileSize - 1, (y + 1) * tileSize - 1)), 0] for x in range(screenXLength)] for y in range(screenYLength)]


def getRectangle(p):
    return screen[int(p.getY()) // tileSize][int(p.getX()) // tileSize]


def initScreen():   

    win.setBackground("light grey")
    win.autoflush = False
    for row in screen:
        for square in row:
            square[0].draw(win)
    win.flush()
    win.autoflush = True
    
    while win.checkKey() == "":
        sqr = getRectangle(win.getMouse())
        if sqr[1] == 0:
            sqr[0].setFill("black")
            sqr[1] = 1
        else:
            sqr[0].setFill("light grey")
            sqr[1] = 0

def getX(sqr):
    return sqr[0].getCenter().getX() // tileSize


def getY(sqr):
    return sqr[0].getCenter().getY() // tileSize


def numOfFriends(square, list):
    counter = 0
    for sqr in list:
        if sqr != square:
            if abs(getX(sqr) - getX(square)) <= 1 and abs(getY(sqr) - getY(square)) <= 1:
                counter += 1
    return counter

def getFriends(square):
    friends = []
    for x in range(-1,2):
        for y in range(-1,2):
            if int(getY(square)) + y <screenYLength and int(getX(square)) + x < screenXLength:
                if screen[y + int(getY(square))][x + int(getX(square))] != square:
                    friends.append(screen[y + int(getY(square))][x + int(getX(square))])
    return friends

def deleteDups(list):
    result = []
    for elem in list:
        if elem not in result:
            result.append(elem)
    return result


def start():

    iteration = 0
    blacked = []
    for row in screen:
        for square in row:
            if square[1] == 1: blacked.append(square)
    while win.checkKey() == "":
        newBlacked = []
        for black in blacked:
            if black[1] == 1 and (numOfFriends(black, blacked) == 3 or numOfFriends(black, blacked) == 2):
                newBlacked.append(black)
            for friend in getFriends(black):
                if friend[1] == 0 and numOfFriends(friend, blacked) == 3:
                    newBlacked.append(friend)
   #     win.autoflush = False
        newBlacked = deleteDups(newBlacked)
        for black in blacked: 
            black[0].setFill("light grey")
            black[1] = 0
        for newBlack in newBlacked: 
            newBlack[0].setFill("black")
            newBlack[1] = 1
        blacked = newBlacked
    #    win.flush()
     #   win.autoflush = True
        iteration += 1
        print(iteration)
        time.sleep(0.2)


def main():
    initScreen()
    start()

main()
