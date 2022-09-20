from random import randint

grid = []
for i in range(1, 17, 4):
    grid.append(list(range(i, i+4)))

def plusRemove(safe, coordinate):
    for item in grid[coordinate[0]]:
        if item in safe:
            safe.remove(item)
    for index in range(0, 4):
        if grid[index][coordinate[1]] in safe:
            safe.remove(grid[index][coordinate[1]])

def polyominoid_one():
    firstPlus = (0, randint(0, 3))
    secondPlus = (3, firstPlus[1] + 2 if firstPlus[1] <= 1 else firstPlus[1] - 2)
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
    safe = list(range(1,17))
    plusRemove(safe, firstPlus)
    plusRemove(safe, secondPlus)
    return safe
        
def main():
    safe = polyominoid_one()
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
