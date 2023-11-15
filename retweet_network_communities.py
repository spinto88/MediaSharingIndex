import pandas as pd 
import networkx as nx 

# Adjacency weighted data
df = pd.read_csv('Weighted_RT_net.csv')

# Creation of the directed weighted graph: the direction points out information flow 
graph = nx.from_pandas_edgelist(df, source = 'uid_rt', target = 'uid', edge_attr = 'weight', create_using = nx.DiGraph())

print('Number of nodes: ', graph.number_of_nodes())
print('Number of edges: ', graph.number_of_edges())

# Community detection algorithm
communities = nx.community.louvain_communities(graph, seed = 123457)

print('Number of communities: ', len(communities))
print('Modularity score: ', nx.community.modularity(graph, communities))

# Save the data
nodes = []
community_label = []
for i in range(len(communities)):
    nodes += list(communities[i])
    community_label += [i] * len(communities[i])

df2save = pd.DataFrame()
df2save['uid'] = nodes
df2save['community_label'] = community_label
df2save.to_csv('User_community.csv', index = False)
