import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import warnings
warnings.filterwarnings("ignore")



class NodeColour:
    WHITE = "WHITE"
    GRAY = "GRAY"
    BLACK = "BLACK"

class Node:
    def __init__(self, data):
        self.data = data
        self.distance = None
        self.predecessor = None
        self.colour = NodeColour.WHITE

    def __str__(self):
        return f"({self.data},d={self.distance})"

class AdjacencyList:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, n1, n2):
        if n1 in self.nodes:
            self.nodes[n1].append(n2)
        else:
            self.nodes[n1] = [n2]

    def bfs(self, s, destination):
        for u in self.nodes.keys():
            if u != s:
                u.colour = NodeColour.WHITE
                u.distance = float('inf')
                u.predecessor = None
        s.colour = NodeColour.GRAY
        s.distance = 0
        s.predecessor = None
        q = deque()
        q.append(s)
        while q:
            u = q.popleft()
            if u in self.nodes:
                for v in self.nodes[u]:
                    #print(u, "node awal")
                    #print(v)
                    #print()
                    if v.colour == NodeColour.WHITE:
                        v.colour = NodeColour.GRAY
                        v.distance = u.distance + 1
                        v.predecessor = u
                        q.append(v)
            u.colour = NodeColour.BLACK
            #print(u, end=" ")
            if u.data == destination.data:
                # Jika mencapai tujuan, cetak jalur dari s ke tujuan
                path = []
                while u is not None:
                    path.insert(0, u.data)
                    u = u.predecessor
                print(" -> ".join(str(node) for node in path))
                break


if __name__ == "__main__":
    # +++++++++++++++++++++++++++++++++++++++++++++++
    # Jawaban Nomor 1
    print("Jawaban Nomor 1")
    graph = AdjacencyList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    graph.add_edge(n1, n2)
    graph.add_edge(n2, n1)
    graph.add_edge(n2, n3)
    graph.add_edge(n3, n4)
    graph.add_edge(n3, n2)
    graph.add_edge(n4, n3)
    graph.add_edge(n4, n5)
    graph.add_edge(n4, n6)
    graph.add_edge(n5, n4)
    graph.add_edge(n5, n6)
    graph.add_edge(n5, n7)
    graph.add_edge(n6, n4)
    graph.add_edge(n6, n5)
    graph.add_edge(n6, n7)
    graph.add_edge(n6, n8)
    graph.add_edge(n7, n5)
    graph.add_edge(n7, n6)
    graph.add_edge(n7, n8)
    graph.add_edge(n8, n6)
    graph.add_edge(n8, n7)
    graph.bfs(n3, n8)
    graph.bfs(n3, n6)
    graph.bfs(n3, n7)
    print("\n")

    # Create a directed graph using networkx
    G = nx.DiGraph()
    edges = [(1, 2), (2, 1), (2, 3), (3, 4), (3, 2), (4, 3), (4, 5), (4, 6),
             (5, 4), (5, 6), (5, 7), (6, 4), (6, 5), (6, 7), (6, 8),
             (7, 5), (7, 6), (7, 8), (8, 6), (8, 7)]

    G.add_edges_from(edges)

    # Draw the directed graph with arrows
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', connectionstyle="arc3,rad=0.1")
    #plt.gcf().canvas.set_window_title("Graph Nomor 1")
    plt.show()
    # +++++++++++++++++++++++++++++++++++++++++++++++





    # +++++++++++++++++++++++++++++++++++++++++++++++
    # Jawaban Nomor 2
    print("Jawaban Nomor 2")
    graph = AdjacencyList()
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    graph.add_edge(n0, n1)
    graph.add_edge(n0, n2)
    graph.add_edge(n1, n3)
    graph.add_edge(n1, n4)
    graph.add_edge(n2, n5)
    graph.add_edge(n2, n6)
    graph.bfs(n0, n5)
    print("\n")



    # Create a directed graph using NetworkX
    G = nx.DiGraph()
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    G.add_edges_from(edges)

    # Manually specify the positions of the nodes
    node_positions = {
        0: (0, 0),
        1: (-1, -1),
        2: (1, -1),
        3: (-2, -2),
        4: (0, -2),
        5: (2, -2),
        6: (1, -3),
    }

    # Draw the directed graph with arrows using the specified positions
    nx.draw(G, pos=node_positions, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', arrows=False)
    #plt.gcf().canvas.set_window_title("Graph Nomor 2")
    plt.show()
    # +++++++++++++++++++++++++++++++++++++++++++++++





    # +++++++++++++++++++++++++++++++++++++++++++++++
    # Jawaban Nomor 3
    print("Jawaban Nomor 3")
    graph = AdjacencyList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n11 = Node(11)
    n12 = Node(12)
    graph.add_edge(n1, n2)
    graph.add_edge(n1, n3)
    graph.add_edge(n1, n4)
    graph.add_edge(n2, n5)
    graph.add_edge(n2, n6)
    graph.add_edge(n4, n7)
    graph.add_edge(n4, n8)
    graph.add_edge(n5, n9)
    graph.add_edge(n5, n10)
    graph.add_edge(n7, n11)
    graph.add_edge(n7, n12)
    graph.bfs(n1, n9)
    print("\n")



    # Create a directed graph using NetworkX
    G = nx.DiGraph()
    edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9), (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)]
    G.add_edges_from(edges)

    # Manually specify the positions of the nodes
    node_positions = {
        1: (0, 0),
        2: (-1, -1),
        3: (0, -1),
        4: (1, -1),
        5: (-2, -2),
        6: (-1, -2),
        7: (1, -2),
        8: (2, -2),
        9: (-3, -3),
        10: (-2, -3),
        11: (1, -3),
        12: (2, -3),
    }

    # Draw the directed graph with arrows using the specified positions
    nx.draw(G, pos=node_positions, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', arrows=False)
    #plt.gcf().canvas.set_window_title("Graph Nomor 3")
    plt.show()
    # +++++++++++++++++++++++++++++++++++++++++++++++





    # +++++++++++++++++++++++++++++++++++++++++++++++
    # Jawaban Nomor 4
    print("Jawaban Nomor 4")
    graph = AdjacencyList()
    na = Node("A")
    nb = Node("B")
    nc = Node("C")
    nd = Node("D")
    ne = Node("E")
    nf = Node("F")
    ng = Node("G")
    nh = Node("H")
    ni = Node("I")
    graph.add_edge(nf, nb)
    graph.add_edge(nf, ng)
    graph.add_edge(nb, na)
    graph.add_edge(nb, nd)
    graph.add_edge(ng, ni)
    graph.add_edge(nd, nc)
    graph.add_edge(nd, ne)
    graph.add_edge(ni, nh)
    graph.bfs(nf, nc)
    print("\n")



    # Create a directed graph using NetworkX
    G = nx.DiGraph()
    edges = [("F", "B"), ("F", "G"), ("B", "A"), ("B", "D"), ("G", "I"), ("D", "C"), ("D", "E"), ("I", "H")]
    G.add_edges_from(edges)

    # Manually specify the positions of the nodes
    node_positions = {
        "F": (0, 0),
        "B": (-1, -1),
        "G": (1, -1),
        "A": (-2, -2),
        "D": (0, -2),
        "I": (2, -2),
        "C": (-1, -3),
        "E": (0, -3),
        "H": (2, -3),
    }

    # Draw the directed graph with arrows using the specified positions
    nx.draw(G, pos=node_positions, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', arrows=True)
    #plt.gcf().canvas.set_window_title("Graph Nomor 4")
    plt.show()
    # +++++++++++++++++++++++++++++++++++++++++++++++
