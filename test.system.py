from turtle import position

from ursina import *
import numpy as np
from random import random, randint
from uuid import uuid4


class Planet(object):

    def __init__(self, tex):
        self.entity = Entity(model='sphere', texture=tex, collider='sphere')
        self.entity.name = str(uuid4())[:5]
        self.s = 0.1 + random() * .2
        print(self.s)
        self.r = random() * 5
        self.angle = np.pi * (random() * 360.) / 180.
        self.rot_dir = randint(0, 1)
        #self.sec = 0

        self.selector = Entity(parent=self.entity, model=Circle(16, mode="line", thickness=6), color=color.yellow)
        self.selector.visible = False
        self.text = Text(self.entity.name)
        self.text.visible = False

    def update(self):
        self.entity.x = np.cos(time.dt + self.angle) * self.r
        self.entity.y = 0
        self.entity.z = np.sin(time.dt + self.angle) * self.r
        self.entity.scale = Vec3(self.s, self.s, self.s)
        if self.rot_dir == 0:
            self.entity.rotation_y += time.dt * 10
        else:
            self.entity.rotation_y += time.dt * -10

        if self.entity.hovered:
            print(self.entity.name)
            self.selector.visible = True
            self.text.position = (mouse.x, mouse.y+.03)
            self.text.visible = True
        else:
            self.selector.visible = False
            self.text.visible = False

    def show_name(self):
        print(self.entity.name)
        selector = self.entity
        selector.color = color.rgba(255, 255, 0, 32)


def update():
    global t
    t = t + 0.01
    angle = np.pi * 40 / 180

    for _ in p:
        _.update()

    #radius_1 = 1
    # mercury.x = np.cos(t) * radius_1
    # mercury.z = np.sin(t) * radius_1
    #
    # radius_2 = 1.4
    # venus.x = np.cos(t + angle) * radius_2
    # venus.z = np.sin(t + angle) * radius_2
    #
    # radius_3 = 1.8
    # earth.x = np.cos(t + angle * 2) * radius_3
    # earth.z = np.sin(t + angle * 2) * radius_3
    #
    # radius_4 = 2.2
    # mars.x = np.cos(t + angle * 3) * radius_4
    # mars.z = np.sin(t + angle * 3) * radius_4
    #
    # radius_5 = 2.6
    # jupiter.x = np.cos(t + angle * 4) * radius_5
    # jupiter.z = np.sin(t + angle * 4) * radius_5
    #
    # radius_6 = 3
    # saturn.x = np.cos(t + angle * 5) * radius_6
    # saturn.z = np.sin(t + angle * 5) * radius_6
    #
    # radius_7 = 3.4
    # uranus.x = np.cos(t + angle * 6) * radius_7
    # uranus.z = np.sin(t + angle * 6) * radius_7
    #
    # radius_8 = 3.8
    # neptune.x = np.cos(t + angle * 7) * radius_8
    # neptune.z = np.sin(t + angle * 7) * radius_8


app = Ursina()

#camera.position = (0, 3.7, -7.5)  # x, y, z

#sun = Entity(model='sphere', scale=1.5)

#mercury = Entity(model='sphere',scale=0.2)
#venus = Entity(model='sphere', scale=0.3)
#earth = Entity(model='sphere', scale=0.4)
#mars = Entity(model='sphere', scale=0.3)
#jupiter = Entity(model='sphere', scale=0.6)
#saturn = Entity(model='sphere', scale=0.5)
#uranus = Entity(model='sphere', scale=0.5)
#neptune = Entity(model='sphere', scale=0.5)


t = -np.pi
p = []
for _ in range(50):
    p.append(Planet(tex="tex/earth"))
print(len(p))

#camera.rotation_z = 0
camera.position = (0, 10, -20)
camera.rotation_x = 25
window.color = color.rgba(10, 10, 10, 0)
app.run()
