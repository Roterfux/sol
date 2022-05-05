from ursina import *  # import ursina engine
import sqlite3

pause = False


def update():
    mouse_action()
    if not pause:
        for entity in sol:
            entity.rotation_y += time.dt * 10
        for entity in planet1:
            entity.rotation_y += time.dt * 50
        #for entity in moons1:
        #    entity.rotation_y -= time.dt * 100

    diff = sqrt((sol[0].x - mouse.x) ** 2 + (sol[0].y - mouse.y) ** 2 + sol[0].z ** 2)
    #print(diff)
    diff_x = sol[0].x - mouse.x
    print(diff_x)

    key_action()



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


def mouse_action():

    if mouse.hovered_entity == sol[0]:
        info.visible = True
        info.x = mouse.x + .025
        info.y = mouse.y - .025

    else:
        info.visible = False


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

    if key == "space":
        global pause
        pause = not pause


def star():
    sun = Entity(model='sphere', position=(0, 0, 0), color=color.yellow, scale=2, texture="tex/2k_sun", collider="sphere")
    corona = Entity(model='sphere', position=(0, 0, 0), color=color.rgba(255, 255, 0, 128), scale=2.05, texture="tex/2k_sun")
    corona2 = Entity(model='sphere', position=(0, 0, 0), color=color.rgba(255, 255, 0, 32), scale=2.15)

    return [sun, corona, corona2]


def planet(position, texture, scale):
    sphere = Entity(model='sphere', position=position, scale=scale, texture=texture)
    sphere_atmosphere = Entity(model='sphere', position=position, color=color.rgba(0, 0, 128, 96), scale=scale+scale*0.1, collider='sphere')#, on_click=show_name)

    return [sphere, sphere_atmosphere]


def moon(parent):
    for _ in range(10):
        satellite = Entity(parent=parent, model='sphere', color=color.white, position=(1 + random.random() * 1.3, 0, 0), scale=0.1 * random.random(), texture="tex/2k_moon",
                           rotation_y=random.random() * 180)
    return [satellite]


def show_name():
    Text.size = 0.002
    Text.default_resolution = 100
    text_name = Text(text="Earth")
    text_name.x = mouse.x / 25.
    text_name.y = mouse.y / 25.
    text_name.visible = True
    print("Click!")


def setup():
    camera.position = (0, 3.7, -7.5)  # x, y, z
    camera.rotation_x = 30
    # window.fullscreen = False  # Go full screen
    window.exit_button.visible = True  # Show the in-game red X that loses the window
    window.fps_counter.enabled = True  # Show the FPS (Frames per second) counter
    window.center_on_screen()
    window.color = color.rgba(10, 10, 10, 0)


def db_test():
    con = sqlite3.connect('sol.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    con.commit()

    for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
    cur.execute("DROP TABLE stocks")
    con.close()


app = Ursina()

sol = star()
planet1 = planet(position=(2, 0, 2), scale=0.2, texture="tex/earth")
#planet2 = planet(position=(2, 0, 2), texture="tex/2k_mars")
#planet3 = planet(position=(3, 0, 3), texture="tex/2k_jupiter")
moons1 = moon(planet1[0])
#moons2 = moon(planet2[0])

db_test()
info = Text(text="This is a test", color=color.white, scale=1)
info.background = True

setup()

app.run()
