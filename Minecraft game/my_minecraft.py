from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import pydoctor


if __name__ == "__main__":
    app = Ursina()

class MockObject:
    """
    Простой класс, представляющий объект с атрибутами `enabled` и `locked`

    Атрибуты:
        enabled (bool): Определяет, включён ли объект. По умолчанию False
        locked (bool): Определяет, заблокирован ли объект. По умолчанию True
    """
    def __init__(self):
        """
        Инициализирует объект MockObject с предопределёнными значениями атрибутов

        Атрибуты:
            enabled (bool): Устанавливается в False
            locked (bool): Устанавливается в True
        """
        self.enabled = False
        self.locked = True

background_music = Audio('C418_Subwoofer_Lullaby.mp3', loop=True, autoplay=True, volume=40)

player = FirstPersonController()
player.collider = 'box'
spawn_position = Vec3(0,5,0)
player.position = spawn_position

fall_threshold = -25


arm_texture = load_texture('arm_texture.png')
hand = Entity(parent=camera.ui, model='arm', texture=arm_texture, scale=0.2,
              rotation=Vec3(150, -10, 10), position=Vec2(0.5, -0.6))

sky_texture = load_texture('skybox.jpg')
sky = Entity(model='sphere', texture=sky_texture, scale=1000, double_sided=True)

player.mouse_sensitivity = Vec2(40, 40)
mouse.locked = True


class Block(Button):
    """
    Класс для создания блока в сцене, наследуется от Button

    Аргументы:
        position (tuple, необязательно): Позиция блока в сцене, по умолчанию (0, 0, 0)

    Атрибуты:
        parent (Entity): Родительский объект, обычно это сцена
        position (tuple): Позиция блока в сцене
        model (str): Модель блока, по умолчанию 'real_block'
        scale (float): Масштаб блока, по умолчанию 0.5
        origin_y (float): Точка отсчёта по высоте, по умолчанию 0.5
        texture (str): Текстура блока, по умолчанию 'grass.jpg'
        color (Color): Цвет блока, по умолчанию белый
        highlight_color (Color): Цвет блока при наведении, по умолчанию лаймовый
        collider (str): Тип коллайдера, по умолчанию 'box'
    """
    def __init__(self, position=(0, 0, 0)):
        """
        Инициализирует объект класса Block

        Аргументы:
            position (tuple): Позиция блока в сцене, по умолчанию (0, 0, 0)
        """
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
    """
    Представляет блок травы, наследуемый от класса Block

    Атрибуты:
        texture (str): Текстура блока травы, устанавливается как 'grass.jpg'
    """
    def __init__(self, position=(0,0,0)):
        """
        Инициализирует блок травы с заданной позицией

        Аргументы:
            position (tuple): Позиция блока в игровом мире, по умолчанию (0, 0, 0)
        """
        super().__init__(position)
        self.texture='grass.jpg'

class Wood_block(Block):
    """
    Представляет блок деревянного куба, наследуемый от класса Block

    Атрибуты:
        texture (str): Текстура блока дерева, устанавливается как 'wood_block.jpg'
    """
    def __init__(self,position=(0,0,0)):
        """
        Инициализирует деревянный блок с заданной позицией

        Аргументы:
            position (tuple): Позиция блока в игровом мире, по умолчанию (0, 0, 0)
        """
        super().__init__(position)
        self.texture='wood_block.jpg'

class Gold(Block):
    """
    Представляет блок золота, наследуемый от класса Block

    Атрибуты:
        texture (str): Текстура блока золота, устанавливается как 'gold_block.png'
    """
    def __init__(self, position=(0,0,0)):
        """
        Инициализирует блок золота с заданной позицией

        Аргументы:
            position (tuple, необязательно): Позиция блока в игровом мире, по умолчанию (0, 0, 0)
        """
        super().__init__(position)
        self.texture='gold_block.png'

class Diamond(Block):
    """
    Представляет блок алмаза, наследуемый от класса Block

    Атрибуты:
        texture (str): Текстура блока алмаза, устанавливается как 'diamond_block.png'
    """
    def __init__(self, position=(0,0,0)):
        """
        Инициализирует блок алмаза с заданной позицией

        Аргументы:
            position (tuple, необязательно): Позиция блока в игровом мире, по умолчанию (0, 0, 0)
        """
        super().__init__(position)
        self.texture='diamond_block.png'

class Lapis(Block):
    """
    Представляет блок лазурита, наследуемый от класса Block

    Атрибуты:
        texture (str): Текстура блока лазурита, устанавливается как 'lapis_block.png'
    """
    def __init__(self, position=(0,0,0)):
        """
        Инициализирует блок лазурита с заданной позицией

        Аргументы:
            position (tuple, необязательно): Позиция блока в игровом мире, по умолчанию (0, 0, 0)
        """
        super().__init__(position)
        self.texture='lapis_block.png'

