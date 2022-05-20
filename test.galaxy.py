from ursina import *
import numpy as np
from uuid import uuid4

class Star(object):
    def __init__(self, x, y, z, color):
        self.id = str(uuid4())[:4]
        self.x = x
        self.y = y
        self.z = z
        self.entity = Entity(model='sphere', collider='sphere', x=x, y=y, z=z, scale=0.075, color=color)
        self.connection = 0
        self.nearest_star = None
        self.nearest_star_distance = 1000

    def update(self, connection, nearest_star, nearest_star_distance):
        self.connection = connection
        self.nearest_star = nearest_star
        self.nearest_star_distance = nearest_star_distance


app = Ursina()


EditorCamera()

angle = 0
radius = 0
count = 25


stars = []

for _ in range(count):
    angle += 10/count
    radius += .81
    x = np.sin(angle) * radius/10 + random.random()
    y = np.cos(angle) * radius/10 + random.random()
    #Entity(model="sphere", scale=0.1, x=x, y=y, color=color.white)
    stars.append(Star(x=x, y=0, z=y, color=color.white))
    x = -np.sin(angle) * radius/10 + random.random()
    z = -np.cos(angle) * radius/10 + random.random()
    #Entity(model="sphere", scale=0.1, x=x, y=y, color=color.yellow)
    stars.append(Star(x=x, y=0, z=y, color=color.yellow))


distance = []
cnt = 0
for i in stars:
    i.id = cnt
    max_distance = 1000
    for j in stars:
        if j.id == i.id:
            continue
        d = np.sqrt((i.x - j.x)**2 + (i.y - j.y)**2 + (i.z - j.z)**2)

        if max_distance > d:
            cnt += 1
            max_distance = d
            i.nearest_star = j

    print(i.id, i.nearest_star.id)


for star in stars:
    try:
        #print(star.id, star.nearest_star.id)
        points = [Vec3(star.x, star.y, star.z), Vec3(star.nearest_star.x, star.nearest_star.y, star.nearest_star.z)]
        curve_renderer = Entity(model=Mesh(vertices=points, mode='line'), color=color.blue)
    except:
        pass

#print(s[1].connection)


#camera.rotation_z = 30
camera.position = (0, 10, -20)
camera.rotation_x = 25
window.color = color.rgba(10, 10, 10, 0)
app.run()
