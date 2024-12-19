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
player.gravity = 9.81
player.collider = 'box'
spawn_position = Vec3(0,10,0)
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
    """Представляет блок в 3D-сцене.

    Класс создаёт интерактивный блок с заданной позицией, текстурой, цветом и другими параметрами.
    Наследует свойства и методы от класса `Button`.

    Attributes:
        position (tuple): Координаты блока в формате (x, y, z). По умолчанию (0, 0, 0).
        parent (Entity): Родительский объект (обычно сцена).
        model (str): Путь к 3D-модели блока. По умолчанию 'objects/real_block'.
        scale (float): Размер блока. По умолчанию 0.5.
        texture (str): Текстура блока. По умолчанию 'textures/grass.jpg'.
        color (color): Цвет блока. По умолчанию белый (color.white).
        highlight_color (color): Цвет подсветки блока при наведении. По умолчанию лаймовый (color.lime).
        collider (str): Тип коллайдера для блока. По умолчанию 'box'.
    """

    def __init__(self, position=(0, 0, 0)):
        """Инициализирует объект Block с заданной позицией и стандартными параметрами.

        Args:
            position (tuple, optional): Координаты блока в формате (x, y, z). По умолчанию (0, 0, 0).
        """
        super().__init__(
            parent=scene,
            position=position,
            model='objects/real_block.obj',
            scale=0.5,
            texture='textures/grass.jpg',
            color=color.white,
            highlight_color=color.lime,
            collider='box'
        )




class Wood(Block):
    """Представляет деревянный блок в 3D-сцене.

    Наследует свойства и методы от класса `Block`, устанавливая текстуру деревянного блока.

    Attributes:
        texture (str): Текстура блока. Всегда 'textures/wood.jpg'.
    """

    def __init__(self, position=(0, 0, 0)):
        """Инициализирует деревянный блок с заданной позицией.

        Args:
            position (tuple, optional): Координаты блока в формате (x, y, z). По умолчанию (0, 0, 0).
        """
        super().__init__(position)
        self.texture = 'textures/wood.jpg'


class Wood_block(Block):
    """Представляет блок из древесины в 3D-сцене.

    Наследует свойства и методы от класса `Block`, устанавливая текстуру древесного блока.

    Attributes:
        texture (str): Текстура блока. Всегда 'textures/wood_block.jpg'.
    """

    def __init__(self, position=(0, 0, 0)):
        """Инициализирует блок из древесины с заданной позицией.

        Args:
            position (tuple, optional): Координаты блока в формате (x, y, z). По умолчанию (0, 0, 0).
        """
        super().__init__(position)
        self.texture = 'textures/wood_block.jpg'


class Grass(Block):
    """Представляет блок с текстурой травы в 3D-сцене.

    Наследует свойства и методы от класса `Block`, устанавливая текстуру травы.

    Attributes:
        texture (str): Текстура блока. Всегда 'textures/grass.jpg'.
    """

    def __init__(self, position=(0, 0, 0)):
        """Инициализирует блок с текстурой травы с заданной позицией.

        Args:
            position (tuple, optional): Координаты блока в формате (x, y, z). По умолчанию (0, 0, 0).
        """
        super().__init__(position)
        self.texture = 'textures/grass.jpg'


class Gold(Block):
    """Представляет блок с текстурой золота в 3D-сцене.

    Наследует свойства и методы от класса `Block`, устанавливая текстуру золота.

    Attributes:
        texture (str): Текстура блока. Всегда 'textures/gold_block.png'.
    """

    def __init__(self, position=(0, 0, 0)):
        """Инициализирует блок с текстурой золота с заданной позицией.

        Args:
            position (tuple, optional): Координаты блока в формате (x, y, z). По умолчанию (0, 0, 0).
        """
        super().__init__(position)
        self.texture = 'textures/gold_block.png'


class Diamond(Block):
    """Представляет блок с текстурой алмаза в 3D-сцене.

    Наследует свойства и методы от класса `Block`, устанавливая текстуру алмаза.

    Attributes:
        texture (str): Текстура блока. Всегда 'textures/diamond_block.png'.
    """

    def __init__(self, position=(0, 0, 0)):
        """Инициализирует блок с текстурой алмаза с заданной позицией.

        Args:
            position (tuple, optional): Координаты блока в формате (x, y, z). По умолчанию (0, 0, 0).
        """
        super().__init__(position)
        self.texture = 'textures/diamond_block.png'