class Stone(Block):
    """
    Представляет блок камня, наследуемый от класса Block

    Атрибуты:
        texture (str): Текстура блока камня, устанавливается как 'stone_block.jpg'
    """
    def __init__(self, position=(0,0,0)):
        """
        Инициализирует блок камня с заданной позицией

        Аргументы:
            position (tuple, необязательно): Позиция блока в игровом мире, по умолчанию (0, 0, 0)
        """
        super().__init__(position)
        self.texture='stone_block.jpg'

class Wood(Block):
    """
    Представляет блок дерева, наследуемый от класса Block

    Атрибуты:
        texture (str): Текстура блока дерева, устанавливается как 'wood.jpg'
    """
    def __init__(self, position=(0,0,0)):
        """
        Инициализирует блок дерева с заданной позицией

        Аргументы:
            position (tuple, необязательно): Позиция блока в игровом мире, по умолчанию (0, 0, 0)
        """
        super().__init__(position)
        self.texture='wood.jpg'

for x in range(25):
    for z in range(25):
        for y in range(2):
            Block(position=(x, -y, z))



current_block = 1


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
    """
    Создает кнопки инвентаря для отображения доступных блоков

    Функция генерирует список кнопок на основе заданных текстур блоков.
    Каждая кнопка соответствует определённому блоку, отображаемому в пользовательском интерфейсе,
    и имеет всплывающую подсказку с номером блока

    Переменные:
        camera.ui (Entity): Пользовательский интерфейс камеры, к которому прикрепляются кнопки

    Возвращает:
        list[Button]: Список созданных кнопок инвентаря
    """
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
        )
        inventory_buttons.append(button)

    return inventory_buttons

