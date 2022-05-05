from ursina import *
import numpy as np
from random import random, randint, choice
from uuid import uuid4


class Planet(object):

    def __init__(self, tex):
        self.entity = Entity(model='sphere', texture=tex, collider='sphere')
        self.entity.name = str(uuid4())[:5]
        self.s = 0.1 + random() * .3
        self.r = random() * 5
        print(self.r)
        self.angle = np.pi * (random() * 360.) / 180.
        self.rot_dir = randint(0, 1)
        #self.sec = 0
        self.t = -np.pi

        self.selector = Entity(parent=self.entity, model=Circle(16, mode="line", thickness=6), color=color.yellow)
        self.selector.visible = False
        self.text = Text(self.entity.name)
        self.text.visible = False

    def update(self):
        self.t += 0.002

        self.entity.x = np.cos(self.t + self.angle) * self.r
        self.entity.y = 0
        self.entity.z = np.sin(self.t + self.angle) * self.r
        self.entity.scale = Vec3(self.s, self.s, self.s)
        if self.rot_dir == 0:
            self.entity.rotation_y += time.dt * 10
        else:
            self.entity.rotation_y += time.dt * -10

        if self.entity.hovered:
            self.selector.visible = True
            self.text.position = (mouse.x, mouse.y+.03)
            self.text.visible = True
        else:
            self.selector.visible = False
            self.text.visible = False

        print(time.dt)

    def show_name(self):
        selector = self.entity
        selector.color = color.rgba(255, 255, 0, 32)


class Sun(object):
    def __init__(self):
        Entity(model='sphere', color=color.yellow, scale=1, texture="tex/2k_sun")
        Entity(model='sphere', color=color.rgba(255, 255, 0, 128), scale=1.05, texture="tex/2k_sun")
        Entity(model='sphere', color=color.rgba(255, 255, 0, 32), scale=1.15)


def update():

    for _ in p:
        _.update()


app = Ursina()

textures = [
    "2k_jupiter",
    "2k_mars",
    "2k_moon",
    "earth"
]

p = []
for _ in range(8):
    p.append(Planet(tex="tex/" + choice(textures)))
sol = Sun()

#camera.rotation_z = 30
camera.position = (0, 10, -20)
camera.rotation_x = 25
window.color = color.rgba(10, 10, 10, 0)
app.run()
