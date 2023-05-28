from ursina import *
import random
from direct.actor.Actor import Actor

app = Ursina()

Sky()

ground = Entity(model='plane', texture='assets/pasir.jpg',
                collider='mesh', scale=(250, 20, 250))

player = Entity(model='assets/nemo/scene.gltf', collider='mesh',
                scale=(0.002), position=(0, 5, -90))
player.rotation_x = 90

animasi_player = Actor('assets/nemo/scene.gltf')
animasi_player.reparentTo(player)
animasi_player.play('swim')

hill = Entity(model='assets/hill/scene.gltf',
              scale=20, collider='box', position=(-150, 7, 270))
acropora = Entity(model='assets/acropora/scene.gltf',
                  scale=0.5, collider='box', position=(-80, -5, 115))
kraken = Entity(model='assets/kraken/scene.gltf',
                scale=0.03, collider='box', position=(-80, 25, 150))
pocillopora = Entity(model='assets/pocillopora/scene.gltf',
                     scale=0.4, collider='box', position=(20, 0, 20))
reef = Entity(model='assets/coralreef/scene.gltf',
                    scale=4, collider='box', position=(120, 0, 10))
starfish = Entity(model='assets/starfish/scene.gltf',
                  scale=2, collider='box')
coral = Entity(model='assets/coral_purple/scene.gltf',
               scale=1.8, collider='box', position=(20, 0, 10))
rumput = Entity(model='assets/rumput/scene.gltf',
                scale=0.5, collider='box', position=(20, 0, 10))
clam = Entity(model='assets/clam/scene.gltf',
              scale=4, collider='box', position=(50, 4, 60))

animasi_kraken = Actor('assets/kraken/scene.gltf')
animasi_kraken.reparentTo(kraken)


def play_kraken():
    animasi_kraken.play('Take 001')
    invoke(play_kraken, delay=15)


invoke(play_kraken, delay=1)


camera.rotation_x = 10
camera.z = player.z - 45
camera.y = player.y + 9

for _ in range(10):
    x = random.uniform(-100, 100)
    z = random.uniform(-100, 100)
    reef_clone = duplicate(reef)
    reef_clone.position = (120, 0, z)

    x = random.uniform(-100, 100)
    z = random.uniform(-100, 100)
    reef_clone2 = duplicate(reef)
    reef_clone2.position = (-120, 0, z)

    x = random.uniform(-100, 100)
    z = random.uniform(-100, 100)
    reef_clone3 = duplicate(reef)
    reef_clone3.position = (x, 0, z)

    x = random.uniform(-100, 100)
    z = random.uniform(-100, 100)
    starfish_clone = duplicate(starfish)
    starfish_clone.position = (x, 0, z)

for _ in range(40):
    x = random.uniform(-100, 100)
    z = random.uniform(-100, 100)
    pocillopora_clone = duplicate(pocillopora)
    pocillopora_clone.position = (x, 0, z)

    x = random.uniform(-100, 100)
    z = random.uniform(-100, 100)
    coral_clone = duplicate(coral)
    coral_clone.position = (x, 0, z)

    x = random.uniform(-100, 100)
    z = random.uniform(-100, 100)
    rumput_clone = duplicate(rumput)
    rumput_clone.position = (x, 0, z)


def update():
    if held_keys['a'] and player.x >= -90:
        animasi_player.play('swim')
        player.x -= 0.3
        player.rotation_y = 90

    if held_keys['d'] and player.x <= 90:
        animasi_player.play('swim')
        player.x += 0.3
        player.rotation_y = -90

    if held_keys['w'] and player.z <= 90:
        animasi_player.play('swim')
        player.z += 0.3
        player.rotation_y = 180

    if held_keys['s'] and player.z >= -108:
        animasi_player.play('swim')
        player.z -= 0.3
        player.rotation_y = 0

    if held_keys['a'] and held_keys['w']:
        animasi_player.play('swim')
        player.x -= 0.01
        player.z += 0.01
        player.rotation_y = 135

    if held_keys['d'] and held_keys['w']:
        animasi_player.play('swim')
        player.x += 0.01
        player.z += 0.01
        player.rotation_y = -135

    if held_keys['a'] and held_keys['s']:
        animasi_player.play('swim')
        player.x -= 0.01
        player.z += 0.01
        player.rotation_y = 45

    if held_keys['d'] and held_keys['s']:
        animasi_player.play('swim')
        player.x += 0.01
        player.z -= 0.01
        player.rotation_y = -45

    if held_keys['up arrow'] and player.y <= 16:
        animasi_player.play('swim')
        player.y += 0.08
        player.rotation_x = 120

    if held_keys['down arrow'] and player.y >= 1:
        animasi_player.play('swim')
        player.y -= 0.08
        player.rotation_x = 60

    elif not held_keys['up arrow'] or held_keys['down_arrow']:
        player.rotation_x = 90

    camera.x = player.x
    camera.z = player.z - 45
    camera.y = player.y + 9


app.run()