def update_inventory_highlight():
    """
    Обновляет выделение текущего элемента в инвентаре

    Функция проходит по всем кнопкам инвентаря и устанавливает их цвет
    в зависимости от того, соответствует ли номер элемента текущему выбранному блоку

    Переменные:
        inventory (list[Button]): Список кнопок инвентаря, доступных для взаимодействия
        current_block (int): Номер текущего выбранного блока

    Возвращает:
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


def toggle_god_mode():
    """
    Переключает режим полёта (God Mode) для игрока

    Функция изменяет состояние глобальной переменной `flight_mode`, включая или отключая режим полёта.
    В режиме полёта отключается гравитация, позволяя игроку свободно перемещаться.
    При выключении режима гравитация возвращается к стандартному значению (9.81)

    Переменные:
        flight_mode (bool): Состояние режима полёта. Если `True`, режим включен, иначе выключен
        player.gravity (float): Гравитация для игрока. Устанавливается в 0 при включении режима или 9.81 при выключении

    Возвращает:
        None
    """
    global flight_mode
    flight_mode = not flight_mode
    if flight_mode:
        player.gravity = 0
    else:
        player.gravity = 9.81


def update():
    """
    Обновляет состояние игрока на каждом кадре

    Функция проверяет, не упал ли игрок ниже заданной высоты (`fall_threshold`).
    Если высота игрока ниже порогового значения, его позиция сбрасывается на позицию возрождения (`spawn_position`).
    Также, если включен режим полёта (`flight_mode`), игрок может двигаться вверх и вниз, удерживая определённые клавиши

    Аргументы:
        player: Игрок, чья позиция обновляется
        spawn_position (Vec3): Позиция, на которую игрок возвращается после падения
        fall_threshold (float): Высота, ниже которой игрок считается упавшим
        flight_mode (bool): Флаг, активирующий режим полёта
        held_keys (dict): Словарь текущих нажатых клавиш

    Возвращает:
        None
    """
    global spawn_position
    if player.y < fall_threshold:
        player.position = spawn_position

    if flight_mode:
        if held_keys['space']:
            player.position += Vec3(0, time.dt * 10, 0)
        if held_keys['left shift']:
            player.position += Vec3(0, -time.dt * 10, 0)


def pause_game():
    """
    Активирует меню паузы и приостанавливает управление игроком

    Функция включает отображение меню паузы, разблокирует указатель мыши
    и отключает управление игроком, чтобы обеспечить взаимодействие с интерфейсом

    Переменные:
        pause_menu.enabled (bool): Состояние меню паузы. Устанавливается в True для отображения меню
        mouse.locked (bool): Состояние блокировки указателя мыши. Устанавливается в False для разблокировки
        player.enabled (bool): Состояние игрока. Устанавливается в False, чтобы отключить управление

    Возвращает:
        None
    """
    pause_menu.enabled = True
    mouse.locked = False
    player.enabled = False


def resume_game():
    """
    Возобновляет игру после паузы

    Функция отключает отображение меню паузы, блокирует указатель мыши
    и включает управление игроком, возвращая его в активное состояние

    Переменные:
        pause_menu.enabled (bool): Состояние меню паузы. Устанавливается в False, чтобы скрыть меню
        mouse.locked (bool): Состояние блокировки указателя мыши. Устанавливается в True для блокировки указателя
        player.enabled (bool): Состояние игрока. Устанавливается в True для включения управления

    Возвращает:
        None
    """
    pause_menu.enabled = False
    mouse.locked = True
    player.enabled = True


def open_settings():
    """
    Открывает меню настроек игры

    Функция отключает меню паузы и включает меню настроек. Устанавливает значения слайдеров
    для чувствительности мыши, поля зрения (FOV) и громкости на временные значения,
    чтобы отразить текущие настройки игрока

    Переменные:
        temp_mouse_sensitivity (float): Временное значение чувствительности мыши
        temp_fov (float): Временное значение поля зрения камеры
        temp_volume (float): Временное значение громкости музыки
        pause_menu.enabled (bool): Состояние меню паузы. Устанавливается в False для отключения меню
        settings_menu.enabled (bool): Состояние меню настроек. Устанавливается в True для включения меню
        mouse_sensitivity_slider.value (float): Значение слайдера чувствительности мыши
        fov_slider.value (float): Значение слайдера поля зрения
        volume_slider.value (float): Значение слайдера громкости

    Возвращает:
        None
    """
    global temp_mouse_sensitivity, temp_fov, temp_volume
    pause_menu.enabled = False
    settings_menu.enabled = True
    mouse_sensitivity_slider.value = temp_mouse_sensitivity
    fov_slider.value = temp_fov
    volume_slider.value = temp_volume



def back_to_pause_menu():
    """
    Возвращает игрока в меню паузы из меню настроек

    Функция восстанавливает значения чувствительности мыши, поля зрения камеры и громкости музыки
    из временных настроек. Отключает меню настроек и включает меню паузы

    Переменные:
        temp_mouse_sensitivity (float): Временное значение чувствительности мыши
        temp_fov (float): Временное значение поля зрения камеры
        temp_volume (float): Временное значение громкости музыки
        player.mouse_sensitivity (Vec2): Значение чувствительности мыши для управления игроком
        camera.fov (float): Поле зрения камеры
        background_music.volume (float): Громкость фоновой музыки в диапазоне от 0 до 1
        settings_menu.enabled (bool): Состояние меню настроек. Устанавливается в False для отключения
        pause_menu.enabled (bool): Состояние меню паузы. Устанавливается в True для включения

    Возвращает:
        None
    """
    global temp_mouse_sensitivity, temp_fov, temp_volume
    player.mouse_sensitivity = Vec2(temp_mouse_sensitivity, temp_mouse_sensitivity)
    camera.fov = temp_fov
    background_music.volume = temp_volume/100
    settings_menu.enabled = False
    pause_menu.enabled = True


def input(key):
    """
    Обрабатывает ввод пользователя

    Функция выполняет действия в зависимости от нажатой клавиши, включая переключение меню,
    активацию режима полета, выбор блока, разрушение или размещение блоков в игровом мире

    Аргументы:
        key (str): Нажатая клавиша или кнопка мыши

    Переменные:
        settings_menu.enabled (bool): Состояние меню настроек. Используется для проверки активности меню
        pause_menu.enabled (bool): Состояние меню паузы. Используется для проверки активности меню
        current_block (int): Номер текущего выбранного блока. Обновляется при выборе блока
        mouse.hovered_entity (Entity): Объект, на который указывает курсор мыши, используется для разрушения или размещения блоков
        mouse.normal (Vec3): Нормаль поверхности объекта под курсором, используется для определения позиции нового блока

    Исключения:
        SystemExit: Если нажата клавиша 'o' для выхода из игры

    Возвращает:
        None
    """
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
    """
    Обновляет временные значения настроек игры

    Функция сохраняет текущие значения слайдеров чувствительности мыши, поля зрения камеры
    и громкости музыки во временные переменные. Эти значения используются для применения
    настроек при возврате из меню

    Переменные:
        temp_mouse_sensitivity (float): Временное значение чувствительности мыши
        temp_fov (float): Временное значение поля зрения камеры
        temp_volume (float): Временное значение громкости музыки
        mouse_sensitivity_slider.value (float): Текущее значение слайдера чувствительности мыши
        fov_slider.value (float): Текущее значение слайдера поля зрения
        volume_slider.value (float): Текущее значение слайдера громкости

    Возвращает:
        None
    """
    global temp_mouse_sensitivity, temp_fov, temp_volume
    temp_mouse_sensitivity = mouse_sensitivity_slider.value
    temp_fov = fov_slider.value
    temp_volume = volume_slider.value


mouse_sensitivity_slider.on_value_changed = update_temp_settings
fov_slider.on_value_changed = update_temp_settings
volume_slider.on_value_changed = update_temp_settings


if __name__ == "__main__":
    app.run()
