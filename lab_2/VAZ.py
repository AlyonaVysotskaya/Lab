from Car import Car
class VAZ(Car):
    def __init__(self, hp, color, max_speed, model, condition):
        super().__init__(hp, color, max_speed)
        self.name = "VAZ"
        self._model = model
        self._condition = condition
    def __repr__(self):
        return f'Car (name = {self.name}, hp = {self._hp}, color = {self._color},' \
               f' max_speed = {self._max_speed}, model = {self._model}, condition = {self._condition})'