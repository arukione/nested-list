# nested-list
 **A nested list Tool which is pure Python.**

**This package can handle some nested lists in Python. You can use pip command to install this package:`pip3 install nested-list`.**

nested lists like these:
```Python
[
	[value1, value2],
	[value1, value2]
]
or
[
	(value1, value2),
	(value1, value2)
]
even
[
	{key1:value1, key2:value2},
	{key1:value1, key2:value2}
]
```

Use functions can help you easy to sort or delete nested lists elements like this that use `dict_sort(dict_list, key, 'ASC')` to sort dict order by key in list.

**It's develop version now, currently, only dict_list_sort function is avaliable.**
