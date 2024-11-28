from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

for x in range(16):
    for z in range(16):
        Entity(model='cube', texture="white_cube", position = Vec3(x,0,z))

player = FirstPersonController()
player.gravity = 0.0

for x_dynamic in range(16):
    for z_dynamic in range(16):
        Entity(model='block', scale=0.6, position=Vec3(x_dynamic,0,z_dynamic))


arm_texture = load_texture('for_minecraft/assets/arm_texture.png')

hand = Entity(parent=camera.ui, model = 'for_minecraft/assets/arm', texture = arm_texture, scale=0.2, rotation = Vec3(150, -10, 10), position = Vec2(0.5, -0.6))

sky_texture = load_texture('for_minecraft/textures/skybox.jpg')

sky = Entity(model='sphere', texture=sky_texture, scale=1000, double_sided=True)

def update():
    print(player.x, player.y, player.z)


normal_speed = 10

#def input(key):
#    if key == 'o':
#        quit()
#    if key == 'shift':
#        global shift_click
#        if shift_click%2==0:
#            player.speed = normal_speed + 3
#            shift_click += 1
#        else:
#           player.speed = normal_speed
#           shift_click += 1#










#Entity(model='plane',scale=(100,1,100),texture='grass',textire_scale=(100,100), collider='box')









app.run()