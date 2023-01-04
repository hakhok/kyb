from vpython import *

# create the floor
floor = box(pos=vector(0,0,0), size=vector(10,0.5,10), color=color.green)

# create the walls
wall1 = box(pos=vector(-4.5,5,-4.5), size=vector(0.5,10,10), color=color.yellow)
wall2 = box(pos=vector(4.5,5,-4.5), size=vector(0.5,10,10), color=color.yellow)
wall3 = box(pos=vector(-4.5,5,4.5), size=vector(9,10,0.5), color=color.yellow)

# create the roof
roof = pyramid(pos=vector(0,10,0), size=vector(9,1,9), color=color.red)

# create the door
door = box(pos=vector(0,0,4.5), size=vector(2,3,0.5), color=color.brown)

# create the windows
window1 = box(pos=vector(-4.5,2.5,-4.5), size=vector(1,1,1), color=color.blue)
window2 = box(pos=vector(4.5,2.5,-4.5), size=vector(1,1,1), color=color.blue)
