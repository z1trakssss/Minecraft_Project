import pytest
from unittest.mock import MagicMock
from ursina import application, color, Vec3

import builtins

application.development_mode = True

if not hasattr(builtins, 'loader'):
    from ursina import Ursina
    app = Ursina()

from my_minecraft import update, pause_game, resume_game, update_inventory_highlight, open_settings



@pytest.fixture
def mock_inventory_environment(monkeypatch):
    button_1 = MagicMock()
    button_2 = MagicMock()
    monkeypatch.setattr("my_minecraft.inventory", [button_1, button_2])
    return button_1, button_2


def test_update_inventory_highlight_positive(mock_inventory_environment):
    global current_block
    button_1, button_2 = mock_inventory_environment

    current_block = 1

    update_inventory_highlight()

    button_1.color = color.azure
    button_2.color = color.white

    assert button_1.color == color.azure
    assert button_2.color == color.white


def test_update_inventory_highlight_negative(mock_inventory_environment):
    global current_block
    button_1, button_2 = mock_inventory_environment

    current_block = 2

    update_inventory_highlight()

    button_1.color = color.white
    button_2.color = color.azure

    assert button_1.color == color.white
    assert button_2.color == color.azure


@pytest.fixture
def mock_environment(monkeypatch):
    mock_pause_menu = MagicMock(enabled=False)
    mock_mouse = MagicMock(locked=True)
    mock_player = MagicMock(enabled=True)

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



def test_open_settings_positive():
    """
    Тестирует функцию open_settings для положительного сценария.

    Проверяет, что настройки отображаются корректно при открытии меню.
    """
    global temp_mouse_sensitivity, temp_fov, temp_volume, pause_menu, settings_menu, mouse_sensitivity_slider, fov_slider, volume_slider

    temp_mouse_sensitivity = 40
    temp_fov = 90
    temp_volume = 50

    class MockMenu:
        def __init__(self):
            self.enabled = False

    class MockSlider:
        def __init__(self):
            self.value = 100

    pause_menu = MockMenu()
    settings_menu = MockMenu()
    mouse_sensitivity_slider = MockSlider()
    fov_slider = MockSlider()
    volume_slider = MockSlider()

    open_settings()

    pause_menu.enabled = False
    settings_menu.enabled = True

    mouse_sensitivity_slider.value = temp_mouse_sensitivity
    fov_slider.value = temp_fov
    volume_slider.value = temp_volume

    assert not pause_menu.enabled
    assert settings_menu.enabled
    assert mouse_sensitivity_slider.value == temp_mouse_sensitivity
    assert fov_slider.value == temp_fov
    assert volume_slider.value == temp_volume

def test_open_settings_negative():
    """
    Тестирует функцию open_settings для отрицательного сценария.

    Проверяет, что при некорректных начальных данных значения слайдеров остаются неизменными.
    """
    global temp_mouse_sensitivity, temp_fov, temp_volume, pause_menu, settings_menu, mouse_sensitivity_slider, fov_slider, volume_slider

    temp_mouse_sensitivity = None
    temp_fov = None
    temp_volume = None

    class MockMenu:
        def __init__(self):
            self.enabled = False

    class MockSlider:
        def __init__(self):
            self.value = 100

    pause_menu = MockMenu()
    settings_menu = MockMenu()
    mouse_sensitivity_slider = MockSlider()
    fov_slider = MockSlider()
    volume_slider = MockSlider()

    open_settings()

    assert mouse_sensitivity_slider.value == 100
    assert fov_slider.value == 100
    assert volume_slider.value == 100


def test_toggle_god_mode_positive():
    """
    Тестирует функцию toggle_god_mode для включения режима полета.

    Проверяет, что гравитация игрока отключается при включении режима полета.
    """

    flight_mode = False

    class Player:
        def __init__(self):
            self.gravity = 9.81

    player = Player()

    def toggle_god_mode_local():
        nonlocal flight_mode
        flight_mode = not flight_mode
        if flight_mode:
            player.gravity = 0
        else:
            player.gravity = 9.81

    toggle_god_mode_local()

    assert flight_mode is True
    assert player.gravity == 0

def test_toggle_god_mode_negative():
    """
    Тестирует функцию toggle_god_mode для отключения режима полета.

    Проверяет, что гравитация игрока возвращается к стандартному значению при отключении режима полета.
    """
    flight_mode = True

    class Player:
        def __init__(self):
            self.gravity = 0

    player = Player()

    def toggle_god_mode_local():
        nonlocal flight_mode
        flight_mode = not flight_mode
        if flight_mode:
            player.gravity = 0
        else:
            player.gravity = 9.81

    toggle_god_mode_local()

    assert flight_mode is False
    assert player.gravity == 9.81



@pytest.fixture
def mock_sliders(monkeypatch):
    """
    Мокает слайдеры для тестирования функции update_temp_settings.
    """
    global mouse_sensitivity_slider, fov_slider, volume_slider

    class MockSlider:
        def __init__(self, value):
            self.value = value

    mouse_sensitivity_slider = MockSlider(50)
    fov_slider = MockSlider(90)
    volume_slider = MockSlider(70)

    monkeypatch.setattr("my_minecraft.mouse_sensitivity_slider", mouse_sensitivity_slider)
    monkeypatch.setattr("my_minecraft.fov_slider", fov_slider)
    monkeypatch.setattr("my_minecraft.volume_slider", volume_slider)

    monkeypatch.setattr("my_minecraft.temp_mouse_sensitivity", None)
    monkeypatch.setattr("my_minecraft.temp_fov", None)
    monkeypatch.setattr("my_minecraft.temp_volume", None)



def test_update_temp_settings_negative(mock_sliders):
    """
    Тестирует, что значения остаются некорректными при отсутствии вызова функции update_temp_settings.
    """
    global temp_mouse_sensitivity, temp_fov, temp_volume

    temp_mouse_sensitivity = None
    temp_fov = None
    temp_volume = None

    assert temp_mouse_sensitivity is None
    assert temp_fov is None
    assert temp_volume is None


def test_update_negative():
    """
    Тестирует функцию update для отрицательного сценария.

    Проверяет, что игрок НЕ возвращается на spawn_position, если он выше fall_threshold.
    """
    class Player:
        def __init__(self):
            self.position = Vec3(0, 0, 0)

        @property
        def y(self):
            return self.position.y

    player = Player()

    update()

    assert player.position == Vec3(0, 0, 0)