class Lapis(Block):
    """Представляет блок с текстурой лазурита в 3D-сцене.

    Наследует свойства и методы от класса `Block`, устанавливая текстуру лазурита.

    Attributes:
        texture (str): Текстура блока. Всегда 'textures/lapis_block.png'.
    """

    def __init__(self, position=(0, 0, 0)):
        """Инициализирует блок с текстурой лазурита с заданной позицией.

        Args:
            position (tuple, optional): Координаты блока в формате (x, y, z). По умолчанию (0, 0, 0).
        """
        super().__init__(position)
        self.texture = 'textures/lapis_block.png'


class Stone(Block):
    """Представляет блок с текстурой камня в 3D-сцене.

    Наследует свойства и методы от класса `Block`, устанавливая текстуру камня.

    Attributes:
        texture (str): Текстура блока. Всегда 'textures/stone_block.jpg'.
    """

    def __init__(self, position=(0, 0, 0)):
        """Инициализирует блок с текстурой камня с заданной позицией.

        Args:
            position (tuple, optional): Координаты блока в формате (x, y, z). По умолчанию (0, 0, 0).
        """
        super().__init__(position)
        self.texture = 'textures/stone_block.jpg'


for x in range(16):
    for z in range(16):
        Block(position=(x,0,z))




hotbar = Entity(
    model='quad',
    parent=camera.ui,
    texture='textures/hotbar.png',
    position=(0,-0.15),
    scale=(1.45,0.8),
    color=color.dark_gray
)

current_block = 1

block_textures = ['textures/grass.jpg', 'textures/wood_block.jpg',
                      'textures/diamond_block.png', 'textures/gold_block.png',
                      'textures/lapis_block.png', 'textures/stone_block.jpg',
                      'textures/wood.jpg']
def create_inventory():
    """Создаёт элементы инвентаря с кнопками для каждого блока.

    Функция генерирует список кнопок инвентаря, каждая из которых отображает
    текстуру соответствующего блока. Кнопки располагаются на экране
    пользовательского интерфейса в заданных позициях.

    Args:
        None

    Returns:
        list: Список объектов `Button`, представляющих элементы инвентаря.

    Raises:
        None
    """
    inventory_buttons = []
    for i, texture in enumerate(block_textures, start=1):
        button = Button(
            parent=camera.ui,
            model='objects/real_block.obj',
            texture=texture,
            scale=(0.02, 0.02),
            position=(-0.2875 + i * 0.06, -0.44)
        )
        inventory_buttons.append(button)
    return inventory_buttons

def update_inventory_highlight():
    """Обновляет подсветку текущего выбранного блока в инвентаре.

    Функция проверяет каждый элемент в инвентаре и подсвечивает текущий выбранный
    блок, изменяя его цвет на серый (`color.gray`). Все остальные блоки сбрасываются
    в белый цвет (`color.white`).

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    for i, button in enumerate(inventory, start=1):
        if i == current_block:
            button.color = color.gray
        else:
            button.color = color.white

inventory = create_inventory()
update_inventory_highlight()


camera.fov = 90
temp_mouse_sensitivity = player.mouse_sensitivity.x
temp_fov = camera.fov
flight_mode = False

def god_mode():
    """Переключает режим полёта для игрока.

    Если режим полёта (`flight_mode`) активируется, гравитация для игрока отключается
    (`player.gravity` устанавливается в 0). Если режим полёта отключается,
    гравитация возвращается в исходное состояние.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    global flight_mode
    flight_mode = not flight_mode
    if flight_mode:
        player.gravity = 0
    else:
        player.gravity = 9.81



