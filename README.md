# Nested-List
 **A nested list Tool which is pure Python.**

## [中文介绍](#中文介绍)

[**Introduction in Chinese**](https://www.arukione.com/2020/01/30/%E5%9F%BA%E4%BA%8Eoperator%E6%9E%84%E5%BB%BA%E7%9A%84Nested-List/)

## [Instruction](#Instruction)

Nested-List is a nested listoperation library. It can operate on list whose elements are not basic data types.

Most functions are build with operator library.

## [Installation](#Installation)

Nested-List can be install with pip:

`$ pip install Nested-List`

or use pip to upgrade it:

`$ pip install --upgrade Nested-List`

## [Usage and Example](#Usage%20and%20Example)

Nested-List automatically check the type of elements in the passed List and calls the appropriate function to work.
You must to ensuer that teh elements in the List are of the same type no matter what is done, which is the basis of Nested-List work.

Every function must pass list whose will be operated when you use them.

```Python
def sort(nl, *key, order=False):
    ...

def delete_items(dl, keys, values, compare=None):
    ...

def max(nl, *keys):
    ...

def min(nl, *keys):
    ...
```

### [sort](#sort)

'nest_list.sort()' can according to the attribute of the element in the list to sort of list element.

The default is ascending sort order, when the order field is set to True or "DESC", 'nest_list.sort()' will work with descending order, when the incoming value dose not conform to the regulations will be sorted by default.

There is a note point is if you want to set the value of the order field, must pass in the value of the 'order' after all the parameters was passed in.

```Python
import nested_list as ntls

dict_list = [
    {'name':'one', 'age':11},
    {'name':'two', 'age':5},
    {'name':'three','age':26},
    {'name':'four','age':19}
]

ntls.sort(dict_list,'age',order=False)
print(dict_list)

# The output should be [{'name': 'two', 'age': 5}, {'name': 'one', 'age': 11}, {'name': 'four', 'age': 19}, {'name': 'three', 'age': 26}]
```

Of course the elements in the list can also be other objects, but you must make sure all objects are of the same type and you can specify sortable properties.

```Python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return 'User({})'.format(self.age)

user_list = [
    User('one',18),
    User('two',9),
    User('three',7),
    User('four',15)
]

ntls.sort(user_list, 'age')
print(user_list)

# The output should be [User(7), User(9), User(15), User(18)]
#if you don't rewrite the  __repr__ function, you won't see the sorting effect because it will print the object information.
```

You can pass in multiple paramenters to sort multiple times, as follows:

```Python
ntls.sort(user_list, 'id', 'age',order="DESC")
```

### [delete_items](#delete_items)

`delete_items` can delete the element according to the attribute value of the element in the list. Similarly, the list element can also be an object. However, when using `delete_items`, there are two points to notice when passing in the parameter:

1. No matter how many attributes will be passed in, they can only be passed in as an iterable object. In Python, although string can be iterated and if you incoming string will not be reported wrong, but you will get wrong execution results, so it is recommended to pass in a tuple or list

2. When there is only one incoming attribute, the incoming judgment value does not need to be stored in the iterable object, it can be directly passed in, otherwise there will be wrong execution results; When there are more than one passed attribute value, the passed judgment value **can only be pass in as a tuple object.**

For example:

```Python
# The right example
ntls.delete_items(user_list, ['age'], 7)
# or like this
ntls.delete_items(user_list, ('age'), 7)

# Wrong Examples
ntls.delete_items(user_list, ['age'], (7))
ntls.delete_items(user_list, 'age', 7)

# The right example
ntls.delete_items(user_list, None, ['age','name'],(7,'four'))

# Wrong Examples
ntls.delete_items(user_list, None, ['age','name'],7,'four')
ntls.delete_items(user_list, None, ['age','name'],[7,'four'])
```

### [max and min](#max%20and%20min)

The usage of 'nest_list.max' and 'nest_list.min' is as follows:

```Python
ntls.max(user_list, "age")
```

When there are multiple judgment attributes, multiple attribute names can be passed in directly.

```Python
ntls.max(user_list, "age", "id")
```

## [Acknowledgements](#Acknowledgements)

Thanks for 《Python Cookbook》3rd Edition author and translator, the initial development of this library is inseparable from
their inspiration to me.

**Python Cookbook 3rd Edition Documentation：**[https://python3-cookbook.readthedocs.io/zh_CN/latest/index.html](https://python3-cookbook.readthedocs.io/zh_CN/latest/index.html)

1.0.x
---
2020/1/31   正式发布
