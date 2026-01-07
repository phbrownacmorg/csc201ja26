from graphics import * 

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin(width=800, height=800)

    # Plot a couple of pixels
    win.plotPixel(400, 400)
    win.plotPixel(0, 400, "red")
    # X increases to the right (normal)
    win.plotPixel(400, 0, "blue")
    # Y increases downwards!

    # Points
    p = Point(400, 400)
    p.draw(win)
    northeast = Point(600, 200)
    northeast.setOutline("green")
    northeast.draw(win)
    southeast = Point(600, 600)
    southeast.setOutline('red')
    southeast.draw(win)

    line1 = Line(southeast, northeast)
    line1.setOutline('purple')
    line1.setArrow('last')
    line1.draw(win)

    east = line1.getCenter()

    circle = Circle(east, 100)
    circle.setFill('yellow')
    circle.draw(win)

    rect = Rectangle(p, southeast)
    rect.setFill('green')
    rect.draw(win)

    northwest = Point(200, 200)
    ellipse = Oval(northwest, east)
    ellipse.setFill('purple')
    ellipse.draw(win)

    poly = Polygon(p, northwest, east, northeast)
    poly.setFill('cyan')
    poly.draw(win)

    instructions = Text(Point(400, 50), 'Click once to close')
    instructions.draw(win)

    # Wait for a mouse click
    win.getMouse()
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
