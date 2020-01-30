"""
A package that operates on a list whose type of element is other object.
It's built based on the operator.attrgetter.
"""
from operator import attrgetter


def sort(ol, order=False, *keys):
    ol.sort(key=attrgetter(*keys), reverse=order if order is True or order == "DESC" else False)


def delete_items(dl, compare, keys, values):
    get_values = attrgetter(*keys)
    for d in dl:
        if compare == 'L' and get_values(d) <= values:
            dl.remove(d)
        elif compare == 'G' and get_values(d) >= values:
            dl.remove(d)
        elif get_values(d) == values:
            dl.remove(d)


def extremum(ol, mode, *keys):
    if mode == "max":
        return ol.max(key=attrgetter(*keys))
    elif mode == "min":
        return ol.min(key=attrgetter(*keys))
    else:
        raise Exception('Error mode value:{}'.format(mode))
