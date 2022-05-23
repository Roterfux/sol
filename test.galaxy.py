
import random

from ursina import *
import numpy as np
from uuid import uuid4


class Star(object):
    def __init__(self, x, y, z, c):
        self.id = str(uuid4())[:4]
        self.x = x
        self.y = y
        self.z = z
        self.scale = 0.05
        self.sphere = Entity(model='sphere', collider='sphere', x=x, y=y, z=z, scale=0.05, color=rgb(0, 0, 0, 0))
        self.entity = [Sprite('tex/light', filtering=False, scale=0.04, color=c, x=x, y=y, z=z, double_sided=True, rotation=(0, 0, 0))]
        self.entity.append(Sprite('tex/light', filtering=False, scale=0.04, color=c, x=x, y=y, z=z, double_sided=True, rotation=(0, 90, 0)))
        self.entity.append(Sprite('tex/light', filtering=False, scale=0.04, color=c, x=x, y=y, z=z, double_sided=True, rotation=(0, 0, 90)))
        self.entity.append(Sprite('tex/light', filtering=False, scale=0.04, color=c, x=x, y=y, z=z, double_sided=True, rotation=(90, 0, 0)))

        self.connection = 0
        self.nearest_star = []
        self.nearest_star_distance = 1000
        # % 5.4f' %(3.141592))
        self.text = Text("%1.2f" % self.x + " " + "%1.2f" % self.y  + " " "%1.2f" % self.z)
        self.text.visible = False
        s = 0
        z_temp = int(self.z * 10)
        if z_temp <= -2:
            s = 0.1
        elif z_temp == -1:
            s = 0.08
        elif z_temp == 1:
            s = 0.06
        elif z_temp >= 2:
            s = 0.04

        for e in self.entity:
            e.scale = s

    def update(self):
        #
        if self.sphere.hovered:
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
    y = random.random()/2.5
    #Entity(model="sphere", scale=0.1, x=x, y=y, color=color.white)
    stars.append(Star(x=x, y=y, z=z, c=color.white))
    x = -np.sin(angle) * radius/10 + random.random()
    z = -np.cos(angle) * radius/10 + random.random()
    y = -random.random() / 2.5
    #Entity(model="sphere", scale=0.1, x=x, y=y, color=color.yellow)
    stars.append(Star(x=x, y=y, z=z, c=color.white))


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
        #print(star.z*10)
        points = [Vec3(star.x, star.y, star.z), Vec3(star.nearest_star[-1].x, star.nearest_star[-1].y, star.nearest_star[-1].z)]
        star_calc = int(star.z * 10)
        if star_calc <= -2:
            t = 128
        elif star_calc == -1:
            t = 96
        elif star_calc == 1:
            t = 64
        elif star_calc >= 2:
            t = 48
        else:
            t = 32
        Entity(model=Mesh(vertices=points, mode='line', thickness=2), color=rgb(0, 64, 255, t / 3))
        Entity(model=Mesh(vertices=points, mode='line', thickness=1), color=rgb(255, 255, 255, t / 3))
        #print(star.id, star.nearest_star[-2].id)
        points = [Vec3(star.x, star.y, star.z), Vec3(star.nearest_star[-2].x, star.nearest_star[-2].y, star.nearest_star[-2].z)]
        Entity(model=Mesh(vertices=points, mode='line', thickness=2), color=rgb(0, 64, 255, t / 3))
        Entity(model=Mesh(vertices=points, mode='line', thickness=1), color=rgb(255, 255, 255, t / 3))
        #print(star.z)
    except:
        pass


def update():
    for star in stars:
        star.update()


camera.orthographic = True
camera.fov = 5
Sprite.ppu = 16
Texture.default_filtering = None

window.vsync = False
#editor_ui = True
#camera.rotation_z = 30
camera.position = (0, 10, -20)
camera.rotation_x = 25
window.color = color.rgba(10, 10, 10, 0)
app.run()
