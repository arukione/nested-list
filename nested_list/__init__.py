"""
NestedList: A library that provides functions to operate on nested list

Copyright (c) 2020 NestedList Contributor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Please view all acknowledgements in the thanks.py file
# Please view the LICENSE of all open source library in QUOTE file.
# https://github.com/arukione/NestedList


import dict_ls
import obj_ls
import array_ls


def type_of_elem(nl):
    """
    :param nl:
    :return:
    """
    ty = 1
    while ty > 0:
        if not isinstance(nl[ty], type(nl[ty - 1])):
            raise Exception('Error Type: The elements in the list are not the same type')
        ty += 1
        if ty >= len(nl):
            break
    return type(nl[0])


def sort(nl, *keys, order=False,):
    """
    :param nl
    :param order: (DESC or True) and (ASC or False)
    """
    ty = type_of_elem(nl)
    if ty is list or ty is tuple:
        array_ls.sort(nl, *keys, order=order)
    elif ty is dict:
        dict_ls.sort(nl, *keys, order=order)
    else:
        obj_ls.sort(nl, *keys, order=order)


def delete_items(nl, indexes, values, compare=None):
    ty = type_of_elem(nl)
    if ty is list or ty is tuple:
        array_ls.delete_items(nl, compare, indexes, values)
    elif ty is dict:
        dict_ls.delete_items(nl, compare, indexes, values)
    else:
        obj_ls.delete_items(nl, compare, indexes, values)


def max(nl, *keys):
    """
    :param nl
    """
    ty = type_of_elem(nl)
    if ty is list or ty is tuple:
        return array_ls.max(nl, *keys)
    elif ty is dict:
        return dict_ls.max(nl, *keys)
    else:
        return obj_ls.max(nl, *keys)


def min(nl, *keys):
    """
    :param nl
    """
    ty = type_of_elem(nl)
    if ty is list or ty is tuple:
        return array_ls.min(nl, *keys)
    elif ty is dict:
        return dict_ls.min(nl, *keys)
    else:
        return obj_ls.min(nl, *keys)
