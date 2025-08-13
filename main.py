import pygame as pg
from sys import exit
from settings import Settings
from player import Player
from utils import Colors
from input import Input

class Game:
    _is_running: bool = True
    clock = pg.time.Clock()
    dt: float = clock.tick() / 1000
    
    def __init__(self):
        pg.init()
        self._event: pg.event
        self._display: pg.Surface = pg.display.set_mode((Settings.get_resolution()), vsync=Settings.get_vsyns_enabled())
        self.player = Player()
        Input.setup_actions_dict()


    def run(self):
        while self._is_running:
            self._update_time()
            self._handle_input()
            self._update_canvas()


    def _handle_input(self):
        for self._event in pg.event.get():
            if self._event.type == pg.QUIT:
                self._is_running = False
    
    
    def _update_time(self):
        fps = Settings.get_fps()
        self.dt = self.clock.tick(fps) / 1000


    def _update_canvas(self):
        self._display.fill(Colors.BLACK)
        self.player.update(self.dt, self._display)
        pg.display.flip()



if __name__ == "__main__":
    game = Game()
    game.run()
    pg.quit()
    exit()