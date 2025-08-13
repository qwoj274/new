from pygame import Vector2, color

class Utils:
    @staticmethod
    def parse_int(x: object):
        if type(x) is int: return x

        if type(x) is bool: return (1 if x else 0)

        if type(x) is str:
            int_x: str = ""
            symbol: str
            for symbol in x:
                if symbol.isdigit():
                    int_x += symbol
            return (0 if int_x == "" else int(int_x))

        return 0
    
    @staticmethod
    def parse_bool(x: object):
        if type(x) is bool: return x

        if type(x) in (float, int): return (True if (x>0) else False)
                
        if type(x) is str: return len(x)>0

        return False

    @staticmethod
    def get_vector(negx: bool, posx: bool, negy: bool, posy: bool) -> Vector2:
        x = int(posx) - int(negx)
        y = int(posy) - int(negy)
        vec = Vector2(x, y)
        if not Utils.parse_bool(vec.length()):
            return Vector2(x,y)
        else:
            return Vector2.normalize(vec)
    
    @staticmethod
    def clamp(value: float, min: float, max: float):
        if min>max:
            raise ValueError("Min value must be less than max value")
        else:
            return (
            value if min<=value<=max else
            min if min>value else
            max
        )
    
    @staticmethod
    def fixed_normalize(vec: Vector2) -> Vector2:
        if vec.magnitude() == 0:
            return vec
        return Vector2.normalize(vec)


class Colors:
    WHITE = color.Color(255, 255, 255)
    BLACK = color.Color(0, 0, 0)
    RED = color.Color(255, 0, 0)
    GREEN = color.Color(0, 255, 0)
    BLUE = color.Color(0, 0, 255)


class classproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, owner):
        return self.func(owner)


if __name__ == "__main__":
    print(Utils.get_vector(False, True, True, False))