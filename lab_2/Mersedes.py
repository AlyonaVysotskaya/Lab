from Car import Car
class Mersedes(Car):
    def __init__(self, hp, color, max_speed, model, clas):
        super().__init__(hp, color, max_speed)
        self.name = "Mersedes"
        self._model = model
        self._clas = clas
    def __repr__(self):
        return f'Car (name = {self.name}, hp = {self._hp}, color = {self._color},' \
               f' max_speed = {self._max_speed}, model = {self._model}, condition = {self._clas})'