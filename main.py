import community
import onadata as ona
import pandas as pd
import networkx as nx
from cdlib import algorithms
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

# see a list of data sets
ona.list_sets()

# load data into a dataframe
email_edge = ona.email_edgelist()
email_vertices = ona.email_vertices()


####### 4 ##########
graph = nx.from_pandas_edgelist(
    email_edge,
    source="from",
    target="to",
    create_using=nx.Graph
)

connected = nx.number_connected_components(graph)

largest  = max(nx.connected_components(graph), key=len)

print('Questão 4: ')
print('Quantidade de  elementos conectados: ', connected)
print('Maior componente conctado: ', largest)
print('__________________________________________________')

#######Questões 5 e 6##########
print('Questoes 5 e 6:')

louvain_comms = algorithms.louvain(graph)
pd.DataFrame(louvain_comms.communities).transpose()

louvain_modularaty = louvain_comms.newman_girvan_modularity()

partition = community.best_partition(graph)
ground_truth_modularaty =  community.modularity(partition, graph)

print('Ground truth departament: ', ground_truth_modularaty)

print('louvain: ', louvain_modularaty.score)
print('__________________________________________________')

#######Questão 7##########
node = list(graph.nodes)

communites = louvain_comms.to_node_community_map()
communites = [communites[k].pop() for k in node]

pastel2 = cm.get_cmap('Pastel2', max(communites) + 1)

np.random.seed(123)
nx.draw_spring(graph, cmap = pastel2, node_color = communites, edge_color = 'grey')
plt.show()

######Questão 8##########

a = np.random.random((16,16))
plt.imshow(a, cmap='Pastel2', interpolation='nearest')
plt.show()

######Questões 9 e 10#########
print('Questões 9 e 10')
cliques = nx.find_cliques(graph)
maximal_clique_size = nx.graph_clique_number(graph)
maximal_cliques = sorted(cliques, key=len)

print('Clique Maximo: ', maximal_clique_size )
print('Cliques maximais: ', len(maximal_cliques))




