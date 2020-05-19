import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np

def create_random_directed_graph(nodes, edges):
    temp_graph = nx.DiGraph()
    temp_graph.add_nodes_from(range(nodes))
    for i in range(edges):

        node_from = random.randint(0, nodes-1)
        node_to =   random.randint(0, nodes-1)

        while (node_from, node_to) in temp_graph.edges:
            node_from = random.randint(0, nodes - 1)
            node_to =   random.randint(0, nodes - 1)

        temp_graph.add_edge(node_from, node_to)
    return temp_graph


def create_random_strongly_connected_directed_graph(nodes, min_edges):
    temp_graph = create_random_directed_graph(nodes, min_edges)
    while not nx.is_strongly_connected(temp_graph):

        node_from = random.randint(0, nodes-1)
        node_to = random.randint(0, nodes-1)

        while (node_from, node_to) in temp_graph.edges:
            node_from = random.randint(0, nodes-1)
            node_to = random.randint(0, nodes-1)

        temp_graph.add_edge(node_from, node_to)
    return temp_graph


def show_graph(graph, save=False, name=""):
    filename = "graph-{}__nodes-{}__edges-{}.png".format(name, graph.number_of_nodes(), graph.number_of_edges())

    print("Rozpoczynam generowanie " + filename)

    fig1, ax1 = plt.subplots(figsize=(10,5))
    ax1.set_title(name)
    nx.draw(graph, pos=nx.circular_layout(graph))
    nx.draw_networkx_labels(graph, pos=nx.circular_layout(graph))

    fig1.show()
    if save:
        fig1.savefig("zad1/plots/" + filename)
        print("Plik " + filename + " został zapisany.")
        pass
    else:
        print("Skończone generowanie " + filename)


show_graph(create_random_strongly_connected_directed_graph(6, 0))
show_graph(create_random_strongly_connected_directed_graph(10, 0))



def create_adjacency_matrix(graph):
    matrix_A = nx.to_numpy_array(graph)
    for node_a in graph.nodes():
        counter = 0
        for cell in matrix_A[int(node_a)]:
            counter = counter + cell
        if counter != 0:
            matrix_A[int(node_a)] /= counter
    return np.transpose(matrix_A)


g = create_random_strongly_connected_directed_graph(4,0)
print(create_adjacency_matrix(g))
show_graph(g)

print(create_adjacency_matrix(g)[0])


def metoda_potegowa__wektor_dom_wlasny(macierz):

    n = len(macierz)
    wektor = np.random.rand(n, 1)
    roznica = 99999

    i = 0
    while (i < 100000 and roznica > 0.00000001):
        wektor_next = macierz @ wektor
        wektor_next = wektor_next / np.linalg.norm(wektor_next, ord=1)
        roznica = np.linalg.norm(wektor - wektor_next, ord=1)

        wektor = wektor_next
        i = i+1

    return wektor


def simple_page_rank(graph):
    temp_adjacency_matrix = create_adjacency_matrix(graph)
    temp_vector = metoda_potegowa__wektor_dom_wlasny(temp_adjacency_matrix)
    return temp_vector

temp1_simple_page_rank = simple_page_rank(create_random_strongly_connected_directed_graph(10,0))
temp2_simple_page_rank = simple_page_rank(create_random_strongly_connected_directed_graph(20,0))
temp3_simple_page_rank = simple_page_rank(create_random_strongly_connected_directed_graph(30,0))

print(np.linalg.norm(temp1_simple_page_rank, ord=1))
print(np.linalg.norm(temp2_simple_page_rank, ord=1))
print(np.linalg.norm(temp3_simple_page_rank, ord=1))


temp4_simple_page_rank = simple_page_rank(create_random_directed_graph(10,6))
print(np.linalg.norm(temp4_simple_page_rank, ord=1))



def create_template1_graph():
    temp_graph = nx.DiGraph()
    temp_graph.add_nodes_from(range(5))
    temp_graph.add_edge(0, 1)
    temp_graph.add_edge(1, 2)
    temp_graph.add_edge(2, 3)
    temp_graph.add_edge(2, 4)
    temp_graph.add_edge(3, 0)
    temp_graph.add_edge(4, 0)
    return temp_graph

