# coding: utf-8


def singletoned(obj):
    _cache = {}
    def instance(*args, **kwargs):
        if obj not in _cache:
            _cache[obj] = obj(*args, **kwargs)

        return _cache[obj]
    return instance


@singletoned
class A(object):
    pass


class B(object):
    pass


if __name__ == '__main__':

    a=A()
    aa=A()
    assert a is aa, u"Singleton did not worked"
