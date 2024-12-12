from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import *


if __name__ == "__main__":
    app = Ursina()

class MockObject:
    def __init__(self):
        self.enabled = False
        self.locked = True

background_music = Audio('C418_Subwoofer_Lullaby.mp3', loop=True, autoplay=True, volume=40)

player = FirstPersonController()
player.collider = 'box'

arm_texture = load_texture('arm_texture.png')
hand = Entity(parent=camera.ui, model='arm', texture=arm_texture, scale=0.2,
              rotation=Vec3(150, -10, 10), position=Vec2(0.5, -0.6))

sky_texture = load_texture('skybox.jpg')
sky = Entity(model='sphere', texture=sky_texture, scale=1000, double_sided=True)

player.mouse_sensitivity = Vec2(40, 40)
mouse.locked = True


class Block(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(parent=scene,
                         position=position,
                         model='real_block',
                         scale=0.5,
                         origin_y=0.5,
                         texture='grass.jpg',
                         color=color.white,
                         highlight_color=color.lime,
                         collider='box'
                         )


class Grass(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='grass.jpg'


class Wood_block(Block):
    def __init__(self,position=(0,0,0)):
        super().__init__(position)
        self.texture='wood_block.jpg'

class Gold(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='gold_block.png'

class Diamond(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='diamond_block.png'

class Lapis(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='lapis_block.png'

class Stone(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='stone_block.jpg'

class Wood(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='wood.jpg'

for x in range(16):
    for z in range(16):
        for y in range(3):
            Block(position=(x, -y, z))


current_block = 1


def update_inventory_highlight():
    for i, button in enumerate(inventory, start=1):
        if i == current_block:
            button.color = color.gray
        else:
            button.color = color.white


hotbar_texture = 'hotbar.png'
hotbar = Entity(
    model='quad',
    texture=hotbar_texture,
    color=color.dark_gray,
    scale=(1.45, 0.8),
    position=(0, -0.15),
    parent=camera.ui
)


def create_inventory():
    inventory_buttons = []
    block_textures = ['grass.png', 'wood_block.jpg', 'diamond_block.png', 'gold_block.png', 'lapis_block.png', 'stone_block.jpg', 'wood.jpg']
    for i, texture in enumerate(block_textures, start=1):
        button = Button(
            parent=camera.ui,
            rotate=(0, 0, 10),
            model='real_block',
            texture=texture,
            scale=(0.02, 0.02),
            position=(-0.2875 + i * 0.06, -0.44),
            tooltip=Tooltip(f'Block {i}')
        )
        inventory_buttons.append(button)

    return inventory_buttons


inventory = create_inventory()
update_inventory_highlight()

camera.fov = 90

temp_mouse_sensitivity = player.mouse_sensitivity.x
temp_fov = camera.fov
temp_volume = background_music.volume*100
flight_mode = False



def toggle_god_mode():
    global flight_mode
    flight_mode = not flight_mode
    if flight_mode:
        player.gravity = 0
    else:
        player.gravity = 9.81


def update():
    if flight_mode:
        if held_keys['space']:
            player.position += Vec3(0, time.dt * 10, 0)
        if held_keys['left shift']:
            player.position += Vec3(0, -time.dt * 10, 0)


def pause_game():
    pause_menu.enabled = True
    mouse.locked = False
    player.enabled = False


def resume_game():
    pause_menu.enabled = False
    mouse.locked = True
    player.enabled = True


def open_settings():
    global temp_mouse_sensitivity, temp_fov, temp_volume
    pause_menu.enabled = False
    settings_menu.enabled = True
    mouse_sensitivity_slider.value = temp_mouse_sensitivity
    fov_slider.value = temp_fov
    volume_slider.value = temp_volume



def back_to_pause_menu():
    global temp_mouse_sensitivity, temp_fov, temp_volume
    player.mouse_sensitivity = Vec2(temp_mouse_sensitivity, temp_mouse_sensitivity)
    camera.fov = temp_fov
    background_music.volume = temp_volume/100
    settings_menu.enabled = False
    pause_menu.enabled = True


def input(key):
    if key == 'escape':
        if settings_menu.enabled:
            back_to_pause_menu()
        elif pause_menu.enabled:
            resume_game()
        else:
            pause_game()

    if key == 'g':
        toggle_god_mode()

    if key == 'o':
        exit()

    global current_block
    if key in ['1', '2', '3', '4', '5', '6', '7']:
        current_block = int(key)
        update_inventory_highlight()

    if key == 'left mouse down':
        hit_info = mouse.hovered_entity
        if hit_info and (pause_menu.enabled != True) and (settings_menu.enabled != True):
            destroy(hit_info)

    if key == 'right mouse down':
        if current_block == 7:
            if mouse.hovered_entity:
                hit_position = mouse.hovered_entity.position
                new_block_position = hit_position + mouse.normal
                Wood(position=new_block_position)
        if current_block == 6:
            if mouse.hovered_entity:
                hit_position = mouse.hovered_entity.position
                new_block_position = hit_position + mouse.normal
                Stone(position=new_block_position)
        if current_block == 5:
            if mouse.hovered_entity:
                hit_position = mouse.hovered_entity.position
                new_block_position = hit_position + mouse.normal
                Lapis(position=new_block_position)
        if current_block == 4:
            if mouse.hovered_entity:
                hit_position = mouse.hovered_entity.position
                new_block_position = hit_position + mouse.normal
                Gold(position=new_block_position)
        if current_block == 3:
            if mouse.hovered_entity:
                hit_position = mouse.hovered_entity.position
                new_block_position = hit_position + mouse.normal
                Diamond(position=new_block_position)
        if current_block == 2:
            if mouse.hovered_entity:
                hit_position = mouse.hovered_entity.position
                new_block_position = hit_position + mouse.normal
                Wood_block(position=new_block_position)
        if current_block == 1:
            if mouse.hovered_entity:
                hit_position = mouse.hovered_entity.position
                new_block_position = hit_position + mouse.normal
                Grass(position=new_block_position)


pause_menu = WindowPanel(
    title='Меню паузы',
    content=(
        Button('Продолжить игру', color=color.azure, on_click=resume_game),
        Button('Настройки', color=color.azure, on_click=open_settings)
    ),
    enabled=False,
    parent=camera.ui,
    draggable=False
)

mouse_sensitivity_slider = Slider(
    min=10,
    max=100,
    default=40,
    text='Чувствительность мыши',
    dynamic=True
)

fov_slider = Slider(
    min=60,
    max=120,
    default=90,
    text='Поле зрения',
    dynamic=True
)

volume_slider = Slider(
    min=0,
    max=100,
    default=40,
    text='Громкость Музыки',
    dynamic=True
)

back_button = Button('Назад', color=color.azure, on_click=back_to_pause_menu)

settings_menu = WindowPanel(
    title='Настройки',
    content=(
        mouse_sensitivity_slider,
        fov_slider,
        volume_slider,
        back_button
    ),
    enabled=False,
    parent=camera.ui,
    draggable=False,
    position=(0, 0.125, 0)
)


def update_temp_settings():
    global temp_mouse_sensitivity, temp_fov, temp_volume
    temp_mouse_sensitivity = mouse_sensitivity_slider.value
    temp_fov = fov_slider.value
    temp_volume = volume_slider.value


mouse_sensitivity_slider.on_value_changed = update_temp_settings
fov_slider.on_value_changed = update_temp_settings
volume_slider.on_value_changed = update_temp_settings


if __name__ == "__main__":
    app.run()
