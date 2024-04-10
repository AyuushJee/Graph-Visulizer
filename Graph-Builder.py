import numpy as np
import networkx as nx
from all_methods import create_bar_chart,create_histogram,create_line_plot,create_scatter_plot
from all_methods import add_node,add_edge,visualize_graph,visualize_dijkstra
import numpy as np
import networkx as nx

def main():
    while True:
        print("Menu: ")
        print("1: Plots")
        print("2: Graphs")
        print('3: Dijkstra Algorithm')
        print('4: Exit Program')
        n = int(input("Enter your choice: "))
        
        if n == 4:
            print("Exiting program.")
            break
        
        elif n == 1:
            while True:
                print("\nChoose a plot type:")
                print("1. Bar Chart")
                print("2. Histogram")
                print("3. Line Plot")
                print("4. Scatter Plot")
                print("5. Back to Main Menu")
                choice = int(input("Enter your choice: "))

                if choice == 5:
                    break

                elif choice in [1, 2, 3, 4]:
                    data = []
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

                else:
                    print("Invalid choice.")

        elif n == 2:
            while True:
                graph = nx.Graph()
                print("\nMenu:")
                print("1. Add Node")
                print("2. Add Edge")
                print("3. Visualize Graph")
                print("4. Back to Main Menu")
                choice = input("Enter your choice: ")

                if choice == "4":
                    break

                elif choice == "1":
                    add_node(graph)
                elif choice == "2":
                    add_edge(graph)
                elif choice == "3":
                    visualize_graph(graph)
                else:
                    print("Invalid choice. Please try again.")

        elif n == 3:
            while True:
                G = nx.DiGraph()
                print("\nMenu:")
                print("1. Visualize Dijkstra's algorithm")
                print("2. Back to Main Menu")
                choice = input("Enter your choice: ")

                if choice == '2':
                    break

                elif choice == '1':
                    count = int(input("Enter the number of edges: "))
                    edge_nodes = []
                    for i in range(count):
                        source = int(input("Enter the Start Node: "))
                        target = int(input("Enter the Target Node: "))
                        weight = int(input("Enter the Weight: "))
                        edge_info = (source, target, weight)
                        edge_nodes.append(edge_info)

                    source_node = int(input("Enter the Source Node: "))
                    target_node = int(input("Enter the Destination Node: "))

                    G.add_weighted_edges_from(edge_nodes)
                    visualize_dijkstra(G, source_node, target_node)

                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


