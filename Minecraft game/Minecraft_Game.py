from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

if __name__ == '__main__':
    app = Ursina()

background_music = Audio('audio/C418_Subwoofer_Lullaby.mp3',
                         loop=True,
                         autoplay=True,
                         volume=40
                         )


player = FirstPersonController()
player.collider = 'box'
spawn_position = Vec3(0,7,0)
player.position = spawn_position
fall_position = -25
player.mouse_sensitivity = Vec2(40,40)
mouse.locked = True


hand = Entity(
    parent=camera.ui,
    model='objects/arm',
    texture='textures/arm_texture.png',
    scale=0.2,
    position=Vec2(0.65,-0.55),
    rotation=Vec3(150,-10,10)
)

sky = Entity(
    model='sphere',
    texture='textures/skybox.jpg',
    scale=1000,
    double_sided=True
)


class Block(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='objects/real_block',
            scale=0.5,
            texture='textures/grass.jpg',
            color=color.white,
            highlight_color=color.lime,
            collider='box'
        )



class Wood(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='textures/wood.jpg'

class Wood_block(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='textures/wood_block.jpg'

class Grass(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='textures/grass.jpg'

class Gold(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='textures/gold_block.png'

class Diamond(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='textures/diamond_block.png'

class Lapis(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='textures/lapis_block.png'

class Stone(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='textures/stone_block.jpg'


for x in range(16):
    for z in range(16):
        Stone(position=(x,0,z))




hotbar = Entity(
    model='quad',
    parent=camera.ui,
    texture='textures/hotbar.png',
    position=(0,-0.15),
    scale=(1.45,0.8),
    color=color.dark_gray
)

current_block = 1

def create_inventory():
    inventory_buttons = []
    block_textures = ['textures/grass.jpg', 'textures/wood_block.jpg',
                      'textures/diamond_block.png', 'textures/gold_block.png',
                      'textures/lapis_block.png', 'textures/stone_block.jpg',
                      'textures/wood.jpg']
    for i, texture in enumerate(block_textures, start=1):
        button = Button(
            parent=camera.ui,
            model='real_block',
            texture=texture,
            scale=(0.02, 0.02),
            position=(-0.2875 + i * 0.06, -0.44)
        )
        inventory_buttons.append(button)
    return inventory_buttons

def update_inventory_highlight():
    for i, button in enumerate(inventory, start=1):
        if i == current_block:
            button.color = color.gray
        else:
            button.color = color.white

inventory = create_inventory()
update_inventory_highlight()




def input(key):
    if key == 'o':
        quit()






if __name__ == '__main__':
    app.run()

