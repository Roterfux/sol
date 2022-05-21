
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
        self.scale = 0.05
        self.entity = Entity(model='sphere', collider='sphere', x=x, y=y, z=z, scale=0.05, color=color)
        #self.entity = Sprite('tex/light', filtering=False, scale=0.05, color=color, x=x, y=y, z=z, double_sided=True, rotation=(0, 0, 0))
        #Sprite('tex/light', filtering=False, scale=0.05, color=color, x=x, y=y, z=z, double_sided=True, rotation=(0, 90, 0))
        #Sprite('tex/light', filtering=False, scale=0.05, color=color, x=x, y=y, z=z, double_sided=True, rotation=(0, 0, 90))
        #Sprite('tex/light', filtering=False, scale=0.05, color=color, x=x, y=y, z=z, double_sided=True, rotation=(90, 0, 0))

        self.connection = 0
        self.nearest_star = []
        self.nearest_star_distance = 1000
        # % 5.4f' %(3.141592))
        self.text = Text("%1.2f" % self.x + " " + "%1.2f" % self.y  + " " "%1.2f" % self.z)
        self.text.visible = False
        if int(self.z*10) <= -2:
            self.entity.scale = 0.05
        elif int(self.z*10) == -1:
            self.entity.scale = 0.04
        elif int(self.z*10) == 1:
            self.entity.scale = 0.03
        elif int(self.z*10) >= 2:
            self.entity.scale = 0.02

    def update(self):
        #
        if self.entity.hovered:
            self.text.position = (mouse.x, mouse.y+.03)
            self.text.visible = True
        else:
            self.text.visible = False



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
        #print(star.id, star.nearest_star[-1].id)
        print(star.z*10)
        points = [Vec3(star.x, star.y, star.z), Vec3(star.nearest_star[-1].x, star.nearest_star[-1].y, star.nearest_star[-1].z)]
        if int(star.z*10) <= -2:
            t = 128
        elif int(star.z*10) == -1:
            t = 96
        elif int(star.z*10) == 1:
            t = 64
        elif int(star.z*10) >= 2:
            t = 48
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


def update():
    for star in stars:
        star.update()

camera.orthographic = True
camera.fov = 5
Sprite.ppu = 16
Texture.default_filtering = None

#camera.rotation_z = 30
camera.position = (0, 10, -20)
camera.rotation_x = 25
window.color = color.rgba(10, 10, 10, 0)
app.run()
