from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import *


if __name__ == "__main__":
    app = Ursina()

class MockObject:
    def __init__(self):
        self.enabled = False
        self.locked = True

# Глобальные объекты
background_music = Audio('C418_Subwoofer_Lullaby.mp3', loop=True, autoplay=True, volume=40)

player = FirstPersonController()
player.gravity = 0.0

grass_texture = load_texture('grass_block_texture.png')

arm_texture = load_texture('for_minecraft/assets/arm_texture.png')
hand = Entity(parent=camera.ui, model='for_minecraft/assets/arm', texture=arm_texture, scale=0.2,
              rotation=Vec3(150, -10, 10), position=Vec2(0.5, -0.6))

sky_texture = load_texture('for_minecraft/textures/skybox.jpg')
sky = Entity(model='sphere', texture=sky_texture, scale=1000, double_sided=True)

player.mouse_sensitivity = Vec2(40, 40)
mouse.locked = True


class Block(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(parent=scene,
                         position=position,
                         model='block',
                         scale=0.5,
                         origin_y=0.5,
                         texture='grass_block_texture',
                         color=color.white,
                         highlight_color=color.lime
                         )


class Grass(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='grass_block_texture.png'


class Wood(Block):
    def __init__(self,position=(0,0,0)):
        super().__init__(position)
        self.texture='wood_block_texture.png'
        self.model='wood_block'


for x in range(16):
    for z in range(16):
        for y in range(3):
            Block(position=(x, -y, z))




current_block = 1


def update_inventory_highlight():
    for i, button in enumerate(inventory, start=1):
        if i == current_block:
            button.color = color.azure
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
    block_textures = ['grass_block_icon.png', 'wood_block_icon.png']
    for i, texture in enumerate(block_textures, start=1):
        button = Button(
            parent=camera.ui,
            rotate=(0, 0, 10),
            model='block',
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
temp_flight_mode = False

flight_mode = False


def update():
    global flight_mode

    if flight_mode:
        player.gravity = 0
        if held_keys['space']:
            player.position += Vec3(0, time.dt * 10, 0)
        if held_keys['left shift']:
            player.position += Vec3(0, -time.dt * 10, 0)
    else:
        flight_mode = False
        player.gravity = 9.81


def pause_game():
    pause_menu.enabled = True
    mouse.locked = False
    player.enabled = False


def resume_game():
    pause_menu.enabled = False
    mouse.locked = True
    player.enabled = True


def open_settings():
    global temp_mouse_sensitivity, temp_fov, temp_flight_mode
    pause_menu.enabled = False
    settings_menu.enabled = True
    mouse_sensitivity_slider.value = temp_mouse_sensitivity
    fov_slider.value = temp_fov
    flight_mode_checkbox.value = temp_flight_mode


def back_to_pause_menu():
    global temp_mouse_sensitivity, temp_fov, temp_flight_mode
    global flight_mode
    player.mouse_sensitivity = Vec2(temp_mouse_sensitivity, temp_mouse_sensitivity)
    camera.fov = temp_fov
    flight_mode = temp_flight_mode
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

    if key == 'o':
        exit()

    global current_block, health
    if key in ['1', '2']:
        current_block = int(key)
        print(f'Выбран блок: {current_block}')
        update_inventory_highlight()

    if key == 'left mouse down':
        hit_info = mouse.hovered_entity
        if hit_info and (pause_menu.enabled != True) and (settings_menu.enabled != True):
            destroy(hit_info)

    if key == 'right mouse down':
        if current_block == 2:
            if mouse.hovered_entity:
                hit_position = mouse.hovered_entity.position
                new_block_position = hit_position + mouse.normal
                Wood(position=new_block_position)
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

flight_mode_checkbox = CheckBox(
    text='God Mode',
    color=color.azure,
    value=True
)

back_button = Button('Назад', color=color.azure, on_click=back_to_pause_menu)

settings_menu = WindowPanel(
    title='Настройки',
    content=(
        mouse_sensitivity_slider,
        fov_slider,
        flight_mode_checkbox,
        back_button
    ),
    enabled=False,
    parent=camera.ui,
    draggable=False,
    position=(0, 0.125, 0)
)


def update_temp_settings():
    global temp_mouse_sensitivity, temp_fov, temp_show_fps, temp_flight_mode
    temp_mouse_sensitivity = mouse_sensitivity_slider.value
    temp_fov = fov_slider.value
    temp_flight_mode = flight_mode_checkbox.value


mouse_sensitivity_slider.on_value_changed = update_temp_settings
fov_slider.on_value_changed = update_temp_settings
flight_mode_checkbox.on_value_changed = update_temp_settings

if __name__ == "__main__":
    app.run()
