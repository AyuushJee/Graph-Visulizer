import numpy as np
import networkx as nx
from all_methods import create_bar_chart,create_histogram,create_line_plot,create_scatter_plot
from all_methods import add_node,add_edge,visualize_graph,visualize_dijkstra
def main():
    print("Menu: ")
    print("1: Plots")
    print("2: Graphs")
    print('3: Dijkstra Algorithm')
    n = int(input("Enter your choice: "))

    if n==1 :
        print("Choose a plot type:")
        print("1. Bar Chart")
        print("2. Histogram")
        print("3. Line Plot")
        print("4. Scatter Plot")
        choice = int(input("Enter your choice: "))

        if choice in [1, 2, 3, 4]:
            data = []
            if choice in [1, 2, 3, 4]:
                n = int(input("Enter the number of data points: "))
                for i in range(n):
                    data_point = float(input(f"Enter data point {i + 1}: "))
                    data.append(data_point)

            if choice == 1:
                categories = [f'Category {i + 1}' for i in range(len(data))]
                create_bar_chart(categories, data)
            elif choice == 2:
                create_histogram(data)
            elif choice == 3:
                x = np.arange(len(data))
                create_line_plot(x, data)
            elif choice == 4:
                x = np.random.rand(len(data))
                create_scatter_plot(x, data)
        else:
            print("Invalid choice.")

    if n==2:
        graph = nx.Graph()
        while True:
            print("\nMenu:")
            print("1. Add Node")
            print("2. Add Edge")
            print("3. Visualize Graph")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_node(graph)
            elif choice == "2":
                add_edge(graph)
            elif choice == "3":
                visualize_graph(graph)
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    if n==3:
        G = nx.DiGraph()
        while True:
            print("Menu:")
            print("1. Visualize Dijkstra's algorithm")
            print("2. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                count = int(input("Enter the number of edges: "))
                edge_nodes = []
                for i in range(0,count):
                    source = int(input("Enter the Start Node: "))
                    target = int(input("Enter the Target Node: "))
                    weight = int(input("Enter the Weight: "))
                    edge_info = (source, target, weight)
                    edge_nodes.append(edge_info)

                source_node = int(input("Enter the Source Node: "))
                target_node = int(input("Enter the Destination Node: "))

                G.add_weighted_edges_from(edge_nodes)
                visualize_dijkstra(G, source_node, target_node)

            elif choice == '2':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")



if __name__ =="__main__":
    main()

