'''
Implements Traveller pseudohex
- Assign value: p = Pseudohex(6)
- Declare without value => value = 0
    p = Pseudohex() => int(p) == 0, str(p) == '0'
- int(p) returns int representation
- str(p) returns str representation
- You can compare with either str or int
'''


class Pseudohex(object):
    '''Pseudohex'''
    def __init__(self, value=0):
        self.valid = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'
        self._set(value)

    def _set(self, value):
        '''Validate and set value'''
        if isinstance(value, str):
            if self.valid.find(value) != -1:
                self._value = self.valid.find(value)
            else:
                raise ValueError('Invalid value {}'.format(value))
        elif isinstance(value, int):
            if value < len(self.valid) and value >= 0:
                self._value = value
            else:
                raise ValueError('Invalid value {}'.format(value))
        else:
            raise TypeError(
                '%s %s should be int or str', type(value), value)

    def __int__(self):
        return self._value

    def __index__(self):
        return self.__int__()

    def __str__(self):
        return self.valid[self._value]

    def __add__(self, other):
        if isinstance(other, str):
            other_value = self.valid.index(other)
            if (self._value + other_value) < len(self.valid):
                self._set(self._value + other_value)
            else:
                self._set(len(self.valid)-1)
        elif isinstance(other, int):
            if (self._value + other) < len(self.valid):
                self._set(self._value + other)
            else:
                self._set(len(self.valid)-1)
        elif isinstance(other, Pseudohex):
            if (self._value + other._value) < len(self.valid):
                self._set(self._value + other._value)
            else:
                self._set(len(self.valid)-1)
        else:
            raise TypeError('%s %s should be int or or Pseudohex', type(other), other)
        return self

    def __sub__(self, other):
        if isinstance(other, str):
            other_value = self.valid.index(other)
            if (self._value - other_value) > 0:
                self._set(self._value + other_value)
            else:
                self._set(0)
        elif isinstance(other, int):
            if (self._value - other) > 0:
                self._set(self._value - other)
            else:
                self._set(0)
        elif isinstance(other, Pseudohex):
            if (self._value - other._value) > 0:
                self._set(self._value - other._value)
            else:
                self._set(0)
        else:
            raise TypeError('%s %s should be int or or Pseudohex', type(other), other)
        return self

    def __eq__(self, other):
        if isinstance(other, str):
            return self.valid[self._value] == other
        elif isinstance(other, int):
            return self._value == other
        elif isinstance(other, Pseudohex):
            return self._value == other._value
        else:
            raise TypeError('%s %s should be int or str or Pseudohex', type(other), other)

    def __ne__(self, other):
        if isinstance(other, str):
            return self.valid[self._value] != other
        elif isinstance(other, int):
            return self._value != other
        elif isinstance(other, Pseudohex):
            return self._value != other._value
        else:
            raise TypeError('%s %s should be int or str', type(other), other)

    def __lt__(self, other):
        if isinstance(other, str):
            return self.valid[self._value] < other
        elif isinstance(other, int):
            return self._value < other
        elif isinstance(other, Pseudohex):
            return self._value < other._value
        else:
            raise TypeError('%s %s should be int or str', type(other), other)

    def __gt__(self, other):
        if isinstance(other, str):
            return self.valid[self._value] > other
        elif isinstance(other, int):
            return self._value > other
        elif isinstance(other, Pseudohex):
            return self._value > other._value
        else:
            raise TypeError('%s %s should be int or str', type(other), other)

    def __le__(self, other):
        if isinstance(other, str):
            return self.valid[self._value] <= other
        elif isinstance(other, int):
            return self._value <= other
        elif isinstance(other, Pseudohex):
            return self._value <= other._value
        else:
            raise TypeError('%s %s should be int or str', type(other), other)

    def __ge__(self, other):
        if isinstance(other, str):
            return self.valid[self._value] >= other
        elif isinstance(other, int):
            return self._value >= other
        elif isinstance(other, Pseudohex):
            return self._value >= other._value
        else:
            raise TypeError('%s %s should be int or str', type(other), other)
