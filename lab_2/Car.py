class Car:
    def __init__(self, hp, color, max_speed):
        self.name = "Car"
        self._hp = hp
        self._color = color
        self._max_speed = max_speed
    def __repr__(self):
        return f'Car (name = {self.name}, hp = {self._hp}, color = {self._color}, max_speed = {self._max_speed}'