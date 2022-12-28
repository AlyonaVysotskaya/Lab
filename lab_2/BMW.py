from Car import Car
class BMW(Car):
    def __init__(self, hp, color, max_speed, model, year_release):
        super().__init__(hp, color, max_speed)
        self.name = "BMW"
        self._model = model
        self._year_realise = year_release
    def __repr__(self):
        return f'Car (name = {self.name}, hp = {self._hp}, color = {self._color},' \
               f' max_speed = {self._max_speed}, model = {self._model}, condition = {self._year_realise})'