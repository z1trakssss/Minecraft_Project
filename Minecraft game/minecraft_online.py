from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.networking import UrsinaNetworking



app = Ursina()
server = UrsinaNetworking(server=True, password='1111')


window.title = 'Minecraft'
window.borderless = False
window.fullscreen = True
window.show_ursina_splash = True
window.exit_button.visible = False
window.fps_counter.visible = True
player = FirstPersonController()
#def update(held_keys):
#    if held_keys['left mouse']:
#punch()
def input(key):
    if key == 'escape':
        quit()

# for x in range(16):
#     for z in range(16):
#         Entity(model='cube',parent=scene ,position=Vec3(x,0,z))







app.run()