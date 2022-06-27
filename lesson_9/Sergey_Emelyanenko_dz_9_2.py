# Домашнеее задание, урок-9, задание-2

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width * self.vol * self.ume

class Mass(Road):
    def __init__(self, _length, _width, vol, ume):
        super().__init__(_length, _width)
        self.vol = vol
        self.ume = ume

rez = Mass(20, 5000, 25, 5)
print(rez.mass()/1000, 'тонн')