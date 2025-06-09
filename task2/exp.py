import networkx as nx
from collections import deque

G = nx.Graph()

cities = [
    "Kyiv",
    "Lviv",
    "Odessa",
    "Kharkiv",
    "Dnipro",
    "Zaporizhzhia",
    "Mykolaiv",
    "Vinnytsia",
    "Ivano-Frankivsk",
    "Ternopil",
    "Lutsk",
    "Cherkasy",
    "Chernihiv",
    "Sumy",
    "Rivne",
    "Zhytomyr",
    "Poltava",
    "Uzhhorod",
    "Chernivtsi",
    "Kropyvnytskyi",
]

G.add_nodes_from(cities)

edges = [
    ("Kyiv", "Lviv"),
    ("Kyiv", "Odessa"),
    ("Kyiv", "Kharkiv"),
    ("Kyiv", "Dnipro"),
    ("Kyiv", "Chernihiv"),
    ("Kyiv", "Zhytomyr"),
    ("Lviv", "Ternopil"),
    ("Lviv", "Ivano-Frankivsk"),
    ("Lviv", "Lutsk"),
    ("Odessa", "Mykolaiv"),
    ("Odessa", "Dnipro"),
    ("Dnipro", "Zaporizhzhia"),
    ("Dnipro", "Kharkiv"),
    ("Zaporizhzhia", "Mykolaiv"),
    ("Cherkasy", "Vinnytsia"),
    ("Vinnytsia", "Zhytomyr"),
    ("Zhytomyr", "Rivne"),
    ("Rivne", "Lutsk"),
    ("Sumy", "Chernihiv"),
    ("Kharkiv", "Poltava"),
    ("Chernivtsi", "Ivano-Frankivsk"),
    ("Chernivtsi", "Ternopil"),
    ("Uzhhorod", "Lviv"),
    ("Kropyvnytskyi", "Mykolaiv"),
]

G.add_edges_from(edges)


# DFS алгоритм
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path.append(start)
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            result = dfs(graph, neighbor, goal, path)
            if result:
                return result
    path.pop()  # Якщо шлях не знайшовся, повертаємося
    return None


# BFS алгоритм
def bfs(graph, start, goal):
    queue = deque([[start]])  # Черга зі шляхів
    visited = set()

    while queue:
        path = queue.popleft()  # Беремо перший шлях з черги
        node = path[-1]  # Останній вузол в цьому шляху

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


# Вхідні дані для пошуку
start_city = "Kyiv"
goal_city = "Odessa"

# Знаходимо шляхи за допомогою DFS та BFS
dfs_path = dfs(G, start_city, goal_city)
bfs_path = bfs(G, start_city, goal_city)

# Виводимо результати
print(f"Шлях від {start_city} до {goal_city} за допомогою DFS: {dfs_path}")
print(f"Шлях від {start_city} до {goal_city} за допомогою BFS: {bfs_path}")

