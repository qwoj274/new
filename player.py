import pygame as pg
import utils, input


class Player():
    _SPEED = 500
    _ACCELERATION = 1.5

    def __init__(self):
        self.position: pg.Vector2 = pg.Vector2(50, 50)
        self.image = pg.Surface((20, 20))
        self.image.fill(utils.Colors.WHITE)
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

        self.direction: pg.Vector2 = pg.Vector2(0, 0)
        
        self.velocity: pg.Vector2 = pg.Vector2(0, 0)


    def update(self, delta: float, source_surface: pg.surface.Surface):
        source_surface.blit(self.image, self.position)
        self._handle_input()
        self._move(delta)
        
    

    def _handle_input(self):
        self.direction = input.Input.get_axis(
            (input.Input.is_action_pressed("MOVE_RIGHT"), input.Input.is_action_pressed("MOVE_LEFT")),
            (input.Input.is_action_pressed("MOVE_DOWN"), input.Input.is_action_pressed("MOVE_UP"))
        )
    

    def _move(self, delta):
        self.velocity = self.direction * self._SPEED * delta
        acceleration_factor = self.velocity * self._ACCELERATION * input.Input.is_action_pressed("ACCELERATE")

        self.position += self.velocity + acceleration_factor


if __name__ == "__main__":
    player = Player()