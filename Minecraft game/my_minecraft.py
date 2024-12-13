from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import pydoctor


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
    """
    Создает блок в игровой сцене.

    :ivar parent: Родительский объект, установленный в `scene`.
    :type parent: Entity
    :ivar model: Модель блока. По умолчанию 'real_block'.
    :type model: str
    :ivar scale: Масштаб блока. По умолчанию 0.5.
    :type scale: float
    :ivar origin_y: Вертикальная точка отсчета блока. По умолчанию 0.5.
    :type origin_y: float
    :ivar texture: Текстура блока. По умолчанию 'grass.jpg'.
    :type texture: str
    :ivar color: Основной цвет блока. По умолчанию белый.
    :type color: color
    :ivar highlight_color: Цвет блока при выделении. По умолчанию лаймовый.
    :type highlight_color: color
    :ivar collider: Тип коллайдера блока. По умолчанию 'box'.
    :type collider: str
    """
    def __init__(self, position=(0, 0, 0)):
        """
        Инициализирует блок с заданными параметрами.

        :param position: Позиция блока в сцене. По умолчанию (0, 0, 0).
        :type position: tuple
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
    Представляет блок травы, наследуемый от класса Block.

    :param position: Позиция блока в игровом мире. По умолчанию (0, 0, 0).
    :type position: tuple
    :ivar texture: Текстура блока травы. Устанавливается как 'grass.jpg'.
    :type texture: str
    """
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='grass.jpg'

class Wood_block(Block):
    """
    Представляет блок деревянного куба, наследуемый от класса Block.

    :param position: Позиция блока в игровом мире. По умолчанию (0, 0, 0).
    :type position: tuple
    :ivar texture: Текстура блока дерева. Устанавливается как 'wood_block.jpg'.
    :type texture: str
    """
    def __init__(self,position=(0,0,0)):
        super().__init__(position)
        self.texture='wood_block.jpg'

class Gold(Block):
    """
    Представляет блок золота, наследуемый от класса Block.

    :param position: Позиция блока в игровом мире. По умолчанию (0, 0, 0).
    :type position: tuple
    :ivar texture: Текстура блока золота. Устанавливается как 'gold_block.png'.
    :type texture: str
    """
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='gold_block.png'

class Diamond(Block):
    """
    Представляет блок алмаза, наследуемый от класса Block.

    :param position: Позиция блока в игровом мире. По умолчанию (0, 0, 0).
    :type position: tuple
    :ivar texture: Текстура блока алмаза. Устанавливается как 'diamond_block.png'.
    :type texture: str
    """
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='diamond_block.png'

class Lapis(Block):
    """
    Представляет блок лазурита, наследуемый от класса Block.

    :param position: Позиция блока в игровом мире. По умолчанию (0, 0, 0).
    :type position: tuple
    :ivar texture: Текстура блока лазурита. Устанавливается как 'lapis_block.png'.
    :type texture: str
    """
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='lapis_block.png'

class Stone(Block):
    """
    Представляет блок камня, наследуемый от класса Block.

    :param position: Позиция блока в игровом мире. По умолчанию (0, 0, 0).
    :type position: tuple
    :ivar texture: Текстура блока камня. Устанавливается как 'stone_block.jpg'.
    :type texture: str
    """
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='stone_block.jpg'

class Wood(Block):
    """
    Представляет блок дерева, наследуемый от класса Block.

    :param position: Позиция блока в игровом мире. По умолчанию (0, 0, 0).
    :type position: tuple
    :ivar texture: Текстура блока дерева. Устанавливается как 'wood.jpg'.
    :type texture: str
    """
    def __init__(self, position=(0,0,0)):
        super().__init__(position)
        self.texture='wood.jpg'

for x in range(27):
    for z in range(27):
        for y in range(1):
            Block(position=(x, -y, z))


current_block = 1


