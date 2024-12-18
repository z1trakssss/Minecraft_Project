import unittest

import pytest
from unittest.mock import MagicMock, patch
from ursina import application, color, Vec3
from ursina.prefabs.first_person_controller import FirstPersonController

import builtins

application.development_mode = True

if not hasattr(builtins, 'loader'):
    from ursina import Ursina
    app = Ursina()

from Minecraft_Game import god_mode, create_inventory, update_inventory_highlight, update, input
from Minecraft_Game import block_textures


class PlayerMock:
    """Заглушка для объекта игрока."""
    def __init__(self):
        self.gravity = 9.81

# Инициализация глобальных переменных для тестов
class PlayerMock:
    """Заглушка для объекта игрока."""
    def __init__(self):
        self.gravity = 9.81

# Инициализация глобальных переменных для тестов
def setup_module(module):
    global flight_mode, player
    flight_mode = False
    player = PlayerMock()

# Положительный тест для функции god_mode
def test_god_mode_positive():
    global flight_mode, player

    # Проверяем начальное состояние
    flight_mode = False
    player.gravity = 9.81

    # Вызываем функцию
    god_mode()

    # Проверяем, что режим полёта включился и гравитация отключена
    assert flight_mode is True
    assert player.gravity == 0

# Отрицательный тест для функции god_mode
def test_god_mode_negative():
    global flight_mode, player

    # Проверяем недопустимость вызова функции без объекта player
    player = None
    with pytest.raises(ValueError):
        god_mode()

if __name__ == '__main__':
    pytest.main()


# def test_create_inventory_positive():
#     inventory = create_inventory()


    # for i in range(len(block_textures)):
    #     assert inventory[i].texture == block_textures[i]

# def test_create_inventory_negative():
#     inventory = create_inventory()
#
#     # Проверяем, что текстуры кнопок не пустые
#     assert all(button.texture for button in inventory)














# def test_god_mode_positive():
#
#     flight_mode = False
#
#     god_mode()
#
#     assert player.gravity == 0
# def test_god_mode_negative():
#     global flight_mode
#     flight_mode = True
#
#     god_mode()
#
#     assert player.gravity == 9.81




# def test_create_inventory_positive2():
#     inventory_buttons = create_inventory()
#
#     assert isinstance(inventory_buttons, list)
#
# def test_create_inventory_negative2():
#     with patch('Minecraft_Game.block_textures', []):
#         inventory_buttons = create_inventory()
#
#         assert inventory_buttons == []


def test_update_inventory_highlight_positive():
    inventory = [MagicMock() for _ in range(7)]
    current_block = 1

    with (patch("Minecraft_Game.inventory", inventory),
          patch("Minecraft_Game.current_block", current_block)):
        update_inventory_highlight()

    for i, button in enumerate(inventory, start=1):
        if i == current_block:
            assert button.color == color.gray
        else:
            assert button.color == color.white



