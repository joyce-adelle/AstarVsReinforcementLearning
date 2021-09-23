class Node:
    def __init__(self, point):
        self.__parent = None
        self.__point = point
        self.__f = 0
        self.__g = 0
        self.__h = 0

    def set_parent(self, parent):
        self.__parent = parent

    def set_g(self, g):
        self.__g = g
        self.__f = self.__g + self.__h

    def set_h(self, h):
        self.__h = h
        self.__f = self.__g + self.__h

    def get_f(self):
        return self.__f

    def get_g(self):
        return self.__g

    def get_h(self):
        return self.__h

    def get_parent(self):
        return self.__parent

    def get_point(self):
        return self.__point

    def compare_f(self, f):
        return self.__f >= f

    def __eq__(self, other):
        return self.__point == other.get_point()
