from abc import ABC, abstractmethod

class Organism(ABC):
    def __init__(self):
        self._age = 0
        self._power = 0
        self._initiative = 0
        self._sign = ''
        self._name = ''
        self._x = 0
        self._y = 0
        self._x_priv = 0
        self._y_priv = 0
        self._world = None

    @property
    def age(self):
        return self._age

    @property
    def power(self):
        return self._power

    @property
    def initiative(self):
        return self._initiative

    @property
    def sign(self):
        return self._sign

    @property
    def name(self):
        return self._name

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def x_priv(self):
        return self._x_priv

    @property
    def y_priv(self):
        return self._y_priv

    @property
    def world(self):
        return self._world

    @age.setter
    def age(self, value):
        self._age = value

    @power.setter
    def power(self, value):
        self._power = value

    @initiative.setter
    def initiative(self, value):
        self._initiative = value

    @sign.setter
    def sign(self, value):
        self._sign = value

    @name.setter
    def name(self, value):
        self._name = value

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @x_priv.setter
    def x_priv(self, value):
        self._x_priv = value

    @y_priv.setter
    def y_priv(self, value):
        self._y_priv = value

    @world.setter
    def world(self, value):
        self._world = value

    def power_increase(self, p):
        self._power += p

    def tarcze_alzura(self, attacker):
        return False

    def did_deflected_attack(self, attacker):
        return False

    @abstractmethod
    def action(self, range):
        pass

    @abstractmethod
    def collision(self, victim, x, y):
        pass