G = nx.DiGraph()
G.add_nodes_from([0,1,2])
G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(2,0)
G.add_edge(0,2)

print(simple_page_rank(G))
show_graph(G)





temp_graf = create_template1_graph()
print(simple_page_rank(temp_graf))
print(np.linalg.norm(simple_page_rank(temp_graf), ord=1))
show_graph(temp_graf)


def create_template2_graph():
    temp_graph = nx.DiGraph()
    temp_graph.add_nodes_from(range(13))
    temp_graph.add_edge(0, 1)
    temp_graph.add_edge(0, 4)
    temp_graph.add_edge(1, 4)
    temp_graph.add_edge(1, 2)
    temp_graph.add_edge(1, 5)
    temp_graph.add_edge(1, 11)
    temp_graph.add_edge(1, 8)
    temp_graph.add_edge(2, 6)
    temp_graph.add_edge(3, 1)
    temp_graph.add_edge(3, 7)
    temp_graph.add_edge(4, 8)
    temp_graph.add_edge(5, 2)
    temp_graph.add_edge(5, 8)
    temp_graph.add_edge(6, 5)
    temp_graph.add_edge(6, 7)
    temp_graph.add_edge(6, 9)
    temp_graph.add_edge(7, 1)
    temp_graph.add_edge(8, 4)
    temp_graph.add_edge(8, 3)
    temp_graph.add_edge(8, 0)
    temp_graph.add_edge(9, 5)
    temp_graph.add_edge(10, 8)
    temp_graph.add_edge(10, 11)
    temp_graph.add_edge(11, 8)
    temp_graph.add_edge(11, 9)
    temp_graph.add_edge(11, 12)
    temp_graph.add_edge(12, 3)
    temp_graph.add_edge(12, 6)
    temp_graph.add_edge(12, 9)
    temp_graph.add_edge(12, 10)

    return temp_graph


temp_graf = create_template2_graph()
print(simple_page_rank(temp_graf))
print(np.linalg.norm(simple_page_rank(temp_graf), ord=1))
show_graph(temp_graf)










def create_default_e(graph):
    n = nx.number_of_nodes(graph)
    for node_a, node_b in graph.edges():
        if int(node_a) > n:
            n = 1+ int(node_a)
        if int(node_b) > n:
            n = 1+ int(node_b)
    e = np.zeros((1, n))
    i = 0
    for node_a, node_b in graph.edges():
        e[0][int(node_b)] += 1
        i += 1
    return e/i





def full_page_rank(graph, e, d):
    temp_adjacency_matrix = create_adjacency_matrix(graph)
    n = len(temp_adjacency_matrix)
    matrix_B = d * temp_adjacency_matrix + (1-d)*np.dot(e, np.diag(np.full(n, 1)))

    temp_vector = metoda_potegowa__wektor_dom_wlasny(matrix_B)
    return temp_vector



a = full_page_rank(temp_graf, create_default_e(temp_graf), 0.5)
print(a)









print("*****************************************************")













def read_directed_graph_from_file(filename):
    graph = nx.DiGraph()
    file = open(filename, "r")
    lines = file.readlines()
    biggest_index = 0
    for line in lines:
        if line[0] == "#":
            continue
        node_a, node_b = line.split()
        graph.add_edge(int(node_a), int(node_b))
        if int(node_a) > biggest_index:
            biggest_index = int(node_a)
        if int(node_b) > biggest_index:
            biggest_index = int(node_b)
    for i in range(biggest_index+1):
        graph.add_node(i)
    file.close()
    return graph







wiki_vote = read_directed_graph_from_file("Wiki-Vote.txt")
print(full_page_rank(wiki_vote, create_default_e(wiki_vote), 0.85))




def create_default_e(graph):   #posprzątanie "print()"
    n = nx.number_of_nodes(graph)
    e = np.zeros((1, n))
    i = 0
    for node_a, node_b in graph.edges():
        e[0][int(node_b)] += 1
        i += 1
    return e/i

def create_different_e(graph):
    n = nx.number_of_nodes(graph)
    e = np.ones((1, n))
    return e/n