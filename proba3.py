# import functools
from datetime import datetime
import time


#
# f = open("test2.txt", "w", encoding="utf8")
# f.write(
#     "Иванов О. 4\n Петров И. 3\n Дмитриев Н. 2\n Смирнова О. 4\n Керченских В. 5\n Котов Д. 2\n Бирюкова Н. 1\n Данилов П. 3\n Аранских В. 5\n Лемонов Ю. 2\n Олегова К. 4")
#
# with open("test2.txt", "r") as f:
#     for a in reversed(f.readlines()):
#         print(a)
#     # print(input_file.readlines())
#     # with open("test1.txt", "w") as output_file:
#     #     for line in reversed(input_file.readlines()):
#     #         output_file.write(line)
# print(datetime.utcnow())
# from datetime import datetime
# import time  # проверять действие измерителя будем с помощью библиотеки time
#
#
# # вся суть этого измерителя заключается в том, что мы считаем разницу в секундах между открытием и закрытием контекстного менеджера
# class Timer:
#     def __init__(self):
#         pass
#
#     def __enter__(
#             self):  # этот метод вызывается при запуске с помощью with. Если вы хотите вернуть какой-то объект, чтобы потом работать с ним в контекстном менеджере, как в примере с файлом, то просто верните этот объект через return
#         self.start = datetime.utcnow()
#         return None
#
#     def __exit__(self, exc_type, exc_val, exc_tb):  # этот метод срабатывает при выходе из контекстного менеджера
#         print(f"Time passed: {(datetime.utcnow() - self.start).total_seconds()}")
#
#
# with Timer():
#     time.sleep(2)

# from datetime import datetime
# import time
#
# from contextlib import contextmanager  # импортируем нужный нам декоратор
#
#
# @contextmanager  # оборачиваем функцию в декоратор contextmanager
# def timer():
#     start = datetime.utcnow()
#     yield  # если вам нужно что-то вернуть через контекстный менеджер, просто вставьте этот объект сюда.
#     print(f"Time passed: {(datetime.utcnow() - start).total_seconds()}")
#
#
# with timer():
#     time.sleep(2)

def par_checker(string):
    stack = {}  # инициализируем стек
    for s in string:
        if s == "(":
            stack["("] += "("
        if s == "[":
            stack["["] += "["

        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент - открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0


# a = "(dsd)"
# print(par_checker(a))

# pars = {")" : "(", "]" : "["}
# def proba(list_):
#     steck = []
#     for s in list_:
#         if s in "([":
#             steck.append(s)
#         elif s in ")]":
#             if len(steck) > 0 and steck[-1] == pars[s]:
#                 steck.pop()
#             else:
#                 return False
#     return len(steck) == 0
#
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self

#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#     def pre_order(self):
#         print(self.value)  # процедура обработки
#
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.pre_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.pre_order()
#
#     def post_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.post_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.post_order()  # рекурсивно вызываем функцию
#
#         print(self.value)  # процедура обработки
#
# # создаем корень и его потомки /7|2|5\
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# # левое поддерево корня /2|7|6\
# node_7 = node_root.left_child.insert_left(2).insert_right(6)
# # правое поддерево предыдущего узла /5|6|11\
# node_6 = node_7.right_child.insert_left(5).insert_right(11)
# # правое поддерево корня /|5|9\
# node_5 = node_root.right_child.insert_right(9)
# # левое поддерево предыдущего узла корня /4|9|\
# node_9 = node_5.right_child.insert_left(4)
#
# # node_root.pre_order()
# print('------')
# node_root.post_order()

# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
#
#         pointer = self.first  # берем первый указатель
#         while pointer is not None:  # пока указатель не станет None
#             R += str(pointer.value)  # добавляем значение в строку
#             pointer = pointer.next  # идем дальше по указателю
#             if pointer is not None:  # если он существует добавляем пробел
#                 R += ' '
#         return R
#
#     def pushleft(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value, self.first)
#             self.first = new_node
#
#     def pushright(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value)
#             self.last.next = new_node
#             self.last = new_node
#
#     def popleft(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.first  # сохраняем первый элемент
#             self.first = self.first.next  # меняем указатель на первый элемент
#             return node  # возвращаем сохраненный
#
#     def popright(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.last  # сохраняем последний
#             pointer = self.first  # создаем указатель
#             while pointer.next is not node:  # пока не найдем предпоследний
#                 pointer = pointer.next
#             pointer.next = None  # обнуляем указатели, чтобы
#             self.last = pointer  # предпоследний стал последним
#             return node  # возвращаем сохраненный

# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(LL)

# def find(array, element):
#     count = 0
#     for i, a in enumerate(array):
#         if a == element:
#             count += 1
#             return i
#         return count
#     return False
#
# array = ({'i'}.[10,20,30])
# element = 30

# print(find(array, element))

# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0
# for i in range(len(array)):  # проходим по всему массиву
#     idx_min = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):
#         count += 1
#         if array[j] > array[idx_min]:
#             idx_min = j
#     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
#         array[i], array[idx_min] = array[idx_min], array[i]
#
# print(array, count)


# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     while idx > 0 and array[idx-1] > x:
#         count += 1
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x


def merge(A, B):
    i, j, C = 0, 0, []
    while True:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
            if i == len(A):
                C.extend(B[j:])
                break

        else:
            C.append(B[j])
            j += 1
            if j == len(B):
                C.extend(A[i:])
                break

    return C

def top_down_merge_sort():
    if len(A) == 1:
        return A

    d = len(A) // 2
    left = top_down_merge_sort(A[:d])
    right = top_down_merge_sort(A[d:])

    return merge(left, right)

array_1 = [2, 11, 13, 15, 3, 8, 7]
array_2 = [10, 1, 4, 6, 5, 9, 34, 12, 19]
count = 0
r = merge(array_1, array_2)
print(r)
print("\n",   count)
top_down_merge_sort(array_2)
