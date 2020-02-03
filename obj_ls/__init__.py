"""
A package that operates on a list whose type of element is other object.
It's built based on the operator.attrgetter.
"""
from operator import attrgetter


def sort(ol, *keys, order=False):
    ol.sort(key=attrgetter(*keys), reverse=order if order is True or order == "DESC" else False)


def delete_items(dl, keys, values, compare):
    get_values = attrgetter(*keys)
    for d in dl:
        if compare == 'L' and get_values(d) <= values:
            dl.remove(d)
        elif compare == 'G' and get_values(d) >= values:
            dl.remove(d)
        elif get_values(d) == values:
            dl.remove(d)


def max(dl, *keys):
    return dl.max(key=attrgetter(*keys))


def min(dl, *keys):
    return dl.min(key=attrgetter(*keys))
