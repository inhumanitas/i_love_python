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


a=A()
aa=A()
aaa=A()
print a, aa, aaa

b=B()
bb=B()
print b, bb
