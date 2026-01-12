from graphics import *
from typing import cast
import math

def makeHead(r: float, color: str) -> list[GraphicsObject]:
    head = Circle(Point(0,0), r)
    head.setFill(color)
    head.setOutline(color)
    return [head]

def makeMouseEars(r: float, color: str) -> list[GraphicsObject]:
    ear_list: list[GraphicsObject] = []
    for side in [-1, 1]:
        angle = math.radians(60)
        p = Point(side * r * 1.5 * math.cos(angle), 
                  r * math.sin(angle) * 1.5)
        ear_radius = 0.65 * r
        ear = Circle(p, ear_radius)
        ear.setFill(color)
        ear.setOutline(color)
        ear_list.append(ear)
    return ear_list

def makeCatEars(r: float, color: str) -> list[GraphicsObject]:
    ear_list: list[GraphicsObject] = []
    for side in [-1, 1]:
        angle = math.radians(60)
        ear_angle = math.radians(25)
        outer_radius = 1.8 * r
        p1 = Point(side * outer_radius * math.cos(angle), 
                   outer_radius * math.sin(angle))
        p2 = Point(side * r * math.cos(angle + ear_angle),
                   r * math.sin(angle + ear_angle))
        p3 = Point(side * r * math.cos(angle - ear_angle),
                   r * math.sin(angle - ear_angle))
        ear = Polygon(p1, p2, p3)
        ear.setFill('orange')
        ear.setOutline('orange')
        ear_list.append(ear)
    return ear_list


def makeEyes(r: float, color: str) -> list[GraphicsObject]:
    """Make two eyes of the given COLOR, for a head with radius R.
    Return the eyes in a list."""
    eye_list: list[GraphicsObject] = []
    for side in [-1, 1]:
        p1 = Point(side * r * 0.15, 0)
        angle = math.radians(50)
        p2 = Point(side * r * math.cos(angle), r * math.sin(angle))
        eye = Oval(p1, p2)
        eye.setFill(color)
        eye_list.append(eye)
    return eye_list

def makeWhiskers(r: float) -> list[GraphicsObject]:
    """Make six whiskers for a head with radius R.  Return them as a list
    of GraphicsObject."""
    whiskerList: list[GraphicsObject] = []
    for side in [-1, 1]:
        for whisker_num in [-1, 0, 1]:
            angle = math.radians(-15)
            offset_angle = math.radians(7)
            whisker_angle = angle + whisker_num * offset_angle
            inner_radius = 0.8 * r
            outer_radius = 1.8 * r
            follicle = Point(side * inner_radius * math.cos(whisker_angle), 
                             inner_radius * math.sin(whisker_angle))
            tip = Point(side * outer_radius * math.cos(whisker_angle), 
                        outer_radius * math.sin(whisker_angle))
            whiskerList.append(Line(follicle, tip))
    return whiskerList

def makeMouseNose(nose_radius: float) -> GraphicsObject:
    nose = Circle(Point(0, 0), nose_radius)
    nose.setFill('pink')
    nose.setOutline('pink')
    return nose

def makeCatNose(nose_radius: float) -> GraphicsObject:
    bottom = Point(0, -nose_radius)
    left = Point(nose_radius/2, 0)
    right = Point(-nose_radius/2, 0)
    nose = Polygon(bottom, left, right)
    nose.setFill('pink')
    nose.setOutline('pink')
    return nose

def makeMouth(center_y: float, r: float) -> list[GraphicsObject]:
    """Make a mouth for a head of radius R, with the center Y offset CENTER_Y.
    Return the mouth as a list of GraphicsObject."""
    partsList: list[GraphicsObject] = []
    center = Point(0, center_y)
    for side in [-1, 1]:
        mouth_width = 0.5 * r
        mouth_angle = math.radians(-35)
        corner = Point(side * mouth_width * math.cos(mouth_angle),
                       center_y + mouth_width * math.sin(mouth_angle))
        half_mouth = Line(center, corner)
        partsList.append(half_mouth)
    return partsList

def animalCenter(animal: list[GraphicsObject]) -> Point:
    return cast(Circle, animal[0]).getCenter()

def moveAnimal(animal: list[GraphicsObject], dx: float, dy: float) -> None:
    for part in animal:
        part.move(dx, dy)

def drawAnimal(animal: list[GraphicsObject], w: GraphWin) -> None:
    for part in animal:
        part.draw(w)

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin(title="Chase the mouse",width=800, height=800)
    win.setCoords(-1, -1, 1, 1)

    num_clicks = 5

    instructions = Text(Point(0, 0.9), '') # start with empty text, so it can get drawn
    instructions.draw(win)
    distance_label = Text(Point(0, 0.85), '')
    distance_label.draw(win)

    # Make the mouse
    radius: float = 0.05
    mouse: list[GraphicsObject] = makeHead(radius, 'gray')
    mouse.extend(makeMouseEars(radius, 'gray'))
    mouse.extend(makeEyes(radius, 'black'))
    mouse.extend(makeWhiskers(radius))
    nose_radius = 0.15 * radius
    mouse.append(makeMouseNose(nose_radius))
    mouse.extend(makeMouth(-nose_radius, radius))
    drawAnimal(mouse, win)

    # Make the cat
    radius = 0.15
    cat: list[GraphicsObject] = makeHead(radius, 'orange')
    cat.extend(makeCatEars(radius, 'orange'))
    cat.extend(makeEyes(radius, 'green'))
    cat.extend(makeWhiskers(radius))
    nose_radius = 0.3 * radius
    cat.append(makeCatNose(nose_radius))
    cat.extend(makeMouth(-nose_radius, radius))
    moveAnimal(cat, 5, 0) # Start the cat well off the screen
    drawAnimal(cat, win)

    # Do the actual chase

    for i in range(num_clicks):
        instructions.setText('Clicks remaining: ' + str(num_clicks - i))
        click: Point = win.getMouse()

        mouse_pt: Point = animalCenter(mouse)
        moveAnimal(mouse, click.getX() - mouse_pt.getX(), click.getY() - mouse_pt.getY())

        cat_pt: Point = animalCenter(cat)
        moveAnimal(cat, mouse_pt.getX() - cat_pt.getX(), mouse_pt.getY() - cat_pt.getY())

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
