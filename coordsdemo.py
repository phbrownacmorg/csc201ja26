from graphics import * 

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin(title="Coordinates demo", width=600, height=600)

    # Change the coordinate system to a 2x2 square with the origin at the center
    # These coordinates are now independent of the size of the window
    win.setCoords(-1, -1, 1, 1)

    c1 = Circle(Point(0, 0), 0.5)
    c1.setFill('blue')
    c1.draw(win)
    
    instructions = Text(Point(0, 0.9), 'Click once to close')
    instructions.draw(win)

    # Wait for a mouse click
    win.getMouse()
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
