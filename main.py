
from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(100, 100, 150, 150)

    c2.draw_move(c3)

    c4 = Cell(win)
    c4.has_left_wall = False
    c4.draw(150, 100, 200, 150)

    c3.draw_move(c4, True)

    win.wait_for_close()

main()

    # Draw 1 line
    # l = Line(Point(50,50), Point(400,400))
    # win.draw_line(l, "black")


    # Draw 4 cells
    # c = Cell(win)
    # c.has_left_wall = False
    # c.draw(50, 50, 100, 100)

    # c = Cell(win)
    # c.has_right_wall = False
    # c.draw(125, 125, 200, 200)

    # c = Cell(win)
    # c.has_bottom_wall = False
    # c.draw(225, 225, 250, 250)

    # c = Cell(win)
    # c.has_top_wall = False
    # c.draw(300, 300, 500, 500)