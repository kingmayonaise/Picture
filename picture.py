"""
picture.py
Author: Daniel M
Credit: Myself, Dad, Internet

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
yellow=Color(0xffff00,1.0)
white=Color(0xffffff,1.0)
brown=Color(0x8b4513,1.0)
cloudwhite=Color(0xf5f5f5,1.0)
glassblue=Color(0xe0ffff,1.0)

thinline = LineStyle(1, black)
noline=LineStyle(0,white)

rectangleRed = RectangleAsset(170, 170, thinline, red)
cloud=EllipseAsset(60,40,thinline,cloudwhite)
sun=CircleAsset(100,thinline,yellow)
roof=PolygonAsset([(490,450),(680,450),(585,365),(490,450)],thinline,blue)
window=RectangleAsset(50,50,thinline,glassblue)
door=RectangleAsset(40,80,thinline,brown)
rainbowBase=EllipseAsset(350,300,thinline,white)
base=RectangleAsset(10000,1000,thinline,white)
rBlue=EllipseAsset(370,320,thinline,blue)
rRed=EllipseAsset(390,340,thinline,red)
rGreen=EllipseAsset(410,360,thinline,green)
rYellow=EllipseAsset(430,380,thinline,yellow)


Sprite(rYellow,(585,620))
Sprite(rGreen,(585,620))
Sprite(rRed,(585,620))
Sprite(rBlue,(585,620))
Sprite(rainbowBase,(585,620))
Sprite(base,(0,570))
Sprite(cloud,(200,150))
Sprite(cloud,(700,100))
Sprite(cloud,(400,250))
Sprite(sun,(0,0))
Sprite(rectangleRed,(500,450))
Sprite(roof)
Sprite(window,(520,470))
Sprite(window,(600,470))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
