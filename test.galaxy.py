from ursina import *
import numpy as np


class Star(object):
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.entity = Entity(model='sphere', collider='sphere', x=x, y=y, z=z, scale=0.075, color=color)
        self.connection = 0
        self.nearest_star = []

    def update(self, connection, nearest_star):
        self.connection = connection
        self.nearest_star = nearest_star


app = Ursina()


EditorCamera()

angle = 0
radius = 0
count = 70

s = []

for _ in range(count):
    angle += 10/count
    radius += .8
    x = np.sin(angle) * radius/10 + random.random()
    y = np.cos(angle) * radius/10 + random.random()
    #Entity(model="sphere", scale=0.1, x=x, y=y, color=color.white)
    star_left = Star(x=x, y=0, z=y, color=color.white)
    x = -np.sin(angle) * radius/10 + random.random()
    z = -np.cos(angle) * radius/10 + random.random()
    #Entity(model="sphere", scale=0.1, x=x, y=y, color=color.yellow)
    star_right = Star(x=x, y=0, z=y, color=color.yellow)
    s.append(star_left)
    s.append(star_right)

distance = []
for i in s:
    for j in s:
        d = np.sqrt((i.x - j.x)**2 + (i.y - j.y)**2 + (i.z - j.z)**2)
        distance.append(d)

        #calc closet stars (1-3) and connect

        if d < 1:
            print(d)
            #line_renderer = Entity(model=Mesh(vertices=[Vec3(0), Vec3(0)], mode='line', thickness=5), z=.1, color=color.white)

            if i.connection < 2 and j.connection < 1:
                i.connection += 1
                points = [Vec3(i.x, i.y, i.z), Vec3(j.x, j.y, j.z)]
                curve_renderer = Entity(model=Mesh(vertices=points, mode='line'), color=color.blue)

print(s[1].connection)


#camera.rotation_z = 30
camera.position = (0, 10, -20)
camera.rotation_x = 25
window.color = color.rgba(10, 10, 10, 0)
app.run()
