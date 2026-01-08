from graphics import * 

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin('Temperature converter', width=400, height=200)
    win.setCoords(-1, -1, 1, 1)

    font_size = 24

    instructions: Text = Text(Point(0, 0.5), 'Enter a temperature\nand click to convert')
    instructions.setSize(font_size)
    instructions.draw(win)

    temp_blank = Entry(Point(-0.5, -0.5), 4)
    temp_blank.setSize(font_size)
    temp_blank.draw(win)

    result = Text(Point(0.2, -0.5), '\u00b0C = \t')
    result.setSize(font_size)
    result.draw(win)

    # Click to convert
    win.getMouse()
    degC = float(temp_blank.getText())
    degF = degC * 1.8 + 32
    result.setText('\u00b0C = ' + str(round(degF, 1)) + '\u00b0F')
    instructions.setText('Click again to exit')

    # Wait for a mouse click
    win.getMouse()
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
