from graphics import * 

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin(title="Coordinates demo", width=800, height=800)

    # Change the coordinate system to a 2x2 square with the origin at the center
    win.setCoords(-1, -1, 1, 1)

    blue = Circle(Point(0, 0), 0.25)
    blue.setFill('blue')
    blue.draw(win)

    # Use the clone() method, so no aliasing
    yellow = blue.clone()
    yellow.draw(win)
    yellow.move(0.7, 0)
    yellow.setFill('yellow')

    # Aliasing--danger, Will Robinson!
    red = blue
    red.setFill('red')

    blue.move(-.6, 0) # Moves the *red* circle, because they refer to the same object
    blue.setWidth(10) # Suddenly, the red circle has a thick border...

    instructions = Text(Point(0, 0.9), 'Click once to close')
    instructions.draw(win)

    # Wait for a mouse click
    win.getMouse()
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
