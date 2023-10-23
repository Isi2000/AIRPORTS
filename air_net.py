import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from mpl_toolkits.basemap import Basemap

#nodes
nodes_info = pd.read_csv("new_data.txt")

names_map = dict(zip(nodes_info['Index'], nodes_info['Airport Name']))

coordinates_dict = dict(zip(nodes_info['Index'], nodes_info[['Latitude', 'Longitude']].apply(tuple, axis=1)))

print(nodes_info)
col_edges = ['departure', 'arrival', 'weight']
edges = pd.read_fwf('data.txt', header = None, names = col_edges)
print(edges)

air_graph = nx.from_pandas_edgelist(df = edges, source = 'departure', target = 'arrival', edge_attr = 'weight')

fig = plt.figure(figsize=(12, 10))

# Create a Basemap instance for the continental US
m = Basemap(llcrnrlat=24, urcrnrlat=49, llcrnrlon=-125, urcrnrlon=-66, resolution='i', projection='merc')

m.drawcoastlines()
m.drawcountries()

# Add points for airports
lons = nodes_info['Longitude'].tolist()
lats = nodes_info['Latitude'].tolist()

x, y = m(lons, lats)
print(air_graph)
print(x)


# Draw edges with weights
pos = {node: (x[idx], y[idx]) for idx, node in enumerate(air_graph.nodes())}  # Reversed due to (x, y) vs (lat, lon)

nx.draw(air_graph, pos, edge_color='blue', node_size = 1, width=0.2, alpha = 0.5)
plt.show()

