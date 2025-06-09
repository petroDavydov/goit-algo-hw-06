import networkx as nx
import matplotlib.pyplot as plt


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
edges = [
    # Boss
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
    # Financial
    ("Server2_financial", "Server3_secretary"),
    ("Server3_secretary", "Server1_boss"),
    ("Server3_secretary", "Server2_financial"),
    # Developer
    ("Server4_developer", "Server3_secretary"),
    ("Server4_developer", "Server5_designer"),
    ("Server4_developer", "Server6_manager"),
    ("Server4_developer", "Server8_free_for_all_1"),
    ("Server4_developer", "Server9_free_for_all_2"),
    ("Server4_developer", "Server11_backup"),
    ("Server4_developer", "Server12_maintenance"),
    # Designer
    ("Server5_designer", "Server3_secretary"),
    ("Server5_designer", "Server6_manager"),
    ("Server5_designer", "Server8_free_for_all_1"),
    ("Server5_designer", "Server9_free_for_all_2"),
    ("Server5_designer", "Server11_backup"),
    ("Server5_designer", "Server12_maintenance"),
    # Manager
    ("Server6_manager", "Server3_secretary"),
    ("Server6_manager", "Server4_developer"),
    ("Server6_manager", "Server5_designer"),
    ("Server6_manager", "Server7_employees_only"),
    ("Server6_manager", "Server8_free_for_all_1"),
    ("Server6_manager", "Server9_free_for_all_2"),    
    ("Server6_manager", "Server11_backup"),
    ("Server6_manager", "Server12_maintenance"),
    # Employees
    ("Server7_employees_only", "Server12_maintenance"),
    ("Server7_employees_only", "Server6_manager"),
    ("Server8_free_for_all_1", "Server10_firewall"),
    ("Server8_free_for_all_1", "Server9_free_for_all_2"),
    ("Server8_free_for_all_1", "Server11_backup"),
    ("Server8_free_for_all_1", "Server12_maintenance"),
    # backup
    ("Server11_backup", "Server10_firewall"),
    # Maintenance
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


# Візуалізація графа
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_size=1000, node_color="lightblue",
        edge_color="gray", font_size=15, font_color="black", pos=pos)
plt.title("Network Access Graph with Firewall and Restricted Access")
plt.show()


# Аналіз графу
print("Number of servers:", G.number_of_nodes())
print("Number of connections:", G.number_of_edges())
print(f"Degree of each server: {dict(G.degree())}")

# use hint
centrality = nx.degree_centrality(G)
print("Centrality of each server:", centrality)
