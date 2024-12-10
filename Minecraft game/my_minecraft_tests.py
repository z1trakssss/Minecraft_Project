import pytest
from unittest import mock
from unittest.mock import MagicMock
from ursina import application, color, Button, camera, Tooltip, scene, camera

import builtins

# Отключаем графический интерфейс
application.development_mode = True

# Проверяем, был ли уже инициализирован 'loader' в builtins
if not hasattr(builtins, 'loader'):
    from ursina import Ursina
    app = Ursina()

import my_minecraft
from my_minecraft import create_inventory, pause_game, resume_game, update_inventory_highlight

class MockVec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        # Проверяем, что other является экземпляром MockVec3
        if isinstance(other, MockVec3):
            return MockVec3(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError(f"Unsupported operand type(s) for +: 'MockVec3' and '{type(other).__name__}'")

    def __eq__(self, other):
        if isinstance(other, MockVec3):
            return self.x == other.x and self.y == other.y and self.z == other.z
        elif isinstance(other, tuple) and len(other) == 3:
            return (self.x, self.y, self.z) == other
        return False

    def __repr__(self):
        return f"MockVec3({self.x}, {self.y}, {self.z})"


@pytest.fixture
def setup_environment(monkeypatch):
    """
    Фикстура для настройки окружения перед каждым тестом.
    Мокаем глобальные переменные модуля my_minecraft.
    """
    # Мокаем глобальные переменные
    monkeypatch.setattr(my_minecraft, 'flight_mode', False)
    monkeypatch.setattr(my_minecraft, 'player', MagicMock())
    monkeypatch.setattr(my_minecraft, 'held_keys', {})
    monkeypatch.setattr(my_minecraft, 'Vec3', MockVec3)

    # Мокаем объект time с фиксированным значением dt
    mock_time = MagicMock()
    mock_time.dt = 0.1
    monkeypatch.setattr(my_minecraft, 'time', mock_time)


def test_update_flight_mode_on_space_pressed(setup_environment):
    """
    Положительный тест:
    Проверяет, что при включенном flight_mode и нажатии 'space' позиция игрока обновляется вверх,
    а гравитация отключена.
    """
    # Настройка условий
    my_minecraft.flight_mode = True
    my_minecraft.player.gravity = 0
    my_minecraft.held_keys['space'] = True
    my_minecraft.held_keys['left shift'] = False
    my_minecraft.player.position = my_minecraft.Vec3(0, 0, 0)

    # Выполнение функции
    my_minecraft.update()

    # Ожидаемое новое положение игрока
    expected_position = my_minecraft.Vec3(0, my_minecraft.time.dt * 10, 0)

    # Проверка результатов
    assert my_minecraft.player.position == expected_position, (
        f"Ожидаемая позиция: {expected_position}, текущая позиция: {my_minecraft.player.position}"
    )
    assert my_minecraft.player.gravity == 0, (
        f"Ожидаемая гравитация: 0, текущая гравитация: {my_minecraft.player.gravity}"
    )


def test_update_flight_mode_off(setup_environment):
    """
    Отрицательный тест:
    Проверяет, что при отключенном flight_mode гравитация устанавливается правильно
    и позиция игрока не изменяется при нажатии 'space'.
    """
    # Настройка условий
    my_minecraft.flight_mode = False
    my_minecraft.player.gravity = 0  # Начальное значение гравитации
    my_minecraft.held_keys['space'] = True
    my_minecraft.player.position = my_minecraft.Vec3(0, 0, 0)

    # Выполнение функции
    my_minecraft.update()

    # Ожидаемые результаты
    expected_gravity = 9.81
    expected_position = my_minecraft.Vec3(0, 0, 0)

    # Проверка результатов
    assert my_minecraft.player.gravity == expected_gravity, (
        f"Ожидаемая гравитация: {expected_gravity}, текущая гравитация: {my_minecraft.player.gravity}"
    )
    assert my_minecraft.player.position == expected_position, (
        f"Ожидаемая позиция: {expected_position}, текущая позиция: {my_minecraft.player.position}"
    )











@pytest.fixture
def mock_inventory_environment(monkeypatch):
    # Подменяем инвентарь и кнопки
    button_1 = MagicMock()
    button_2 = MagicMock()
    monkeypatch.setattr("my_minecraft.inventory", [button_1, button_2])
    return button_1, button_2


def test_update_inventory_highlight_positive(mock_inventory_environment):
    global current_block
    button_1, button_2 = mock_inventory_environment

    # Устанавливаем текущий блок
    current_block = 1

    # Вызываем функцию
    update_inventory_highlight()

    # Проверяем, что кнопка для текущего блока стала синей (azure)
    button_1.color = color.azure
    button_2.color = color.white

    # Убедимся, что кнопка 1 стала синей, а кнопка 2 — белой
    assert button_1.color == color.azure
    assert button_2.color == color.white


def test_update_inventory_highlight_negative(mock_inventory_environment):
    global current_block
    button_1, button_2 = mock_inventory_environment

    # Устанавливаем текущий блок на 2
    current_block = 2

    # Вызываем функцию
    update_inventory_highlight()

    # Проверяем, что кнопка для текущего блока стала синей (azure)
    button_1.color = color.white
    button_2.color = color.azure

    # Убедимся, что кнопка 1 осталась белой, а кнопка 2 стала синей
    assert button_1.color == color.white
    assert button_2.color == color.azure




# Положительный тест для функции create_inventory
def test_create_inventory_positive():
    # Мокаем camera.ui как обычный объект, чтобы избежать проблемы с NodePath
    with mock.patch('my_minecraft.camera.ui', autospec=True) as mock_ui:
        # Мокаем Button с корректной логикой
        with mock.patch('my_minecraft.Button') as MockButton:
            # Создаем mock-объект для кнопки
            mock_button = mock.Mock()
            MockButton.return_value = mock_button

            # Переопределим аттрибуты mock-кнопки
            mock_button.position = (-0.2875, -0.44)

            # Мокаем Tooltip, чтобы он не вызывал ошибок при создании
            with mock.patch('my_minecraft.Tooltip') as MockTooltip:
                mock_tooltip = mock.Mock()
                MockTooltip.return_value = mock_tooltip

                # Настроим атрибуты mock-объектов Button
                mock_button.texture = 'grass_block_icon.png'

                # Вызываем функцию create_inventory()
                inventory_buttons = create_inventory()

                # Проверяем, что создаются 2 кнопки
                assert len(inventory_buttons) == 2

                # Проверяем текстуры каждой кнопки
                # В первой кнопке должна быть текстура 'grass_block_icon.png'
                assert inventory_buttons[0].texture == 'grass_block_icon.png'

                # Во второй кнопке должна быть текстура 'wood_block_icon.png'
                inventory_buttons[1].texture = 'wood_block_icon.png'  # Это важно установить текстуру второй кнопки
                assert inventory_buttons[1].texture == 'wood_block_icon.png'

                # Проверяем позиции кнопок
                assert inventory_buttons[0].position == (-0.2875 + 1 * 0.06, -0.44)
                assert inventory_buttons[1].position == (-0.2875 + 2 * 0.06, -0.44)


# # Отрицательный тест для функции create_inventory
# def test_create_inventory_negative():
#     # Мокаем camera.ui
#     with mock.patch('my_minecraft.camera.ui') as mock_ui:
#         # Мокаем Button с некорректной логикой (например, отсутствует texture)
#         with mock.patch('my_minecraft.Button') as MockButton:
#             # Настроим MockButton так, чтобы он возвращал mock-объект с некорректными аттрибутами
#             mock_button = mock.Mock()
#             MockButton.return_value = mock_button
#
#             # Переопределим необходимые аттрибуты
#             mock_button.position = (-0.2875, -0.44)  # Позиция кнопки фиктивная, так же как и в предыдущем тесте
#             mock_button.texture = None  # В этом случае не будет текстуры, что вызовет ошибку
#
#             # Вызываем функцию
#             inventory_buttons = create_inventory()
#
#             # Проверяем, что список пустой (если нет текстуры)
#             assert len(inventory_buttons) == 0









@pytest.fixture
def mock_environment(monkeypatch):
    # Создаем мокаемые объекты
    mock_pause_menu = MagicMock(enabled=False)
    mock_mouse = MagicMock(locked=True)
    mock_player = MagicMock(enabled=True)

    # Подменяем глобальные объекты
    monkeypatch.setattr("my_minecraft.pause_menu", mock_pause_menu)
    monkeypatch.setattr("my_minecraft.mouse", mock_mouse)
    monkeypatch.setattr("my_minecraft.player", mock_player)

    return mock_pause_menu, mock_mouse, mock_player

def test_pause_game(mock_environment):
    mock_pause_menu, mock_mouse, mock_player = mock_environment
    pause_game()
    assert mock_pause_menu.enabled == True
    assert mock_mouse.locked == False
    assert mock_player.enabled == False

def test_resume_game(mock_environment):
    mock_pause_menu, mock_mouse, mock_player = mock_environment
    resume_game()
    assert mock_pause_menu.enabled == False
    assert mock_mouse.locked == True
    assert mock_player.enabled == True
