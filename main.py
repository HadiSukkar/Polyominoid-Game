from random import randint
import turtle

#set up a 4 by 4 matrix each containing numbers from 1 to 16 with the numbers going from left to right.
grid = []
for i in range(1, 17, 4):
    grid.append(list(range(i, i+4)))
pen = turtle.Turtle()
HYPOTENUSE = (2*100**2)**0.5

"""
Method to draw the 4x4 grid with the turtle module. 
The exact center of the grid is (0,0) with each square being 100x100 in length.
As a result the grid is first drawn with all the horizontal lines followed by all the vertical lines.
"""
def drawGrid():
    pen.up()
    for i in range(0, 5):
        pen.goto(-200, -200+100*i)
        pen.down()
        pen.forward(400)
        pen.up()
    pen.left(90)
    for i in range(0, 5):
        pen.goto(-200+100*i, -200)
        pen.down()
        pen.forward(400)
        pen.up()
    pen.right(90)

"""
Method to draw the + signs.
It takes a parameter of the coordinates of the plus. 
The first number is the row number (and therefore corresponds to the Y-axis).
The second number is the column number (and therefore corresponds to the X-axis).
"""
def drawPlus(coordinate):
    pen.width(5)
    pen.color("red")
    #X starts at -200 and increments by 100 because the higher the column number, the more positive the value of X has to be.
    #Y starts at 200 (150 in this case because it has to start in the middle of the square to draw the line) and decrements by 100 because the higher the row number,
    #the further down the grid the pen has to go and therefore the more negative the value of Y has to be.
    pen.goto(-200+100*coordinate[1], 150-100*coordinate[0])
    pen.down()
    pen.forward(100)
    pen.up()
    pen.right(90)
    pen.goto(-150+100*coordinate[1], 200-100*coordinate[0])
    pen.down()
    pen.forward(100)
    pen.up()
    pen.left(90)

"""
Method to draw the X signs.
It takes a parameter of the coordinates of the X.
The first number is the row number and the second number is the column number.
"""
def drawX(coordinate):
    pen.width(5)
    pen.color("red")
    #drawing down and to the right
    pen.right(45)
    #see drawPlus for logic behind pen placement
    pen.goto(-200+100*coordinate[1], 200-100*coordinate[0])
    pen.down()
    pen.forward(HYPOTENUSE)
    pen.up()
    #drawing up and to the right
    pen.left(90)
    #notably this is going to be starting from the bottom left of the square and so has to be 100 lower on the Y axis.
    pen.goto(-200+100*coordinate[1], 100-100*coordinate[0])
    pen.down()
    pen.forward(HYPOTENUSE)
    pen.up()
    pen.right(45)

"""
Method to draw tethers between two shapes.
It takes a pair of two coordinates and draws a line between the center of the squares that they correspond to.
"""
def drawTether(coordinateSet):
    pen.width(3)
    start, destination = coordinateSet
    pen.color("blue")
    pen.goto(-150+100*start[1], 150-100*start[0])
    pen.down()
    pen.goto(-150+100*destination[1], 150-100*destination[0])
    pen.up()

"""
Method to both draw and remove the safe squares from the chorus ixou pattern. Chorus ixou is an hourglass or bowtie shape that makes any square completely covered by the
hourglass or bowtie be rendered unsafe.
"""
def chorosIxou(safe):
    #A cardinality of 0 means that there's an hourglass shape choros ixou. A cardinality of 1 means a bowtie.
    cardinality = randint(0, 1)
    removed =[[2, 3, 14, 15], [5, 8, 9, 12]] 
    for i in removed[cardinality]:
        safe.remove(i)
    pen.width(1)
    pen.color("green")
    pen.fillcolor("green")
    pen.goto(0, 0)
    if cardinality == 0:
        pen.left(45)
    else:
        pen.right(45)
    pen.down()
    pen.begin_fill()
    pen.forward(2*HYPOTENUSE)
    pen.left(135)
    pen.forward(400)
    pen.left(135)
    pen.forward(4*HYPOTENUSE)
    pen.right(135)
    pen.forward(400)
    pen.right(135)
    pen.forward(2*HYPOTENUSE)
    if cardinality == 0:
        pen.right(45)
    else:
        pen.left(45)
    pen.end_fill()
    pen.up()

"""
Method that takes a set of safe grid spaces and the coordinate of a plus and removes all the safe squares that are horizontal and vertical of the plus.
"""
def plusRemove(safe, coordinate):
    #remove all horizontal squares
    for item in grid[coordinate[0]]:
        if item in safe:
            safe.remove(item)
    #remove all vertical squares
    for index in range(0, 4):
        if grid[index][coordinate[1]] in safe:
            safe.remove(grid[index][coordinate[1]])

