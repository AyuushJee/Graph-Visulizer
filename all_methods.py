from matplotlib import pyplot as plt
import networkx as nx

def create_bar_chart(x, y):
    plt.bar(x, y, color='blue')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart')
    plt.show()

def create_histogram(data):
    plt.hist(data, bins=10, color='green', alpha=0.7)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

def create_line_plot(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Plot')
    plt.grid(True)
    plt.show()

def create_scatter_plot(x, y):
    plt.scatter(x, y, color='red', marker='o')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot')
    plt.show()

def add_node(graph):
    node = input("Enter the name of the node: ")
    graph.add_node(node)
    print(f"Node '{node}' added.")

def add_edge(graph):
    source = input("Enter the source node: ")
    target = input("Enter the target node: ")
    graph.add_edge(source, target)
    print(f"Edge between '{source}' and '{target}' added.")

def visualize_graph(graph):
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()

def visualize_dijkstra(graph, source_node, target_node):
    shortest_paths = nx.single_source_dijkstra_path(graph, source_node)

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color='lightblue')

    for edge in graph.edges:
        edge_weight = graph[edge[0]][edge[1]]['weight']
        nx.draw_networkx_edge_labels(graph, pos, edge_labels={(edge[0], edge[1]): edge_weight})

    path_to_target = shortest_paths.get(target_node, None)
    if path_to_target:
        edges = [(path_to_target[i], path_to_target[i + 1]) for i in range(len(path_to_target) - 1)]
        nx.draw_networkx_edges(graph, pos, edgelist=edges, width=2.0, edge_color='red', arrowstyle='-|>')
    plt.show()