# import netconv
import networkx as NX
from networkX import G
#
# n = netconv.etwork()
# netconv.importPajek(n, 'VOSTOTAL.net')
#
# G = NX.Graph()
# netconv.netconv2NX(n, G)

import community
p = community.best_partition(G, weight='weight')
print(p)
print(len(G.nodes()))

file4=open('nxOutput/1.clu','a+')
file4.write("*Vertices %d \n"%(len(G.nodes())))
for x in p.values():
    file4.write("%d \n"%x)
file4.close()

