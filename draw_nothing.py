from graphics import * 

def main(args: list[str]) -> int:
    win: GraphWin = GraphWin(width=800, height=800)

    # Wait for a mouse click
    win.getMouse()
    win.close()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
