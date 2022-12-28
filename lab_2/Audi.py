from Car import Car
class Audi(Car):
    def __init__(self, hp, color, max_speed, model, wheel_radius):
        super().__init__(hp, color, max_speed)
        self.name = "Audi"
        self._model = model
        self._wheel_radius = wheel_radius
    def __repr__(self):
        return f'Car (name = {self.name}, hp = {self._hp}, color = {self._color},' \
               f' max_speed = {self._max_speed}, model = {self._model}, condition = {self._wheel_radius})'