"""
Method that takes a set of safe grid spaces and the coordinates of an X and removes all the safe squares that are diagonal of the X. 
"""
def XRemove(safe, coordinate):
    #starts with removing the square the X is on itself.
    if grid[coordinate[0]][coordinate[1]] in safe:
        safe.remove(grid[coordinate[0]][coordinate[1]])
    #all the possible diagonal movements from the X.
    diagonalMovement = [(-1,-1), (-1, 1), (1, -1), (1, 1)]
    #as soon as all the squares in one direction are cleared of being safe, it will iterate in the next direction starting from the same origin of the X.
    for movement in diagonalMovement:
        x, y = coordinate
        while 0 <= x + movement[0] <= 3 and 0 <= y + movement[1] <= 3:
            x += movement[0]
            y += movement[1]
            if grid[x][y] in safe:
                safe.remove(grid[x][y])
        

"""
The first puzzle set that always has one plus each on the top and bottom row with the plus on the bottom row always being two columns over from the plus on the top row.
"""
def polyominoid_one(safe = 0):
    firstPlus = (0, randint(0, 3))
    secondPlus = (3, firstPlus[1] + 2 if firstPlus[1] <= 1 else firstPlus[1] - 2)
    drawPlus(firstPlus)
    drawPlus(secondPlus)
    """"
    ominoid = []
    for _ in range(0,4):
        ominoid.append("[]")
    ominoid = [ominoid]
    for _ in range(0,3):
        ominoid.append(ominoid[0].copy())
    ominoid[firstPlus[0]][firstPlus[1]] = "+"
    ominoid[secondPlus[0]][secondPlus[1]] = "+"
    for row in ominoid:
        print("\t".join(row))
    """
    if safe == 0:
        safe = list(range(1,17))
    plusRemove(safe, firstPlus)
    plusRemove(safe, secondPlus)
    return safe

"""
The second puzzle set that has two Xs on opposite corners and one + in one of the remaining corners tethered to one of these Xs.
There is a remaining + across from the remaining untethered X but shifted one across and these two are also tethered.
"""
def polyominoid_two():
    #this expression gets the Y coordinate to either be 0 or 3
    firstX = (0, 3*randint(0,1))
    secondX = (3, 3-firstX[1])
    XShape = [firstX, secondX]
    randomX = XShape[randint(0,1)]
    untetheredX = XShape[1-XShape.index(randomX)]
    #this assigns the first plus to be in the same row as one of the random Xs but in the other corner in that row.
    firstPlus = (3 - randomX[0], randomX[1])
    firstTether = [randomX, firstPlus]
    #The second + is first created as a list so it can be placed in a corner and then moved over to the correct location before being turned into a tuple.
    secondPlus = [3-firstPlus[0], 3-firstPlus[1]]
    for i in range(0, 2):
        if secondPlus[i] == untetheredX[i]:
            if secondPlus[i] == 3:
                secondPlus[i] = 2
            else:
                secondPlus[i] = 1
    secondPlus = tuple(secondPlus)
    secondTether = [untetheredX, secondPlus]
    drawX(firstX)
    drawX(secondX)
    drawPlus(firstPlus)
    drawPlus(secondPlus)
    drawTether(firstTether)
    drawTether(secondTether)
    randomX, firstPlus = firstPlus, randomX
    untetheredX, secondPlus = secondPlus, untetheredX
    safe = list(range(1,17))
    plusRemove(safe, firstPlus)
    plusRemove(safe, secondPlus)
    XRemove(safe, randomX)
    XRemove(safe, untetheredX)
    return safe

"""
The third puzzle set that has either of two orientations. In both orientations there are two Xs in opposite corners.
In the first orientation there are two + one square horizontally and one square vertically from an unoccupied corner. Both form straight line tethers to the Xs.
In the second orientation there is one + in the corner that is tethered to an X and another + that is adjacent to that X (in the square that isn't in the path of the tether)
that is tethered to the remaining X. 
"""
def polyominoid_three():
    firstX = (0, 3*randint(0,1))
    secondX = (3, 3-firstX[1])
    XShape = [firstX, secondX]
    randomX = XShape[randint(0,1)]
    orientation = randint(0,1)
    if orientation == 0:
        #in this orientation both + are around one of the remaining corners and so they are therefore initially placed in the corner as a list and then
        #corrected to the right location and turned into a tuple.
        firstPlus = [3- randomX[0], randomX[1]]
        secondPlus = [firstPlus[0], firstPlus[1]]
        for i in range(0, 2):
            if firstPlus[i] == firstX[i]:
                if firstPlus[i] == 3:
                    firstPlus[i] = 2
                else:
                    firstPlus[i] = 1
            if secondPlus[i] == secondX[i]:
                if secondPlus[i] == 3:
                    secondPlus[i] = 2
                else:
                    secondPlus[i] = 1
        firstPlus = tuple(firstPlus)
        secondPlus = tuple(secondPlus)
        #notably the + symbols will shift to a different row or column creating a diagonal tether so to maintain the straight line tether, the + will have to tether to 
        #opposite X they were compared to in the above statements.
        firstTether = [firstX, secondPlus]
        secondTether = [secondX, firstPlus]
    else:
        firstPlus = (3 - randomX[0], randomX[1])
        randomX = XShape[randint(0,1)]
        firstTether = [randomX, firstPlus]
        untetheredX = XShape[1-XShape.index(randomX)]
        secondPlus = [3 - firstPlus[0], 3 - firstPlus[1]]
        for i in range(0, 2):
            if secondPlus[i] == untetheredX[i]:
                if secondPlus[i] == 3:
                    secondPlus[i] = 1
                else:
                    secondPlus[i] = 2
        secondPlus = tuple(secondPlus)
        secondTether = [untetheredX, secondPlus]
    drawX(firstX)
    drawX(secondX)
    drawPlus(firstPlus)
    drawPlus(secondPlus)
    drawTether(firstTether)
    drawTether(secondTether)
    firstTether[0], firstTether[1] = firstTether[1], firstTether[0]
    secondTether[0], secondTether[1] = secondTether[1], secondTether[0]
    safe = list(range(1,17))
    plusRemove(safe, firstTether[1])
    plusRemove(safe, secondTether[1])
    XRemove(safe, firstTether[0])
    XRemove(safe, secondTether[0])
    return safe


