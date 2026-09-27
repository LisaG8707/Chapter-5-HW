from graphics import *

def logistic(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
    return x

def main():
    win = GraphWin("Logistic Function", 600, 500)

    xAxis = Line(Point(50, 450), Point(550, 450))
    xAxis.draw(win)

    yAxis = Line(Point(50, 450), Point(50, 50))
    yAxis.draw(win)

    x = float(input("Enter the starting value for x: "))
    k = float(input("Enter the value for k: "))

    for i in range(100):
        x = logistic(k, x, 1)

        graphX = 50 + i * 5
        graphY = 450 - x * 400

        point = Point(graphX, graphY)
        point.draw(win)

    win.getMouse()
    win.close()

main()
