from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Создаем землю
ground = Entity(
    model='plane',
    scale=(100, 1, 100),
    texture='grass',
    texture_scale=(100, 100),
    collider='box'
)

# Добавляем несколько объектов
for z in range(8):
    for x in range(8):
        voxel = Entity(
            model='cube',
            color=color.hsv(0, 0, random.uniform(0.9, 1)),
            texture='white_cube',
            position=(x, random.uniform(0, 2), z),
            collider='box'
        )

# Создаем игрока
player = FirstPersonController()
player.mouse_sensitivity = Vec2(40, 40)
mouse.locked = True

# Устанавливаем поле зрения
camera.fov = 90

# Создаем счетчик FPS
fps_counter = Text(
    text='',
    position=(-0.85, 0.45),
    origin=(0, 0),
    scale=2,
    enabled=False
)
fps_counter.parent = camera.ui

# Переменные для настроек
temp_mouse_sensitivity = player.mouse_sensitivity.x
temp_fov = camera.fov
temp_show_fps = False
temp_flight_mode = False

# Текущие настройки игры
show_fps = False
flight_mode = False

# Функция обновления
def update():
    global show_fps, flight_mode
    if show_fps:
        fps_counter.enabled = True
        fps_counter.text = f'FPS: {int(1 / time.dt)}'
    else:
        fps_counter.enabled = False

    if flight_mode:
        # Отключаем гравитацию
        player.gravity = 0
        # Управление полетом
        if held_keys['space']:
            player.position += Vec3(0, time.dt * 5, 0)
        if held_keys['left shift']:
            player.position += Vec3(0, -time.dt * 5, 0)
    else:
        player.gravity = 9.81

# Функции паузы
def pause_game():
    pause_menu.enabled = True
    mouse.locked = False
    player.enabled = False

def resume_game():
    pause_menu.enabled = False
    mouse.locked = True
    player.enabled = True

def open_settings():
    global temp_mouse_sensitivity, temp_fov, temp_show_fps, temp_flight_mode
    pause_menu.enabled = False
    settings_menu.enabled = True
    # Устанавливаем текущие значения в настройках
    mouse_sensitivity_slider.value = temp_mouse_sensitivity
    fov_slider.value = temp_fov
    show_fps_checkbox.value = temp_show_fps
    flight_mode_checkbox.value = temp_flight_mode

def back_to_pause_menu():
    global temp_mouse_sensitivity, temp_fov, temp_show_fps, temp_flight_mode
    global show_fps, flight_mode
    # Применяем настройки
    player.mouse_sensitivity = Vec2(temp_mouse_sensitivity, temp_mouse_sensitivity)
    camera.fov = temp_fov
    show_fps = temp_show_fps
    flight_mode = temp_flight_mode
    settings_menu.enabled = False
    pause_menu.enabled = True

# Обработка нажатий клавиш
def input(key):
    if key == 'escape':
        if settings_menu.enabled:
            back_to_pause_menu()
        elif pause_menu.enabled:
            resume_game()
        else:
            pause_game()

# Меню паузы
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

# Элементы меню настроек
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

show_fps_checkbox = CheckBox(
    text='Показывать FPS',
    color=color.azure,
    value=True
)

flight_mode_checkbox = CheckBox(
    text='Режим полета',
    color=color.azure,
    value=True
)

back_button = Button('Назад', color=color.azure, on_click=back_to_pause_menu)

# Объединяем элементы в меню настроек
settings_menu = WindowPanel(
    title='Настройки',
    content=(
        mouse_sensitivity_slider,
        fov_slider,
        show_fps_checkbox,
        flight_mode_checkbox,
        back_button
    ),
    enabled=False,
    parent=camera.ui,
    draggable=False
)

# Обновление временных настроек
def update_temp_settings():
    global temp_mouse_sensitivity, temp_fov, temp_show_fps, temp_flight_mode
    temp_mouse_sensitivity = mouse_sensitivity_slider.value
    temp_fov = fov_slider.value
    temp_show_fps = show_fps_checkbox.value
    temp_flight_mode = flight_mode_checkbox.value

# Привязываем обновление настроек
mouse_sensitivity_slider.on_value_changed = update_temp_settings
fov_slider.on_value_changed = update_temp_settings
show_fps_checkbox.on_value_changed = update_temp_settings
flight_mode_checkbox.on_value_changed = update_temp_settings

# Настраиваем освещение и небо
DirectionalLight(y=3, rotation=(45, -45, 45))
Sky()
















app.run()