def update_inventory_highlight():
    """
    Обновляет выделение текущего элемента в инвентаре.

    Функция проходит по всем кнопкам инвентаря и изменяет их цвет в зависимости
    от того, соответствует ли номер элемента текущему выбранному блоку.

    :ivar inventory: Список кнопок инвентаря, доступных для взаимодействия.
    :type inventory: list[Button]
    :ivar current_block: Номер текущего выбранного блока.
    :type current_block: int
    :return: None
    """
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
    """
    Создает кнопки инвентаря для отображения доступных блоков.

    Функция генерирует список кнопок на основе заданных текстур блоков.
    Каждая кнопка представляет определенный блок, отображаемый в пользовательском интерфейсе,
    и имеет всплывающую подсказку с указанием номера блока.

    :ivar camera.ui: Пользовательский интерфейс камеры, к которому прикрепляются кнопки.
    :type camera.ui: Entity
    :return: Список созданных кнопок инвентаря.
    :rtype: list[Button]
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
            tooltip=Tooltip(f'Block {i}')
        )
        inventory_buttons.append(button)

    return inventory_buttons


inventory = create_inventory()
update_inventory_highlight()

camera.fov = 90


temp_mouse_sensitivity = player.mouse_sensitivity.x
temp_fov = camera.fov
#temp_volume = background_music.volume*100
flight_mode = False



def toggle_god_mode():
    """
    Переключает режим полета (God Mode) для игрока.

    Функция изменяет состояние переменной `flight_mode`, включая или отключая режим полета.
    В режиме полета отключается гравитация, позволяя игроку свободно перемещаться,
    в противном случае гравитация возвращается к стандартному значению.

    :ivar flight_mode: Состояние режима полета. Если `True`, режим включен, иначе выключен.
    :type flight_mode: bool
    :ivar player.gravity: Параметр гравитации для игрока. Устанавливается в 0 при включении режима или 9.81 при выключении.
    :type player.gravity: float
    :return: None
    """
    global flight_mode
    flight_mode = not flight_mode
    if flight_mode:
        player.gravity = 0
    else:
        player.gravity = 9.81


def update():
    """
    Обновляет состояние игрока в режиме полета.

    Функция проверяет, активирован ли режим полета (`flight_mode`), и обрабатывает управление игроком.
    При удерживании клавиши `space` игрок поднимается вверх, а при удерживании `left shift` опускается вниз.
    Скорость перемещения зависит от времени, прошедшего с последнего кадра (`time.dt`).

    :ivar flight_mode: Состояние режима полета. Если `True`, управление высотой игрока активно.
    :type flight_mode: bool
    :ivar held_keys: Словарь текущих нажатых клавиш.
    :type held_keys: dict
    :ivar player.position: Позиция игрока в игровом пространстве.
    :type player.position: Vec3
    :return: None
    """
    if flight_mode:
        if held_keys['space']:
            player.position += Vec3(0, time.dt * 10, 0)
        if held_keys['left shift']:
            player.position += Vec3(0, -time.dt * 10, 0)


def pause_game():
    """
    Активирует меню паузы и приостанавливает управление игроком.

    Функция включает отображение меню паузы, разблокирует указатель мыши
    и отключает управление игроком, чтобы обеспечить корректное взаимодействие с интерфейсом.

    :ivar pause_menu.enabled: Состояние меню паузы. Устанавливается в True для отображения меню.
    :type pause_menu.enabled: bool
    :ivar mouse.locked: Состояние блокировки указателя мыши. Устанавливается в False, чтобы разблокировать указатель.
    :type mouse.locked: bool
    :ivar player.enabled: Состояние игрока. Устанавливается в False, чтобы отключить управление.
    :type player.enabled: bool
    :return: None
    """
    pause_menu.enabled = True
    mouse.locked = False
    player.enabled = False


def resume_game():
    """
    Возобновляет игру после паузы.

    Функция отключает отображение меню паузы, блокирует указатель мыши
    и включает управление игроком, возвращая его в активное состояние.

    :ivar pause_menu.enabled: Состояние меню паузы. Устанавливается в False, чтобы скрыть меню.
    :type pause_menu.enabled: bool
    :ivar mouse.locked: Состояние блокировки указателя мыши. Устанавливается в True, чтобы заблокировать указатель.
    :type mouse.locked: bool
    :ivar player.enabled: Состояние игрока. Устанавливается в True, чтобы включить управление.
    :type player.enabled: bool
    :return: None
    """
    pause_menu.enabled = False
    mouse.locked = True
    player.enabled = True


def open_settings():
    """
    Открывает меню настроек игры.

    Функция отключает меню паузы и включает меню настроек. Значения слайдеров для чувствительности мыши,
    поля зрения (FOV) и громкости устанавливаются на временные значения, чтобы отразить текущие настройки игрока.

    :ivar temp_mouse_sensitivity: Временное значение чувствительности мыши.
    :type temp_mouse_sensitivity: float
    :ivar temp_fov: Временное значение поля зрения камеры.
    :type temp_fov: float
    :ivar temp_volume: Временное значение громкости музыки.
    :type temp_volume: float
    :ivar pause_menu.enabled: Состояние меню паузы. Устанавливается в False, чтобы отключить меню.
    :type pause_menu.enabled: bool
    :ivar settings_menu.enabled: Состояние меню настроек. Устанавливается в True, чтобы включить меню.
    :type settings_menu.enabled: bool
    :ivar mouse_sensitivity_slider.value: Текущее значение слайдера чувствительности мыши.
    :type mouse_sensitivity_slider.value: float
    :ivar fov_slider.value: Текущее значение слайдера поля зрения.
    :type fov_slider.value: float
    :ivar volume_slider.value: Текущее значение слайдера громкости.
    :type volume_slider.value: float
    :return: None
    """
    global temp_mouse_sensitivity, temp_fov, temp_volume
    pause_menu.enabled = False
    settings_menu.enabled = True
    mouse_sensitivity_slider.value = temp_mouse_sensitivity
    fov_slider.value = temp_fov
    volume_slider.value = temp_volume



def back_to_pause_menu():
    """
    Возвращает игрока в меню паузы из меню настроек.

    Функция восстанавливает значения чувствительности мыши, поля зрения камеры и громкости музыки
    из временных настроек. Отключает меню настроек и включает меню паузы.

    :ivar temp_mouse_sensitivity: Временное значение чувствительности мыши.
    :type temp_mouse_sensitivity: float
    :ivar temp_fov: Временное значение поля зрения камеры.
    :type temp_fov: float
    :ivar temp_volume: Временное значение громкости музыки.
    :type temp_volume: float
    :ivar player.mouse_sensitivity: Значение чувствительности мыши для управления игроком.
    :type player.mouse_sensitivity: Vec2
    :ivar camera.fov: Поле зрения камеры.
    :type camera.fov: float
    :ivar background_music.volume: Громкость фоновой музыки. Приводится к диапазону 0-1.
    :type background_music.volume: float
    :ivar settings_menu.enabled: Состояние меню настроек. Устанавливается в False, чтобы отключить его.
    :type settings_menu.enabled: bool
    :ivar pause_menu.enabled: Состояние меню паузы. Устанавливается в True, чтобы включить его.
    :type pause_menu.enabled: bool
    :return: None
    """
    global temp_mouse_sensitivity, temp_fov, temp_volume
    player.mouse_sensitivity = Vec2(temp_mouse_sensitivity, temp_mouse_sensitivity)
    camera.fov = temp_fov
    background_music.volume = temp_volume/100
    settings_menu.enabled = False
    pause_menu.enabled = True


def input(key):
    """
    Обрабатывает ввод пользователя.

    Функция выполняет действия в зависимости от нажатой клавиши, включая переключение меню,
    активацию режима полета, выбор блока, разрушение или размещение блоков в игровом мире.

    :param key: Нажатая клавиша или кнопка мыши.
    :type key: str

    :ivar settings_menu.enabled: Состояние меню настроек. Используется для проверки активности меню.
    :type settings_menu.enabled: bool
    :ivar pause_menu.enabled: Состояние меню паузы. Используется для проверки активности меню.
    :type pause_menu.enabled: bool
    :ivar current_block: Номер текущего выбранного блока. Обновляется при выборе блока.
    :type current_block: int
    :ivar mouse.hovered_entity: Объект, на который указывает курсор мыши. Используется для разрушения или размещения блоков.
    :type mouse.hovered_entity: Entity
    :ivar mouse.normal: Нормаль поверхности объекта под курсором. Используется для определения позиции нового блока.
    :type mouse.normal: Vec3

    :raises SystemExit: Если нажата клавиша 'o' для выхода из игры.
    :return: None
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
    Обновляет временные значения настроек игры.

    Функция сохраняет текущие значения слайдеров чувствительности мыши, поля зрения камеры
    и громкости музыки во временные переменные. Эти значения используются для применения
    настроек при возврате из меню.

    :ivar temp_mouse_sensitivity: Временное значение чувствительности мыши.
    :type temp_mouse_sensitivity: float
    :ivar temp_fov: Временное значение поля зрения камеры.
    :type temp_fov: float
    :ivar temp_volume: Временное значение громкости музыки.
    :type temp_volume: float
    :ivar mouse_sensitivity_slider.value: Текущее значение слайдера чувствительности мыши.
    :type mouse_sensitivity_slider.value: float
    :ivar fov_slider.value: Текущее значение слайдера поля зрения.
    :type fov_slider.value: float
    :ivar volume_slider.value: Текущее значение слайдера громкости.
    :type volume_slider.value: float
    :return: None
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
