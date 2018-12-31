
from edges import edgesCountList , edgesList
import networkx as nx
import matplotlib.pyplot as plt

# print(edgesCountList[1])

G=nx.Graph()

for i in range(len(edgesList)):
   G.add_edge(edgesList[i][0],edgesList[i][1],weight=edgesCountList[i])
Edges=G.edges()
print(Edges)


pos=nx.spring_layout(G,scale=2)
nx.draw_networkx(G,pos)
edge_labels=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)

nx.write_pajek(G,"nxOutput/1.net")


