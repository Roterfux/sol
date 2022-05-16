from ursina.shaders import lit_with_shadows_shader
from ursina import *
import numpy as np
from random import random, randint, choice
from uuid import uuid4

pause = False


class Planet(object):

    def __init__(self, tex):
        self.entity = Entity(model='sphere', texture=tex, collider='sphere')
        self.entity.name = self.entity.texture.name
        #self.entity.name = str(uuid4())[:5]
        self.s = 0.1 + random() * .3
        self.r = 0.75 + random() * 5.1
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
            self.entity.rotation_y += time.dt * 20
        else:
            self.entity.rotation_y += time.dt * -20

        if self.entity.hovered:
            self.selector.visible = True
            self.text.position = (mouse.x, mouse.y+.03)
            self.text.visible = True
        else:
            self.selector.visible = False
            self.text.visible = False

    def show_name(self):
        selector = self.entity
        selector.color = color.rgba(255, 255, 0, 32)


class Sun(object):
    def __init__(self):
        Entity(model='sphere', color=color.yellow, scale=1, texture="tex/2k_sun", shader=lit_with_shadows_shader)
        #Entity(model='sphere', color=color.rgba(255, 255, 0, 96), scale=1.05, texture="tex/2k_sun")
        #Entity(model='sphere', color=color.rgba(255, 255, 0, 32), scale=1.15)


def update():

    for _ in p:
        _.update()
    key_action()
    #mouse_action()


def mouse_action():
    #mouse_pos = Text()
    #   x    y     z
    # 0.0 10.0 -20.0
    # 0.8  0.4 -----

    if window.center.x > mouse.x:
        camera.position -= (time.dt / 10, 0, 0)
    else:
        camera.position += (time.dt / 10, 0, 0)

    if window.center.y > mouse.y:
        camera.position -= (0, time.dt / 10, 0)
    else:
        camera.position += (0, time.dt / 10, 0)


def key_action():
    if held_keys['e']:
        camera.position += (0, time.dt, 0)
    if held_keys['q']:
        camera.position -= (0, time.dt, 0)
    if held_keys['w']:
        camera.position -= (0, 0, -time.dt)
    if held_keys['s']:
        camera.position -= (0, 0, time.dt)
    if held_keys['a']:
        camera.position -= (time.dt, 0, 0)
    if held_keys['d']:
        camera.position -= (-time.dt, 0, 0)
    if held_keys['x']:
        exit(0)


def input(key):
    if key == '1':
        camera.position = (0, 0, -20)
        camera.rotation_x = 0

    if key == '2':
        camera.position = (0, 20, 0)
        camera.rotation_x = 90

    if key == '3':
        camera.position = (0, 10, -20)
        camera.rotation_x = 30

    if key == "enter":
        global pause
        pause = not pause


def read_texture_names():
    import os
    textures = []
    with os.scandir("./tex/") as dirs:
        for entry in dirs:
            if "2k" in entry.name:
                textures.append(entry.name)
    return textures


app = Ursina()

EditorCamera()
pivot = Entity()
PointLight(parent=pivot, x=0, y=0, z=0, shadows=True)
SpotLight(parent=pivot, x=0, y=0, z=0, shadows=True)

p = []
for _ in range(8):
    p.append(Planet(tex="tex/" + read_texture_names()[_]))
sol = Sun()

#camera.rotation_z = 30
camera.position = (0, 10, -20)
camera.rotation_x = 25
window.color = color.rgba(10, 10, 10, 0)
app.run()
