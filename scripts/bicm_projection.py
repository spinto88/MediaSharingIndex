#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:25:26 2023

@author: tcicchini
"""

import pandas as pd
import bicm
import networkx as nx
import os

# ------------------------------------------ Variable definition
DATA_PATH = '../Data/data.csv' # File location
NEWS_COL = 'url' # Column associated with news (used for counting when grouping)
US_COL = 'uid' # Column associated with users
MEDIA_COL = 'outlet' # Column associated with media outlets
FILE_MEDIA = '../Results/media_network_p01.gml' # Name of the output media network file
ALPHA = 0.1 # Significance value for the hypothesis test (note that being a multiple test, it is not actually the value against which it is compared)


#-------------- Fetching the Data --------------
d = pd.read_csv(DATA_PATH)

#----------- Generating dictionaries and the adjacency list
id_us = pd.DataFrame([{'i_us': i, US_COL: us} for i, us in enumerate(d[US_COL].unique())])
id_medio = pd.DataFrame([{'i_med': i, MEDIA_COL: us} for i, us in enumerate(d[MEDIA_COL].unique())])

# Adjacency list for finding the media projection
edgelist_row = sorted((d.groupby([US_COL, MEDIA_COL])[NEWS_COL].count().reset_index()
            )[[US_COL, MEDIA_COL]].merge(id_us,
                                            on=US_COL
                                            ).merge(id_medio,
                                                    on=MEDIA_COL)[['i_med', 'i_us']].values.tolist())

# We will use them to name nodes in the networks
id_medio = id_medio.set_index('i_med').to_dict()[MEDIA_COL]

# -------------------------- Performing the projection

B = bicm.BipartiteGraph() # Initialize bipartite graph
B.set_edgelist(edgelist_row) # Provide the data
B.get_bicm_matrix() # Generate the adjacency matrix of the model
B.get_bicm_fitnesses() # Adjust the model
B.compute_projection(alpha=ALPHA, # Compute the projection considering the model and real data, for a given ALPHA
                     threads_num=1)
p1 = B.get_rows_projection( # Obtain the sought monopartite graph
                            method='poison',
                            fmt='edgelist',
                            alpha=ALPHA
                            )
# -------------------------- Generate the graph resulting from the projection

mediaSharing = d[MEDIA_COL].value_counts().to_dict() # Number of times a media outlet was reposted
mediaUniqueNews = d.drop_duplicates(subset=NEWS_COL)[MEDIA_COL].value_counts().to_dict() # Number of unique news for each media outlet

g = nx.Graph()
g.add_edges_from([(id_medio[i], id_medio[j]) for i, j in p1])

nx.set_node_attributes(g,
                       mediaSharing,
                       'mediaSharing')
nx.set_node_attributes(g,
                       mediaUniqueNews,
                       'mediaUniqueNews')

nx.write_gml(g, FILE_MEDIA)
