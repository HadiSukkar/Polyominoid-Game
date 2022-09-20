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
def polyominoid_one():
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
    safe = list(range(1,17))
    plusRemove(safe, firstPlus)
    plusRemove(safe, secondPlus)
    return safe

"""
The fourth puzzle set that always has two X's on the inner four circles with the X's always being diagonal to each other.
"""     
def polyominoid_four():
    firstX = (1, randint(1,2))
    secondX = (2, abs(3 - firstX[1]))
    drawX(firstX)
    drawX(secondX)
    safe = list(range(1,17))
    XRemove(safe, firstX)
    XRemove(safe, secondX)
    return safe

def main():
    drawGrid()
    polyominoid = [polyominoid_one, polyominoid_four]
    safe = polyominoid[1]()
    guess = input("Determine the safe spots for this pattern: ").split()
    for index in range(0, len(guess)):
        guess[index] = int(guess[index])
    for item in safe:
        if item not in guess:
            print("You guessed wrong!")
            return
    print("You guessed correctly!")

if __name__ == "__main__":
    main()
