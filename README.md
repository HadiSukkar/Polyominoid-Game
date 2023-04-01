# Polyominoid-Game

A game based on a sort of puzzle mechanic in the video game Final Fantasy XIV. In this game you have a 4x4 grid and you essentially have to determine a safe spot based on a set of shapes that can appear in each square. There are multiple different patterns named: Polyominoid One, Polyominoid Two, Polyominoid Three, Polyominoid Four, Polyominoid Five, Polyominoid Six and Cachexia. The set of shapes and where they can appear will vary based on the pattern (and there will be some slight variations in the pattern itself) but the general method for solving each one can generally be codified down to some guiding principles.

When the program shows the user the patterns on the 4 x 4 grid, they are to write out the number square that is considered "safe". The ordering of the squares goes from 1 to 16 ascending from left to right and then top to bottom. I.E:

&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;\
| 1&ensp;|&ensp;2&ensp;|&ensp;3&ensp;|&ensp;4 |\
| 5&ensp;|&ensp;6&ensp;|&ensp;7&ensp;|&ensp;8 |\
| 9&ensp;|&nbsp;10&nbsp;|&nbsp;11&nbsp;|&nbsp;12|\
|13&nbsp;|&nbsp;14&nbsp;|&nbsp;15&nbsp;|&nbsp;16|\
&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;&ndash;

The user is to enter the squares corresponding to the safe positions (there can be more than one) with the corresponding number and with a space between each number. After entering the number the program will inform the user whether their guess was correct and how long it took them to arrive at that guess and consequently prompt them to enter either Y or N if they want to keep repeating the game. 

# + Shape

When this shape appears (and drawn in red) for the game, it means that all squares in the same row and column as the square with the '+' shape on it are considered unsafe.

# X Shape

When this shape appear (also drawn in red), all squares that are diagonal from the square with the 'x' shape on it are considered unsafe.

# Tether

This will appear in some patterns of the game and appears like a blue line between any two of the above shapes. It indicates that the shapes will swap positions. For example if there is a + shape in square 4 and an X shape in square 5 and there is a blue tether between them, this indicates that the X shape is now in square 4 and the + shape is now in square 5.

# Choros Ixou

This is a fancy name for a unique shape that spans multiple squares. It always comes as either a green hourglass going from the top edge to the bottom edge of the grid or as a green bowtie (the hourglass rotated 90 degrees) going from the left edge to the right edge of the grid. All square that are completely covered by this green hourglass/bowtie will be considered unsafe. Any square that is only partially covered can still be safe.

# Program Overview

Notably this is a rather simple python project I worked on to brush up a little on python usage and making use of github. Looking back the program could have been more complex or linked to a database to save results and possibly have a user be capable of tracking their records for each pattern and improving upon them. Additionally the input from the user could have been more relaxed on both entering the numbers and being able to repeat the game.
