from arcade.gui import *
import arcade
import os

from Speech_IO import *
import DataScraper

class ButlerGUI(arcade.Window):
    def __init__(self):
        super().__init__(500, 500, "Monkey Butler", fullscreen=False)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        None

    def on_draw(self):
        arcade.start_render()
        super().on_draw()

    def update(self, delta_time):
        if userCommand() == 'butler':
            voiceAssistant(userCommand())
        else:
            None

def main():
    GUI = ButlerGUI()
    GUI.setup()
    arcade.run()

main()