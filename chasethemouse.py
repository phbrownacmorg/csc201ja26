from graphics import *
import math

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin(title="Chase the mouse",width=800, height=800)
    win.setCoords(-1, -1, 1, 1)

    num_clicks = 5

    instructions = Text(Point(0, 0.9), '') # start with empty text, so it can get drawn
    instructions.draw(win)
    distance_label = Text(Point(0, 0.85), '')
    distance_label.draw(win)

    mouse = Circle(Point(0, 0), 0.05)
    mouse.setFill('gray')
    mouse.draw(win)

    cat = Circle(Point(5, 0), 0.15) # Start well off the screen
    cat.setFill('orange')
    cat.draw(win)

    for i in range(num_clicks):
        instructions.setText('Clicks remaining: ' + str(num_clicks - i))
        click: Point = win.getMouse()
        mouse_pt = mouse.getCenter()
        mouse.move(click.getX() - mouse_pt.getX(), click.getY() - mouse_pt.getY())

        cat_pt = cat.getCenter()
        cat.move(mouse_pt.getX() - cat_pt.getX(), mouse_pt.getY() - cat_pt.getY())
        distance = math.dist([click.getX(), click.getY()], [mouse_pt.getX(), mouse_pt.getY()])
        distance_label.setText('Distance: ' + str(distance))

    instructions.setText('Click once more to exit')
    # Wait for a mouse click
    win.getMouse()
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
