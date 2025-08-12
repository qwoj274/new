from utils import Utils
from json import load
from pygame import key


SETTINGS_PATH: str = "settings.json"

data = load(open(SETTINGS_PATH, 'r'))

display_parameters = data["display_parameters"]
controls = data["controls"]

class Settings():
    @staticmethod
    def get_resolution():
        x = Utils.parse_int(display_parameters["WIDTH"])
        y = Utils.parse_int(display_parameters["HEIGHT"])
        return x, y

    @staticmethod
    def get_vsyns_enabled():
        return Utils.parse_int(display_parameters["VSYNC"])

    def get_fps():
        return Utils.parse_int(display_parameters["FPS"])

    @staticmethod
    def get_input_map():
        return controls


if __name__ == "__main__":
    for key in controls:
        print(controls[key])
        
        
        