"""
The fourth puzzle set that always has two X's on the inner four circles with the X's always being diagonal to each other.
"""     
def polyominoid_four():
    firstX = (1, randint(1,2))
    secondX = (2, 3 - firstX[1])
    drawX(firstX)
    drawX(secondX)
    safe = list(range(1,17))
    XRemove(safe, firstX)
    XRemove(safe, secondX)
    return safe

"""
The fifth puzzle set that will always have two + in opposite corners and an X in a corner that lies in the same diagonal as those two +. 
This X is also tethered to one of the two + with either a north/south choros ixou or an east/west chorus ixou making an unsafe hourglass
or an unsafe bowtie.
"""
def polyominoid_five():
    safe = list(range(1,17))
    chorosIxou(safe)
    firstPlus = (0, 3*randint(0,1))
    secondPlus = (3, 3-firstPlus[1])
    diagonalMovement = randint(1, 2)
    #places the X in the diagonal between the two plus in one of two random positions
    onlyX = (firstPlus[0] + diagonalMovement, firstPlus[1] + diagonalMovement if firstPlus[1] == 0 else firstPlus[1] - diagonalMovement)
    plusShape = [firstPlus, secondPlus]
    randomPlus = plusShape[randint(0,1)]
    untetheredPlus = plusShape[1 - plusShape.index(randomPlus)]
    tether = [onlyX, randomPlus]
    drawPlus(firstPlus)
    drawPlus(secondPlus)
    drawX(onlyX)
    drawTether(tether)
    tether[0], tether[1] = tether[1], tether[0]
    plusRemove(safe, tether[1])
    plusRemove(safe, untetheredPlus)
    XRemove(safe, tether[0])
    return safe

"""
The six puzzle set will always have two + in opposite corners and one X in one of the remaining corners. The final symbol will either be a + or X and will be
one square horizontal or vertical of the remaining unfilled corner.
"""
def polyominoid_six():
    firstPlus = (0, 3*randint(0, 1))
    secondPlus = (3, 3-firstPlus[1])
    plusShape = [firstPlus, secondPlus]
    randomPlus = plusShape[randint(0,1)]
    otherPlus = plusShape[1 - plusShape.index(randomPlus)]
    firstX = (3-randomPlus[0], randomPlus[1])
    finalShape = [3 - otherPlus[0], otherPlus[1]]
    x_or_y = randint(0, 1)
    if x_or_y == 0:
        if finalShape[0] == 0:
            finalShape[0] = 1
        else:
            finalShape[0] = 2
    else:
        if finalShape[1] == 0:
            finalShape[1] = 1
        else:
            finalShape[1] = 2
    drawPlus(firstPlus)
    drawPlus(secondPlus)
    drawX(firstX)
    safe = list(range(1,17))
    plusOrX = randint(0,1)
    if plusOrX == 0:
        drawPlus(finalShape)
        plusRemove(safe, finalShape)
    else:
        drawX(finalShape)
        XRemove(safe, finalShape)
    plusRemove(safe, firstPlus)
    plusRemove(safe, secondPlus)
    XRemove(safe, firstX)
    return safe

"""
The seventh puzzle set is exactly like the first set except with Chorus Ixou. 
"""
def polyominoid_seven():
    safe = list(range(1,17))
    chorosIxou(safe)
    return polyominoid_one(safe)
    
def main():
    drawGrid()
    polyominoid = [polyominoid_one, polyominoid_two, polyominoid_three, polyominoid_four, polyominoid_five, polyominoid_six, polyominoid_seven]
    safe = polyominoid[6]()
    guess = input("Determine the safe spots for this pattern: ").split()
    for index in range(0, len(guess)):
        guess[index] = int(guess[index])
    if len(safe) != len(guess):
        print("You guessed wrong!")
        return
    for item in safe:
        if item not in guess:
            print("You guessed wrong!")
            return
    print("You guessed correctly!")

if __name__ == "__main__":
    main()
