# coding: utf-8

class SingletonObject(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
             cls.instance = super(SingletonObject, cls).__new__(
                 cls, *args, **kwargs)
        return cls.instance


if __name__ == '__main__':

    a = SingletonObject()
    aa = SingletonObject()
    assert a is aa, u"Singleton did not worked"
