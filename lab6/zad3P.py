import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl




def readWeightedGraph(nodesFile, edgesFile):
    G = nx.DiGraph()
    edges = nx.read_edgelist(edgesFile, data=(('weight', float),))
    nodes = nx.read_adjlist(nodesFile)

    G.add_nodes_from(nodes)
    G.add_edges_from(edges.edges(data=True))
    return G

def displayGraph(graph):
    pos = nx.circular_layout(graph)

    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx(graph, pos=pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=labels)
    plt.show()





G = readWeightedGraph('nodes','edges')


displayGraph(G)
