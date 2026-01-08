from graphics import * 

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin(width=800, height=800)
    win.setCoords(-1, -1, 1, 1) # Note: these may not be what you want! (but usually they are)

    # Wait for a mouse click
    win.getMouse()
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
