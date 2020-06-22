# Zadanie 3 Analiza obwodu elektrycznego
# Napisz program, który:

# a) Wczytuje z pliku listę krawędzi grafu opisującego obwód elektryczny.
# Wagi krawędzi określają opór fragmentu obwodu między dwoma węzłami.
# Wierzchołki grafu identyﬁkowane są przez liczby naturalne.

# b)  Wczytuje dodatkowo trójkę liczb (s,t,E), przy czym para (s,t) wskazuje
# między którymi węzłami sieci przyłożono siłę elektromotoryczną E. Opór wewnętrzny SEM można zaniedbać.

# c) Wykorzystując prawa Kirchhoﬀa znajduje natężenia prądu w każdej części obwodu
# i przedstawia je na rysunku w postaci grafu ważonego z etykietami.

# d) Wykorzystując metodę potencjałów węzłowych zaimplementuj alternatywne rozwiązanie problemu.

# e) Przedstaw (wizualizacja + sprawdzenie poprawności wyników)
# działanie programu dla grafów spójnych mających od 15 do 100 wierzchołków:
#   - Spójny graf losowy
#   – Graf 3-regularny (kubiczny)
#   – Graf złożony z dwóch grafów losowych połączonych mostkiem
#   – Graf siatka 2D


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np




def readWeightedGraph(nodesFile, edgesFile, directional):   # umożliwia czytanie zarówno grafów skierowanych jak i nieskierowanych
    if directional:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    edges = nx.read_edgelist(edgesFile, data=(('R', float),))
    nodes = nx.read_adjlist(nodesFile)

    G.add_nodes_from(nodes)
    G.add_edges_from(edges.edges(data=True))
    return G


def displayGraph(graph):    # wyświetlanie grafu i wag krawędzi (potrzebne, aby sprawdzić czy cokolwiek działa)
    pos = nx.circular_layout(graph)

    labels = nx.get_edge_attributes(graph, 'R')
    nx.draw_networkx(graph, pos=pos, with_labels=True, font_weight='bold', node_color='red')
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=labels)
    plt.show()



G = readWeightedGraph('zad3/nodes','zad3/edges', False)
displayGraph(G)



def Kirchoff(graph, s, t, E):
    n = len(graph.nodes)

    matrix_A = np.zeros((n, n)).astype(int)  # macierz adjacencji (1, jeśli są połączone)
    matrix_R = np.zeros((n, n)).astype(float)  # macierz "oporu"
    matrix_V = np.zeros((n, n)).astype(float)  # macierz źródeł napięcia

    for (node1, node2, data) in G.edges(data=True):
        matrix_A[int(node1)][int(node2)] = 1
        matrix_A[int(node2)][int(node1)] = 1

        matrix_R[int(node1)][int(node2)] = data["R"]
        matrix_R[int(node2)][int(node1)] = data["R"]

    matrix_V[s][t] = E
    # już przygotowane macierze


    #Tworzenie "spanning tree"
    vector_C = np.zeros(n).astype(int)
    vector_C[0] = 1
    matrix_B = np.zeros((n, n)).astype(int)

    for i in range(0, n):
        for j in range(0,n):
            if matrix_A[i][j] == 1 and vector_C[i] == 1 and vector_C[j] == 0:
                matrix_B[i][j] = 1
                matrix_B[j][i] = 1
                vector_C[j] = 1
            if matrix_A[i][j] == 1 and vector_C[i] == 0 and vector_C[j] == 1:
                matrix_B[i][j] = 1
                matrix_B[j][i] = 1
                vector_C[i] = 1

    # Macierz B jest macierzą adjacencji "spanning tree"




    # Szukanie niezależnych cykli
    matrix_C = np.zeros((n,n))
    matrix_Dk = np.zeros((n,n))

    for i in range(0,n):
        for j in range(0,n):
            matrix_C[i][j] = matrix_A[i][j] - matrix_B[i][j]    # macierz C zawiera jedynki tam, gdzie "usuwamy" połączenia
            matrix_Dk[i][j] = matrix_B[i][j]

    k = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if matrix_C[i][j] == 1:
                k = k + 1
                matrix_Dk[i][j] = 1
                matrix_Dk[j][i] = 1
                # prune Matrix_Dk tree (?)
                # muszę usunąć "zbędne" odnogi, które nie wchodzą w skład pętli


    m = k   # Liczba niezależnych cykli

    print(matrix_A)
    print(matrix_B)
    print(matrix_Dk)




    pass


Kirchoff(G, 0, 1, 12.5)

