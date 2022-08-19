# Поиск в ширину, используя хеш-таблицы (словари) и двусторонние очереди.
# [O(V+E); V - количество вершин графа, E - количество ребер графа]

from collections import deque


def check_person_seller(name):
    return name[-1] == 'n'


def search_mango_seller(dict_name):
    search_queue = deque()
    search_queue += graph[dict_name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if check_person_seller(person):
                print(f"{person} is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


graph = {"Shepard": ["Garrus", "Liara", "Wrex"],
         "Garrus": ["Grunt"],
         "Liara": ["Grunt", "Shadow Broker"],
         "Wrex": ["Mordin", "Tali"],
         "Shadow Broker": [],
         "Grunt": [],
         "Mordin": [],
         "Tali": []}

print(search_mango_seller('Shepard'))
