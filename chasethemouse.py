from graphics import *
from typing import cast
import math

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
    mouse: list[GraphicsObject] = [Circle(Point(0, 0), radius)]
    mouse[0].setFill('gray')
    mouse[0].setOutline('gray')
    mouse[0].draw(win)

    ## Add ears
    for side in [-1, 1]:
        angle = math.radians(60)
        p = Point(side * radius * 1.5 * math.cos(angle), 
                  radius * math.sin(angle) * 1.5)
        ear_radius = 0.65 * radius
        ear = Circle(p, ear_radius)
        ear.setFill('gray')
        ear.setOutline('gray')
        ear.draw(win)
        mouse.append(ear)

    ## Add eyes
    for side in [-1, 1]:
        p1 = Point(side * radius * 0.15, 0)
        angle = math.radians(50)
        p2 = Point(side * radius * math.cos(angle), radius * math.sin(angle))
        eye = Oval(p1, p2)
        eye.setFill('black')
        eye.draw(win)
        mouse.append(eye)

    ## Add whiskers
    for side in [-1, 1]:
        for whisker_num in [-1, 0, 1]:
            angle = math.radians(-15)
            offset_angle = math.radians(10)
            whisker_angle = angle + whisker_num * offset_angle
            inner_radius = 0.8 * radius
            outer_radius = 1.8 * radius
            follicle = Point(side * inner_radius * math.cos(whisker_angle), 
                             inner_radius * math.sin(whisker_angle))
            tip = Point(side * outer_radius * math.cos(whisker_angle), 
                        outer_radius * math.sin(whisker_angle))
            whisker = Line(follicle, tip)
            whisker.draw(win)
            mouse.append(whisker)
            
    ## Add a nose
    nose_radius = 0.15 * radius
    nose = Circle(Point(0, 0), nose_radius)
    nose.setFill('pink')
    nose.setOutline('pink')
    nose.draw(win)
    mouse.append(nose)

    ## Add a mouth
    center_y = -nose_radius
    center = Point(0, center_y)
    for side in [-1, 1]:
        mouth_width = 0.5 * radius
        mouth_angle = math.radians(-35)
        corner = Point(side * mouth_width * math.cos(mouth_angle),
                       center_y + mouth_width * math.sin(mouth_angle))
        half_mouth = Line(center, corner)
        half_mouth.draw(win)
        mouse.append(half_mouth)

    # Make the cat
    radius = 0.15
    cat: list[GraphicsObject] = [Circle(Point(5, 0), radius)] # Start well off the screen
    cat[0].setFill('orange')
    cat[0].setOutline('orange')
    cat[0].draw(win)

    ## Add ears
    for side in [-1, 1]:
        angle = math.radians(60)
        ear_angle = math.radians(25)
        outer_radius = 1.8 * radius
        p1 = Point(5 + side * outer_radius * math.cos(angle), 
                   outer_radius * math.sin(angle))
        p2 = Point(5 + side * radius * math.cos(angle + ear_angle),
                   radius * math.sin(angle + ear_angle))
        p3 = Point(5 + side * radius * math.cos(angle - ear_angle),
                   radius * math.sin(angle - ear_angle))
        ear = Polygon(p1, p2, p3)
        ear.setFill('orange')
        ear.setOutline('orange')
        ear.draw(win)
        cat.append(ear)

    ## Add eyes
    for side in [-1, 1]:
        p1 = Point(5 + side * radius * 0.1, 0)
        angle = math.radians(50)
        p2 = Point(5 + side * radius * math.cos(angle), radius * math.sin(angle))
        eye = Oval(p1, p2)
        eye.setFill('green')
        eye.draw(win)
        cat.append(eye)

    ## Add whiskers
    for side in [-1, 1]:
        for whisker_num in [-1, 0, 1]:
            angle = math.radians(-15)
            offset_angle = math.radians(8)
            whisker_angle = angle + whisker_num * offset_angle
            inner_radius = 0.8 * radius
            outer_radius = 1.8 * radius
            follicle = Point(5 + side * inner_radius * math.cos(whisker_angle), 
                             inner_radius * math.sin(whisker_angle))
            tip = Point(5 + side * outer_radius * math.cos(whisker_angle), 
                        outer_radius * math.sin(whisker_angle))
            whisker = Line(follicle, tip)
            whisker.draw(win)
            cat.append(whisker)
    
    ## Add a nose
    nose_radius = -0.3 * radius
    bottom = Point(5, nose_radius)
    left = Point(5 + nose_radius/2, 0)
    right = Point(5 - nose_radius/2, 0)
    nose = Polygon(bottom, left, right)
    nose.setFill('pink')
    nose.setOutline('pink')
    nose.draw(win)
    cat.append(nose)

    ## Add a mouth
    center_y = nose_radius  # Already negative
    center = Point(5, center_y)
    for side in [-1, 1]:
        mouth_width = 0.5 * radius
        mouth_angle = math.radians(-30)
        corner = Point(5 + side * mouth_width * math.cos(mouth_angle),
                       center_y + mouth_width * math.sin(mouth_angle))
        half_mouth = Line(center, corner)
        half_mouth.draw(win)
        cat.append(half_mouth)

    # Do the actual chase

    for i in range(num_clicks):
        instructions.setText('Clicks remaining: ' + str(num_clicks - i))
        click: Point = win.getMouse()
        mouse_pt: Point = cast(Circle, mouse[0]).getCenter()
        for part in mouse:
            part.move(click.getX() - mouse_pt.getX(), click.getY() - mouse_pt.getY())

        cat_pt: Point = cast(Circle, cat[0]).getCenter()
        for part in cat:
            part.move(mouse_pt.getX() - cat_pt.getX(), mouse_pt.getY() - cat_pt.getY())
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
