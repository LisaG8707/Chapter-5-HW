from graphics import *
import math

def makePolygon(n):
    angle = 360 / n
    vertices = []
    radius = 150
    centerX = 250
    centerY = 250

    for i in range(n):
        degrees = i * angle
        radians = math.radians(degrees)

        x = centerX + radius * math.cos(radians)
        y = centerY + radius * math.sin(radians)

        vertices.append(Point(x, y))

    polygon = Polygon(vertices)
    return polygon

def drawPolygon(win, entry):
    win.getMouse()

    n = int(entry.getText())

    polygon = makePolygon(n)
    polygon.draw(win)

    return polygon

def main():
    win = GraphWin("N-Sided Polygon", 500, 500)

    label = Text(Point(150, 30), "Number of sides:")
    label.draw(win)

    entry = Entry(Point(275, 30), 5)
    entry.setText("5")
    entry.draw(win)

    button = Rectangle(Point(200, 60), Point(300, 100))
    button.draw(win)

    buttonText = Text(Point(250, 80), "Graph")
    buttonText.draw(win)

    drawPolygon(win, entry)

    buttonText.setText("Exit")

    win.getMouse()
    win.close()

main()
