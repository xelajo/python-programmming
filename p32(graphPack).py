from graphics.circle import *
from graphics.rectangle import *
from graphics.dgraphics.cuboid import *
from graphics.dgraphics.sphere import *
r = int(input("Enter the radius of circle:"))
carea(r)
cperi(r)
lr = int(input("Enter the length of rectangle:"))
br = int(input("Enter the breadth of rectangle:"))
rarea(lr, br)
rperi(lr, br)
lc = int(input("Enter the length of cuboid:"))
bc = int(input("Enter the breadth of cuboid:"))
hc = int(input("Enter the height of cuboid:"))
cuarea(lc, bc, hc)
cuperi(lc, bc, hc)
r = int(input("Enter the radius of sphere:"))
sarea(r)
speri(r)
