# класс это тип данных

# класс это "чертеж"

# class MyClass:
#     cls_attr = 11
#     obj_attr: str
#
#     def __init__(self, obj_attr):
#         self.obj_attr = obj_attr
#
#     def say_something(self):
#         return f'I say: {self.obj_attr}'

# class MyCustomClass:
#     val: str
#
#     def __init__(self, some_val):
#         self.val = some_val
#
# class_obj = MyCustomClass('value')
# print(class_obj)

# class User:
#     role = "User"
#     group = "simple user"
#
#     def __init__(self, first_name: str) -> None:
#         self.first_name = first_name.title()
#         self.i = -1
#
#     def info(self) -> str:
#         self.foo()
#         return f"User: {self.first_name}, Role: {self.role}"
#
#     @classmethod
#     def foo(cls):
#         print("FOO")
#
#     @staticmethod
#     def bar():
#         print("BAR")

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     try:
    #         self.i += 1
    #         return self.first_name[self.i]
    #     except IndexError:
    #         self.i = -1
    #         raise StopIteration

    # def __len__(self):
    #     return len(self.first_name)
    #
    # def __getitem__(self, item):
    #     return self.first_name[item]


# class Vector:
#
#     def __init__(self, a: int, b: int):
#         self.a = a
#         self.b = b
#
#     def __len__(self):
#         return abs(self.a - self.b)