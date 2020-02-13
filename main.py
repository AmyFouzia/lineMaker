from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

#octants 1 and 5
#draw_line(0, 0, XRES-1, YRES-1, s, c)
#draw_line(0, 0, XRES-1, YRES / 2, s, c)
#draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)
#WORKS

#octants 8 and 4
#c[BLUE] = 255;
#draw_line(0, YRES-1, XRES-1, 0, s, c);
#draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
#draw_line(XRES-1, 0, 0, YRES/2, s, c);
#WORKS

#octants 2 and 6
c[RED] = 255;
c[GREEN] = 0;
c[BLUE] = 0;
draw_line(0, 0, XRES/2, YRES-1, s, c); #WORKS
draw_line(XRES-1, YRES-1, XRES/2, 0, s, c); #DOESNT WORK
#draw_line(499, 499, 250, 0, s, c) m = pos

#octants 7 and 3
#c[BLUE] = 255;
#draw_line(0, YRES-1, XRES/2, 0, s, c); #WORKS
draw_line(XRES-1, 0, XRES/2, YRES-1, s, c); #DOESNT WORK
#draw_line(499, 0, 250, 499, s, c) m = pos
print(XRES-1, XRES/2, YRES-1)

#horizontal and vertical
#c[BLUE] = 0;
#c[GREEN] = 255;
#draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
#draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);
#WORKS


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
