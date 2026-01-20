from graphics import *

def getPoint(w: GraphWin, label_pt: Point) -> Point:
    click: Point = w.getMouse()
    click.draw(w)
    pt_label = Text(label_pt, f'({click.getX():.4f},{click.getY():.4f})')
    pt_label.draw(w)
    return click

def distance_label(p1: Point, p2: Point, label_pt: Point) -> Text:
    import math
    distance = math.dist((p1.getX(), p1.getY()), (p2.getX(), p2.getY()))
    label = Text(label_pt, f'Distance: {distance:.4f}')
    return label

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin(width=800, height=800)
    win.setCoords(-1, -1, 1, 1) # Note: these may not be what you want! (but usually they are)
    label_spacing = 0.05
    label_pt = Point(0, 1 - label_spacing)
    instructions = Text(label_pt, 'Click to set a point')
    instructions.draw(win)

    label_pt = Point(label_pt.getX(), label_pt.getY() - label_spacing)
    p1 = getPoint(win, label_pt)
    label_pt = Point(label_pt.getX(), label_pt.getY() - label_spacing)
    p2 = getPoint(win, label_pt)

    line = Line(p1, p2)
    line.draw(win)
    label_pt = Point(label_pt.getX(), label_pt.getY() - label_spacing)
    distance_label(p1, p2, label_pt).draw(win)

    instructions.setText('Click again to exit')
    # Wait for a mouse click
    win.getMouse()
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
