import networkx as nx
import matplotlib.pyplot as plt
import heapq as hq


# Список серверів
servers = [
    "Server1_boss", "Server2_financial", "Server3_secretary", "Server4_developer",
    "Server5_designer", "Server6_manager", "Server7_employees_only",
    "Server8_free_for_all_1", "Server9_free_for_all_2", "Server10_firewall",
    "Server11_backup", "Server12_maintenance"
]

# Створення нрафа-сервера
G = nx.Graph()

# Додаємо вузли-сервери
G.add_nodes_from(servers)

# Додаємо ребра між серверами
edges_with_weight = [
    # Boss 12
    ("Server1_boss", "Server2_financial", 12),
    ("Server1_boss", "Server3_secretary", 11),
    ("Server1_boss", "Server4_developer", 1),
    ("Server1_boss", "Server5_designer", 1),
    ("Server1_boss", "Server6_manager", 10),
    ("Server1_boss", "Server7_employees_only", 1),
    ("Server1_boss", "Server8_free_for_all_1", 1),
    ("Server1_boss", "Server9_free_for_all_2", 1),
    ("Server1_boss", "Server10_firewall", 10),
    ("Server1_boss", "Server11_backup", 9),
    ("Server1_boss", "Server12_maintenance", 8),
    # Financial
    ("Server2_financial", "Server3_secretary", 11),
    ("Server3_secretary", "Server1_boss", 12),
    ("Server3_secretary", "Server2_financial", 11),
    # Developer
    ("Server4_developer", "Server3_secretary", 5),
    ("Server4_developer", "Server5_designer", 12),
    ("Server4_developer", "Server6_manager", 8),
    ("Server4_developer", "Server8_free_for_all_1", 10),
    ("Server4_developer", "Server9_free_for_all_2", 10),
    ("Server4_developer", "Server11_backup", 12),
    ("Server4_developer", "Server12_maintenance", 10),
    # Designer
    ("Server5_designer", "Server3_secretary", 5),
    ("Server5_designer", "Server6_manager", 8),
    ("Server5_designer", "Server8_free_for_all_1", 7),
    ("Server5_designer", "Server9_free_for_all_2", 3),
    ("Server5_designer", "Server11_backup", 12),
    ("Server5_designer", "Server12_maintenance", 10),
    # Manager
    ("Server6_manager", "Server3_secretary", 10),
    ("Server6_manager", "Server4_developer", 11),
    ("Server6_manager", "Server5_designer", 11),
    ("Server6_manager", "Server7_employees_only", 4),
    ("Server6_manager", "Server8_free_for_all_1", 2),
    ("Server6_manager", "Server9_free_for_all_2", 3),
    ("Server6_manager", "Server11_backup", 12),
    ("Server6_manager", "Server12_maintenance", 10),
    # Employees
    ("Server7_employees_only", "Server12_maintenance", 12),
    ("Server7_employees_only", "Server6_manager", 11),
    ("Server8_free_for_all_1", "Server10_firewall", 9),
    ("Server8_free_for_all_1", "Server9_free_for_all_2", 12),
    ("Server8_free_for_all_1", "Server11_backup", 1),
    ("Server8_free_for_all_1", "Server12_maintenance", 12),
    # backup
    ("Server11_backup", "Server10_firewall", 12),
    # Maintenance
    ("Server12_maintenance", "Server10_firewall", 12),
    ("Server12_maintenance", "Server11_backup", 12),
    ("Server12_maintenance", "Server2_financial", 11),
    ("Server12_maintenance", "Server3_secretary", 10),
    ("Server12_maintenance", "Server4_developer", 9),
    ("Server12_maintenance", "Server5_designer", 9),
    ("Server12_maintenance", "Server6_manager", 8),
    ("Server12_maintenance", "Server7_employees_only", 7),
    ("Server12_maintenance", "Server8_free_for_all_1", 6),
    ("Server12_maintenance", "Server9_free_for_all_2", 5),
]

G.add_weighted_edges_from(edges_with_weight)


# Візуалізація графа
plt.figure(figsize=(15, 8))
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_size=1000, node_color="lightblue",
        edge_color="gray", font_size=15, font_color="black", pos=pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(
    G, 'weight'), font_color='lightgreen', font_size=12)

plt.title("Servers and Connections Graph with Weights")
plt.show()


# Фналіз даних графу за допомогою алгоритму Дейкстри
def dijkstra_path_hand(graph, start_server):
    shortest_paths = {server: float('inf') for server in graph.nodes}
    shortest_paths[start_server] = 0

    priority_queue = [(0, start_server)]

    while priority_queue:
        current_distance, current_server = hq.heappop(priority_queue)

        if current_distance > shortest_paths[current_server]:
            continue

        for neighbor, weight in graph[current_server].items():
            distance = current_distance + weight['weight']

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                hq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


start_server = "Server11_backup"

shortest_path = dijkstra_path_hand(G, start_server)

# Виводимо найкоротші шляхи
print(f"Shortest path to  {start_server}:")
for server, distance in shortest_path.items():
    print(f"From {start_server} -to-> {server}: {distance} node(s)")
