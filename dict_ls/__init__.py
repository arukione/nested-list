"""
A package that operates on a list whose type of element is dict.
It's built based on the operator.itemgetter.
"""
from operator import itemgetter


def sort(dl, order=False, *keys):
    dl.sort(key=itemgetter(*keys), reverse=order if order is True or order == "DESC" else False)


def delete_items(dl, compare, keys, values):
    get_values = itemgetter(*keys)
    for d in dl:
        if compare == 'L' and get_values(d) <= values:
            dl.remove(d)
        elif compare == 'G' and get_values(d) >= values:
            dl.remove(d)
        elif get_values(d) == values:
            dl.remove(d)


def extremum(dl, mode, *keys):
    if mode == "max":
        return dl.max(key=itemgetter(*keys))
    elif mode == "min":
        return dl.min(key=itemgetter(*keys))
    else:
        raise Exception('Error mode value:{}'.format(mode))
