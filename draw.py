from display import *
import math

def draw_line( x0, y0, x1, y1, screen, color):
    A = y1 - y0
    B = -(x1 - x0)
    x = x0
    y = y0
    m = (float(y1-y0)/float(x1-x0))

    if (x1 < x0):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #vertical lines
    if (x0 == x1):
         if(y1 < y0):
            y0, y1 = y1, y0
        for i in range(y0, y1 + 1):
            plot(screen, color, int(x0), int(i))

    #octant 1/5 / horizontal lines
    if (0 >= m and m <= 1):
        d1 = (2 * A) + B

        while x <= x1:
            plot(screen, color, int(x), int(y))

            if(d1 > 0):
                y = y+1
                d1 = d1 + (2 * B)
            x = x + 1
            d1 = d1 + (2 * A)

    #octant 2/6
    if (1 < m):
        d2 = A + (2 * B)

        while y <= y1:
            plot(screen, color, int(x), int(y))

            if(d2 < 0):
                x = x+1
                d2 = d2 + (2 * A)
            y = y + 1
            d2 = d2 + (2 * B)

    #octant 8/4
    if (-1 > m):
        d3 = A - (2 * B)

        while y >= y1:
            plot(screen, color, int(x), int(y))

            if(d3 > 0):
                x = x+1
                d3 = d3 + (2 * A)
            y = y - 1
            d3 = d3 - (2 * B)

    #octant 7/3 / horizontal lines
    if(m <= 0 and m >= -1):
        d4 = B + (2 * A)

        while x <= x1:
            plot(screen, color, int(x), int(y))

            if(d4 < 0):
                y = y-1
                d4 = d4 - (2 * B)
            x = x + 1
            d4 = d4 + (2 * A)


    return True
