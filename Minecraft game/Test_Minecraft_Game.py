import pytest
from unittest.mock import MagicMock, patch
from ursina import *

import builtins


application.development_mode = True

if not hasattr(builtins, 'loader'):
    app = Ursina()

from Minecraft_Game import update, pause_game, update_inventory_highlight, open_settings, god_mode, input
from Minecraft_Game import flight_mode, player, mouse, pause_menu, inventory, current_block, spawn_position



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

def test_update_inventory_highlight_negative():
    inventory = [MagicMock() for _ in range(7)]
    current_block = 2

    with (patch("Minecraft_Game.inventory", inventory),
          patch("Minecraft_Game.current_block", current_block)):
        update_inventory_highlight()

    for i, button in enumerate(inventory, start=1):
        if i == current_block:
            assert button.color == color.gray
        else:
            assert button.color == color.white



def test_pause_game_positive():
    with patch('Minecraft_Game.mouse', autospec=True) as mock_mouse:
        with (patch('Minecraft_Game.pause_menu.enabled', False),
             patch('Minecraft_Game.player.enabled', True)):
            pause_game()

            assert pause_menu.enabled is True
            assert mock_mouse.locked is False
            assert player.enabled is False

def test_pause_game_negative():
    with (patch('Minecraft_Game.pause_menu', None),
         patch('Minecraft_Game.mouse', None),
         patch('Minecraft_Game.player', None)):

        try:
            pause_game()
            assert False, "pause_game должна была вызвать ошибку"
        except AttributeError:
            pass


def test_open_settings_positive():
    with (patch('Minecraft_Game.pause_menu') as mock_pause_menu,
            patch('Minecraft_Game.settings_menu') as mock_settings_menu,
            patch('Minecraft_Game.mouse_sensitivity_slider') as mock_mouse_slider,
            patch('Minecraft_Game.fov_slider') as mock_fov_slider,
            patch('Minecraft_Game.volume_slider') as mock_volume_slider,
            patch.dict('Minecraft_Game.__dict__', {
                'temp_mouse_sensitivity': 50,
                'temp_fov': 90,
                'temp_volume': 70
            })):
        open_settings()

        assert mock_pause_menu.enabled is False
        assert mock_settings_menu.enabled is True
        assert mock_mouse_slider.value == 50
        assert mock_fov_slider.value == 90
        assert mock_volume_slider.value == 70


def test_open_settings_negative():
    with (patch('Minecraft_Game.pause_menu') as mock_pause_menu,
            patch('Minecraft_Game.settings_menu') as mock_settings_menu,
            patch.dict('Minecraft_Game.__dict__', {
                'temp_mouse_sensitivity': 50,
                'temp_fov': 90,
                'temp_volume': 70
            }),
            patch('Minecraft_Game.mouse_sensitivity_slider', None),
            patch('Minecraft_Game.fov_slider', None),
            patch('Minecraft_Game.volume_slider', None)):

        try:
            open_settings()
            assert False
        except AttributeError:
            pass



def test_god_mode_positive():
    global flight_mode, player

    with patch('Minecraft_Game.player.gravity', 9.81), patch('Minecraft_Game.flight_mode', False):
        god_mode()

        assert player.gravity == 0
def test_god_mode_negative():
    global flight_mode, player

    with patch('Minecraft_Game.player.gravity', 0), patch('Minecraft_Game.flight_mode', True):
        god_mode()

        assert player.gravity == 9.81



def test_update_positive():
    with (patch('Minecraft_Game.player') as mock_player,
         patch('Minecraft_Game.spawn_position') as mock_spawn_position,
         patch('Minecraft_Game.fall_position', -25)):

        mock_player.y = -30

        update()

        assert mock_player.position == mock_spawn_position



def test_input_positive():
    global current_block

    with (patch('Minecraft_Game.quit') as mock_quit,
         patch('Minecraft_Game.resume_game') as mock_resume_game,
         patch('Minecraft_Game.god_mode') as mock_god_mode,
         patch('Minecraft_Game.mouse') as mock_mouse):

        input('o')
        mock_quit.assert_called_once()

        with (patch('Minecraft_Game.pause_menu.enabled', True),
             patch('Minecraft_Game.settings_menu.enabled', False)):
            input('escape')
            mock_resume_game.assert_called_once()

        input('g')
        mock_god_mode.assert_called_once()

        current_block = 1
        mock_mouse.hovered_entity = MagicMock()
        mock_mouse.hovered_entity.position = MagicMock()
        mock_mouse.normal = MagicMock(return_value=(0, 1, 0))
        with patch('Minecraft_Game.Grass') as mock_grass:
            input('right mouse down')
            mock_grass.assert_called_once_with(position=mock_mouse.hovered_entity.position + mock_mouse.normal)


def test_input_negative():
    global current_block

    with patch('Minecraft_Game.quit') as mock_quit, \
         patch('Minecraft_Game.pause_game') as mock_pause_game, \
         patch('Minecraft_Game.resume_game') as mock_resume_game, \
         patch('Minecraft_Game.god_mode') as mock_god_mode, \
         patch('Minecraft_Game.update_inventory_highlight') as mock_update_inventory_highlight, \
         patch('Minecraft_Game.mouse') as mock_mouse:

        input('invalid_key')
        mock_quit.assert_not_called()
        mock_pause_game.assert_not_called()
        mock_resume_game.assert_not_called()
        mock_god_mode.assert_not_called()
        mock_update_inventory_highlight.assert_not_called()

        current_block = 1
        mock_mouse.hovered_entity = None
        with patch('Minecraft_Game.Grass') as mock_grass:
            input('right mouse down')
            mock_grass.assert_not_called()
