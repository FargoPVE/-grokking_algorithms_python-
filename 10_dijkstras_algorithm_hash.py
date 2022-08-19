# Алгоритм Дейкстры, используя хеш-таблицы (словари).
# [O(E*log V); V - количество вершин графа, E - количество ребер графа]

graph = {'start': {'A': 6, 'B': 2},
         'B': {'A': 3, 'end': 5},
         'A': {'B': 3, 'end': 1},
         'end': {}}

infinity = float('inf')

costs = {'A': 6,
         'B': 2,
         'end': infinity}

parents = {'a': 'start',
           'b': 'start',
           'end': None}

processed = []


def find_lowest_cost_node(table_of_costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for key_node in table_of_costs.keys():
        value_cost = table_of_costs[key_node]
        if value_cost < lowest_cost and key_node not in processed:
            lowest_cost = value_cost
            lowest_cost_node = key_node
    return lowest_cost_node


node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for neighbors_name in neighbors.keys():
        new_cost = cost + neighbors[neighbors_name]
        if costs[neighbors_name] > new_cost:
            costs[neighbors_name] = new_cost
            parents[neighbors_name] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)
