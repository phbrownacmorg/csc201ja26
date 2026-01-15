from graphics import *
from typing import Any

def readParameters() -> tuple[float, float, float]:
    """Reads the parameters for an investment (amount, interest rate, and the
    percent growth to show) from the keyboard, and returns them (in that order).
    The interest rate and growth percentage are returned in absolute terms, not
    as percentages."""
    amt: float = float(input('Please enter an initial amount to invest: '))
    if amt < 0.01:
        raise ValueError('Amount to invest must be at least $0.01.') 
    rate: float = float(input('Please enter the interest rate, as a percentage: '))
    rate = rate / 100
    if rate < 0.0001:
        raise ValueError('Interest rate must be at least 0.01%.')
    growth: float = int(input('Please enter the amount of growth to show, as a percentage of the initial investment: '))
    growth = growth / 100
    if growth < 0.0001:
        raise ValueError('Growth percentage must be at leaast 0.01%.')
    return amt, rate, growth

def calcBalances(amt: float, rate: float, growth: float) -> list[float]:
    balances: list[float] = [amt] # balances[0] is the initial balance
    # 2. Loop
    while amt <= balances[0] * (1 + growth):
        interest: float = amt * rate
        # 3. Each time through the loop, the accumulator variable gets a little more of the answer
        amt = amt + interest
        balances.append(amt) # Save the successive amounts in a list
    return balances

def printTable(balances: list[float]) -> None:
    """Given a list of investment balances BALANCES, print them in a table."""
    # Make a (rough) table
        # Print the top of the table
    print('Period\tInterest\tBalance')
    print('-' * 40)
        # Print the initial balance
    print('Initial\t\t\t$', round(balances[0],2), sep='')
    # For each loan period, figure the interest and the new balance, and print them out
    for p in range(1, len(balances)):
        interest = balances[p] - balances[p-1]
        print((p), '$' + str(round(interest,2)), "", '$' + str(round(balances[p],2)), sep='\t')

def changeCoords(win: GraphWin, top_x: float, top_y: float, margin: float) -> None:
    """Set the coordinates on GraphWin WIN so it will comfortably hold a graph
    contained within the rectangle defined by (0, 0) and (TOP_X, TOP_Y), with
    a margin MARGIN around the edges."""
    max_X = top_x * (1 + margin)
    min_X = top_x * -margin
    max_Y = top_y * (1 + margin)
    min_Y = top_y * -margin
    win.setCoords(min_X, min_Y, max_X, max_Y)

def drawAxes(win: GraphWin, x_end: float, y_end: float) -> None:
    """Draw axes on GraphWin WIN.  The x-axis runs from the origin to (X_END, 0),
        and the y-axis runs from the origin to (0, Y_END)."""
    xAxis = Line(Point(0,0), Point(x_end, 0))
    xAxis.setArrow('last')
    xAxis.draw(win)
    yAxis = Line(Point(0,0), Point(0, y_end))
    yAxis.setArrow('last')
    yAxis.draw(win)

def drawXLabels(win: GraphWin, labels: list[Any], y_offset: float) -> None:
    """On GraphWin WIN, draw X-axis labels from the list LABELS, with an offset
        in y of Y_OFFSET."""
    for i in range(len(labels)):
        label = Text(Point(i + 0.5, y_offset), str(labels[i]))
        label.draw(win)

def drawBars(win: GraphWin, balances: list[float]) -> None:
    """On GraphWin WIN, make bars for a bar graph of the sequence of values BALANCES."""
    for i in range(len(balances)):
        bar = Rectangle(Point(i, 0), Point(i+1, balances[i]))
        bar.setFill('green')
        bar.draw(win)

def labelBars(win: GraphWin, balances: list[float], offset: float) -> None:
    """On GraphWin WIN, create bar labels for bars representing a sequence of
    values BALANCES.  The labels are offset by OFFSET from the top of each
    bar.  The labels are printed with dollar signs."""
    for i in range(len(balances)):
        label = Text(Point(i + 0.5, balances[i] + offset), 
                     '$' + str(round(balances[i])))
        label.draw(win)

def graphBalances(balances: list[float]) -> None:
    """Make a bar graph of a series of investment balances BALANCES, and wait for
    a mouse click.  Because of the wait for a mouse click, this function should be
    called *after* other forms of output have happened."""
    # Prepare the window
    win: GraphWin = GraphWin(title="Investment growth", width=800, height=800)
    max_value = max(balances)
    margin = 0.1
    num_bars = len(balances)
    changeCoords(win, num_bars, max_value, margin)

    # Draw the graph
    drawAxes(win, num_bars * (1+(margin/2)), max_value * (1+(margin/2)))
    drawXLabels(win, list(range(num_bars)), -0.25 * max_value * margin)
    drawBars(win, balances)
    labelBars(win, balances, 0.25 * max_value * margin)

    # Wait for a mouse click
    win.getMouse()
    win.close()


def main(args: list[str]) -> int:
    # Read the parameters for an investment
        # Initial amount, interest rate, number of investment periods (months, years, whatever)
    # 1. Accumulator variable
    try:
        amt, rate, growth = readParameters()
    except ValueError as e:
        if 'could not convert' in e.args[0]:
            print('Inputs must all be positive numbers.')
        else:
            print(e)
    else:
        # Print out the parameters
        print('Investing $', amt, ' at ', rate, "% until it grows by ", growth, '%', sep="")
        balances = calcBalances(amt, rate, growth)
        printTable(balances)
        graphBalances(balances)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
