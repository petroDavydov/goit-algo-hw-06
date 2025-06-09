import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Список серверів
servers = [
    "Server1_boss", "Server2_financial", "Server3_secretary", "Server4_developer",
    "Server5_designer", "Server6_manager", "Server7_employees_only",
    "Server8_free_for_all_1", "Server9_free_for_all_2", "Server10_firewall",
    "Server11_backup", "Server12_maintenance"
]

# Створення графа сервера
G = nx.Graph()

# Додаємо вузли-сервери
G.add_nodes_from(servers)

# Додаємо ребра між серверами
edges = [
    ("Server1_boss", "Server2_financial"),
    ("Server1_boss", "Server3_secretary"),
    ("Server1_boss", "Server4_developer"),
    ("Server1_boss", "Server5_designer"),
    ("Server1_boss", "Server6_manager"),
    ("Server1_boss", "Server7_employees_only"),
    ("Server1_boss", "Server8_free_for_all_1"),
    ("Server1_boss", "Server9_free_for_all_2"),
    ("Server1_boss", "Server10_firewall"),
    ("Server1_boss", "Server11_backup"),
    ("Server1_boss", "Server12_maintenance"),

    ("Server2_financial", "Server3_secretary"),
    ("Server3_secretary", "Server1_boss"),
    ("Server3_secretary", "Server2_financial"),

    ("Server4_developer", "Server3_secretary"),
    ("Server4_developer", "Server5_designer"),
    ("Server4_developer", "Server6_manager"),
    ("Server4_developer", "Server8_free_for_all_1"),
    ("Server4_developer", "Server9_free_for_all_2"),
    ("Server4_developer", "Server11_backup"),
    ("Server4_developer", "Server12_maintenance"),

    ("Server5_designer", "Server3_secretary"),
    ("Server5_designer", "Server6_manager"),
    ("Server5_designer", "Server8_free_for_all_1"),
    ("Server5_designer", "Server9_free_for_all_2"),
    ("Server5_designer", "Server11_backup"),
    ("Server5_designer", "Server12_maintenance"),

    ("Server6_manager", "Server3_secretary"),
    ("Server6_manager", "Server4_developer"),
    ("Server6_manager", "Server5_designer"),
    ("Server6_manager", "Server7_employees_only"),
    ("Server6_manager", "Server8_free_for_all_1"),
    ("Server6_manager", "Server9_free_for_all_2"),
    ("Server6_manager", "Server11_backup"),
    ("Server6_manager", "Server12_maintenance"),

    ("Server7_employees_only", "Server12_maintenance"),
    ("Server7_employees_only", "Server6_manager"),
    ("Server8_free_for_all_1", "Server10_firewall"),
    ("Server8_free_for_all_1", "Server9_free_for_all_2"),
    ("Server8_free_for_all_1", "Server11_backup"),
    ("Server8_free_for_all_1", "Server12_maintenance"),

    ("Server11_backup", "Server10_firewall"),

    ("Server12_maintenance", "Server10_firewall"),
    ("Server12_maintenance", "Server11_backup"),
    ("Server12_maintenance", "Server2_financial"),
    ("Server12_maintenance", "Server3_secretary"),
    ("Server12_maintenance", "Server4_developer"),
    ("Server12_maintenance", "Server5_designer"),
    ("Server12_maintenance", "Server6_manager"),
    ("Server12_maintenance", "Server7_employees_only"),
    ("Server12_maintenance", "Server8_free_for_all_1"),
    ("Server12_maintenance", "Server9_free_for_all_2"),
]

G.add_edges_from(edges)

# BFS algorithm to find the path


def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = path + [neighbor]
                queue.append(new_path)

    return None

# DFS algorithm to find the path


def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = [start]
    else:
        path.append(start)  # use hint
    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            result_newpath = dfs_path(graph, neighbor, goal, path + [neighbor])
            if result_newpath:
                return result_newpath
    return None


print(f"Name of the servers: {servers}")

# Введення користувача
start = input("Enter the name of the server you want to start from: ")
stop = input("Enter the name of the server you want to reach: ")

bfs_result = bfs_path(G, start, stop)
dfs_result = dfs_path(G, start, stop)


print(f"BFS Path from {start} to {stop}: {bfs_result}")
print(f"DFS Path from {start} to {stop}: {dfs_result}")


# use hint and knowleadge from google for visualisation and analysis

if bfs_result and dfs_result:
    print("\n🔍 Аналіз результатів:")
    print(f"📌 Довжина BFS-шляху: {len(bfs_result)}")
    print(f"📌 Довжина DFS-шляху: {len(dfs_result)}")

    if bfs_result == dfs_result:
        print("✅ BFS і DFS дали однаковий шлях.")
    else:
        print("⚡ BFS і DFS дали РІЗНІ шляхи.")
        print(f"🚀 BFS зазвичай знаходить КОРОТШИЙ ШЛЯХ, бо проходить рівні графа.")
        print(f"🛠 DFS може ПРОХОДИТИ ГЛИБШЕ, перш ніж знайде кінцевий вузол.")


bfs_result = bfs_result or []
dfs_result = dfs_result or []

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)

nodes_to_show = set(bfs_result) | set(dfs_result)

edges_to_show = [edge for edge in G.edges() if edge in list(
    zip(bfs_result, bfs_result[1:])) or edge in list(zip(dfs_result, dfs_result[1:]))]

nx.draw(
    G.subgraph(nodes_to_show), pos, with_labels=True, node_size=1000, font_size=12,
    node_color=[
        "red" if node in bfs_result else "green" for node in nodes_to_show],
    edge_color=["red" if edge in zip(
        bfs_result, bfs_result[1:]) else "green" for edge in edges_to_show]
)
plt.title("Filtered Graph: BFS (Red) & DFS (Green)")
plt.show()