def update():
    """Обновляет состояние игрока и его положение в игре.

    Если координата `y` игрока становится меньше заданной высоты (`fall_position`),
    игрок перемещается на точку возрождения (`spawn_position`).
    Если активирован режим полёта (`flight_mode`), игрок может двигаться вверх
    при нажатии пробела или вниз при нажатии левого Shift.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    global spawn_position
    if player.y < fall_position:
        player.position = spawn_position

    if flight_mode:
        if held_keys['space']:
            player.position += Vec3(0, time.dt * 10, 0)
        if held_keys['left shift']:
            player.position += Vec3(0, -time.dt * 10, 0)

def pause_game():
    """Приостанавливает игру и активирует меню паузы.

    Функция включает меню паузы, разблокирует мышь для взаимодействия с интерфейсом
    и отключает управление игроком, чтобы предотвратить любые действия в игре во время паузы.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    pause_menu.enabled = True
    mouse.locked = False
    player.enabled = False

def resume_game():
    """Возобновляет игру после паузы.

    Функция отключает меню паузы, блокирует указатель мыши и включает управление игроком.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    pause_menu.enabled = False
    mouse.locked = True
    player.enabled = True


def open_settings():
    """Открывает меню настроек и инициализирует временные параметры.

    Функция отключает меню паузы, включает меню настроек и устанавливает текущие
    значения ползунков (чувствительность мыши, угол обзора и громкость) на основе
    временных параметров.

    Global Variables:
        temp_mouse_sensitivity (float): Временное значение чувствительности мыши.
        temp_fov (float): Временное значение угла обзора (Field of View).
        temp_volume (float): Временное значение уровня громкости.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    global temp_mouse_sensitivity, temp_fov, temp_volume
    pause_menu.enabled = False
    settings_menu.enabled = True
    mouse_sensitivity_slider.value = temp_mouse_sensitivity
    fov_slider.value = temp_fov
    volume_slider.value = temp_volume



def back_to_pause_menu():
    """Возвращает пользователя из меню настроек в меню паузы.

    Функция применяет временные настройки (чувствительность мыши, угол обзора, громкость),
    закрывает меню настроек и включает меню паузы.

    Global Variables:
        temp_mouse_sensitivity (float): Временное значение чувствительности мыши.
        temp_fov (float): Временное значение угла обзора (Field of View).
        temp_volume (float): Временное значение уровня громкости.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    global temp_mouse_sensitivity, temp_fov, temp_volume
    player.mouse_sensitivity = Vec2(temp_mouse_sensitivity, temp_mouse_sensitivity)
    camera.fov = temp_fov
    background_music.volume = temp_volume / 100
    settings_menu.enabled = False
    pause_menu.enabled = True


def input(key):
    """Обрабатывает действия пользователя в зависимости от нажатой клавиши.

    Функция выполняет различные действия, такие как выход из игры, управление паузой,
    переключение режима "бога", смена текущего блока в инвентаре, разрушение блоков
    и создание новых блоков.

    Global Variables:
        current_block (int): Текущий выбранный блок из инвентаря.

    Args:
        key (str): Клавиша, нажатая пользователем.

    Returns:
        None

    Raises:
        None
    """
    global current_block

    if key == 'o':
        quit()

    if key == 'escape':
        if settings_menu.enabled:
            back_to_pause_menu()
        elif pause_menu.enabled:
            resume_game()
        else:
            pause_game()

    if key == 'g':
        god_mode()

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
        Button(text='Продолжить игру',
               color=color.azure,
               on_click=resume_game),
        Button(text='Настройки',
               color=color.azure,
               on_click=open_settings)
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

back_button = Button(
    text='Назад',
    color=color.azure,
    on_click=back_to_pause_menu
)

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
    """Обновляет временные настройки пользователя.

    Функция сохраняет текущие значения ползунков (чувствительность мыши, угол обзора и громкость)
    в соответствующие временные переменные.

    Global Variables:
        temp_mouse_sensitivity (float): Временное значение чувствительности мыши, полученное из ползунка.
        temp_fov (float): Временное значение угла обзора (Field of View), полученное из ползунка.
        temp_volume (float): Временное значение уровня громкости, полученное из ползунка.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    global temp_mouse_sensitivity, temp_fov, temp_volume
    temp_mouse_sensitivity = mouse_sensitivity_slider.value
    temp_fov = fov_slider.value
    temp_volume = volume_slider.value

mouse_sensitivity_slider.on_value_changed = update_temp_settings
fov_slider.on_value_changed = update_temp_settings
volume_slider.on_value_changed = update_temp_settings

if __name__ == '__main__':
    app.run()

