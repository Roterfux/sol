
import random

from ursina import *
import numpy as np
from uuid import uuid4


class Star(object):
    def __init__(self, x, y, z, color):
        self.id = str(uuid4())[:4]
        self.x = x
        self.y = y
        self.z = z
        self.entity = Entity(model='sphere', collider='sphere', x=x, y=y, z=z, scale=0.05, color=color)
        #Sprite('tex/light', filtering=False, scale=0.05, color=color, x=x, y=y, z=z, double_sided=True, rotation=(0, 0, 0))
        #Sprite('tex/light', filtering=False, scale=0.05, color=color, x=x, y=y, z=z, double_sided=True, rotation=(0, 90, 0))
        #Sprite('tex/light', filtering=False, scale=0.05, color=color, x=x, y=y, z=z, double_sided=True, rotation=(0, 90, 90))
        #Sprite('tex/light', filtering=False, scale=0.05, color=color, x=x, y=y, z=z, double_sided=True, rotation=(90, 0, 0))

        self.connection = 0
        self.nearest_star = []
        self.nearest_star_distance = 1000

    def update(self, connection, nearest_star, nearest_star_distance):
        self.connection = connection
        self.nearest_star = nearest_star
        self.nearest_star_distance = nearest_star_distance


app = Ursina()


EditorCamera()

angle = 0
radius = 0
count = 100


stars = []

for _ in range(count):
    angle += 10/count
    radius += .3
    x = np.sin(angle) * radius/10 + random.random()
    z = np.cos(angle) * radius/10 + random.random()
    y = random.random()/2
    #Entity(model="sphere", scale=0.1, x=x, y=y, color=color.white)
    stars.append(Star(x=x, y=y, z=z, color=color.white))
    x = -np.sin(angle) * radius/10 + random.random()
    z = -np.cos(angle) * radius/10 + random.random()
    y = -random.random() / 2
    #Entity(model="sphere", scale=0.1, x=x, y=y, color=color.yellow)
    stars.append(Star(x=x, y=y, z=z, color=color.yellow))


#distance = []
cnt = 0
for star in stars:
    star.id = cnt
    max_distance = 100
    cnt += 1
    for j in stars:
        if j.id == star.id:
            continue
        d = np.sqrt(np.power(star.x - j.x, 2) + np.power(star.y - j.y, 2) + np.power(star.z - j.z, 2))

        if max_distance > d:
            max_distance = d
            star.nearest_star.append(j)

for star in stars:
    try:
        print(star.id, star.nearest_star[-1].id)
        points = [Vec3(star.x, star.y, star.z), Vec3(star.nearest_star[-1].x, star.nearest_star[-1].y, star.nearest_star[-1].z)]
        if star.z < 0:
            t = 100
        else:
            t = 50
        Entity(model=Mesh(vertices=points, mode='line', thickness=2), color=rgb(255, 255, 0, t / 3))
        Entity(model=Mesh(vertices=points, mode='line', thickness=1), color=rgb(255, 255, 255, t / 3))
        #print(star.id, star.nearest_star[-2].id)
        points = [Vec3(star.x, star.y, star.z), Vec3(star.nearest_star[-2].x, star.nearest_star[-2].y, star.nearest_star[-2].z)]
        Entity(model=Mesh(vertices=points, mode='line', thickness=2), color=rgb(255, 255, 0, t / 3))
        Entity(model=Mesh(vertices=points, mode='line', thickness=1), color=rgb(255, 255, 255, t / 3))
        #print(star.z)
    except:
        pass

#print(s[1].connection)

camera.orthographic = True
camera.fov = 5
Sprite.ppu = 16
Texture.default_filtering = None

#camera.rotation_z = 30
camera.position = (0, 10, -20)
camera.rotation_x = 25
window.color = color.rgba(10, 10, 10, 0)
app.run()
