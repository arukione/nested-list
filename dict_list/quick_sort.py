def dict_list_sort(dict_list, field, order):
    if order == "ASC":
        quick_sort(dict_list, 0, len(dict_list) - 1, field, 1)
    if order == "DESC":
        quick_sort(dict_list, 0, len(dict_list) - 1, field, -1)


def quick_sort(dict_list, left, right, field, order):
    if left < right:
        pivot_index = partition_ascend(dict_list, left, right, field, order)
        quick_sort(dict_list, pivot_index + 1, right, field, order)
        quick_sort(dict_list, left, pivot_index - 1, field, order)


def partition_ascend(dict_list, left, right, field, order):
    pivot_value = dict_list[right][field]
    pivot_index = left - 1
    for index in range(left, right):
        if order_describe(order, dict_list[index][field], pivot_value):
            pivot_index += 1
            dict_list[pivot_index], dict_list[index] = dict_list[index], dict_list[pivot_index]
    dict_list[pivot_index + 1], dict_list[right] = dict_list[right], dict_list[pivot_index + 1]
    return pivot_index + 1


def order_describe(order, value, pivot_value):
    if order > 0:
        return value <= pivot_value
    else:
        return value >= pivot_value
