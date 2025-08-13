import pygame as pg
from abc import ABC, abstractmethod
from utils import Utils, classproperty
import settings

ACTIONS: dict = {}


class Action:
    def __init__(self, *action_keys: int):
        self.keys = list()
        for key in action_keys:
            self.add_key(key)

    @classproperty
    def EMPTY(cls):
        return cls()


    @property
    def is_pressed(self):
        return True in self.get_pressed_keys()


    def get_pressed_keys(self) -> list:
        pressed_keys = list()
        for key in self.keys:
            pressed_keys.append(pg.key.get_pressed()[key])
        return pressed_keys
        
        
    def add_key(self, key: int):
        self.keys.append(key)


    def get_key_list(self, *, named = False):
        if not named:
            return self.keys
        name_list = list()
        key: int
        for key in self.keys:
            name_list.append(pg.key.name(key))
        return name_list


    def get_keys_names(self):
        name_list = list()
        key: int
        for key in self.keys:
            name_list.append(pg.key.name(key))
        return name_list
            


class Input(ABC):
    @abstractmethod
    def __init__(self):
        self.actions = ACTIONS


    def create_action(self, name: str, key: list):
        self.actions[name] = Action(key)


    @staticmethod
    def is_action_pressed(action_name: str) -> bool:
        if action_name in ACTIONS:
            return ACTIONS[action_name].is_pressed
        else:
            return False
    
    @staticmethod
    def setup_actions_dict():
        actions_list = settings.Settings.get_input_map()
        for action_name in actions_list:
            action = Action()
            for action_key in range(len(actions_list[action_name])):
                action.add_key(pg.key.key_code(actions_list[action_name][action_key]))
            ACTIONS[action_name] = action

    @staticmethod
    def get_axis(x: tuple[2], y: tuple[2]) -> pg.Vector2:
        axis_vector = pg.Vector2(0, 0)
        axis_vector.x = x[0] - x[1]
        axis_vector.y = y[0] - y[1]
        return Utils.fixed_normalize(axis_vector)


    def get_action(self, action_name) -> Action:
        if action_name in ACTIONS:
            return ACTIONS[action_name]
        else:
            return Action.EMPTY

    
    def add_key(self, action_name: str, key: int):
        action: Action = self.actions[action_name]
        action.add_key(key)


    def get_keys_in_action(self, action_name: str, *, named: bool = False):
        if self.actions[action_name]:
            if named:
                return self.actions[action_name].get_keys_names()
            else:
                return self.actions[action_name].get_key_list()
        else:
            return list()



if __name__ == "__main__":
    Input.setup_actions_dict()
    print(Action.EMPTY.get_key_list())
    print(ACTIONS["MOVE_RIGHT"].get_key_list())