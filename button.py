from graphics import * 

def inButton(click: Point, button: Rectangle) -> bool:
    """Return True if CLICK is in BUTTON; else return False."""
    p1 = button.getP1()
    p2 = button.getP2()
    min_x = min(p1.getX(), p2.getX())
    max_x = max(p1.getX(), p2.getX())
    min_y = min(p1.getY(), p2.getY())
    max_y = max(p1.getY(), p2.getY())
    return (max_x >= click.getX() >= min_x) and (max_y >= click.getY() >= min_y)

def makeButton(p1: Point, p2: Point, label_text: str, win: GraphWin) -> Rectangle:
    """Create and draw a button, consisting of a Rectangle defined by P1 and P2
        and a Text object, centered in the Rectangle and displaying LABEL_TEXT.
        Returns the Rectangle."""
    button = Rectangle(p1, p2)
    label = Text(button.getCenter(), label_text)
    button.draw(win)
    label.draw(win)
    return button

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin(width=800, height=800)
    win.setCoords(-1, -1, 1, 1) # Note: these may not be what you want! (but usually they are)

    button: Rectangle = makeButton(Point(-1, .8), Point(-.8, 1), 'Click', win)

    num_clicks = 4
    for i in range(num_clicks): # type: ignore
        if inButton(win.getMouse(), button):
            win.setBackground('green')
        else:
            win.setBackground('red')

    # Wait for a mouse click
    win.getMouse()
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
