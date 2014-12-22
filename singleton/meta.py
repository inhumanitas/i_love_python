# coding: utf-8

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = type.__call__(cls)
        return cls._instances[cls]

class Singleton(object):
    __metaclass__ = SingletonMeta


if __name__ == '__main__':

    a = Singleton()
    aa = Singleton()
    assert a is aa, u"Singleton did not worked"
