# encoding: utf-8
u"""
Есть два списка разной длины.
В первом содержатся ключи, а во втором значения.
Напишите функцию, которая создаёт из этих ключей
и значений словарь.
Если ключу не хватило значения, в словаре должно
быть значение None.
Значения, которым не хватило ключей, нужно игнорировать.
"""

try:
    # Python 2
    from itertools import izip_longest as zip_longest
except ImportError:
    # Python 3
    from itertools import zip_longest

class DictValidationError(Exception):
    pass


def check_dict(d, keys, values):
    """Validate dict by pre defined key\value"""
    assert isinstance(d, dict), "Type error"
    if (filter(bool, d.values()) != values or
            filter(bool, d.keys()) != keys):

        raise DictValidationError("You done it wrong")


class DictCreator(object):
    """Base for dict creators"""
    def __init__(self, keys, values):
        msg = "Wrong input parameter"
        assert isinstance(keys, list), msg
        assert isinstance(values, list), msg
        self.keys = keys
        self.values = values

    def __call__(self):
        raise NotImplementedError

class MapDictCreator(DictCreator):
    """Creating dict by map feature"""
    def __call__(self):
        res_list = map(None, keys_list, values_list)
        res_dict = dict(res_list)
        return res_dict


class DictCompCreator(DictCreator):
    """Creating dict by Dict Comprehension"""
    def __call__(self):
        res_dict = {
            k:v for k, v  in zip_longest(keys_list, values_list)
            if k
        }
        return res_dict


if __name__ == '__main__':
    keys_list = [1, 2, 3, 4, 5, 6]
    values_list = ['1', '2', '3', '4']

    dict_creators = [
        MapDictCreator(keys_list, values_list),
        DictCompCreator(keys_list, values_list),
    ]

    for dict_creator in dict_creators:
        dict_ = dict_creator()
        try:
            check_dict(dict_, keys_list, values_list)
        except DictValidationError:
            print "Houston we have a problem"
        else:
            print dict_
