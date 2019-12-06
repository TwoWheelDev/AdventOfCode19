import networkx as nx

infile = open("d6_input.txt", "r")
graph = nx.DiGraph()
for line in infile.readlines():
    a = [x.strip() for x in line.split(")")]
    graph.add_edge(*a)

print("Total number of orbits:", nx.transitive_closure(graph).size())
print("Orbital transfers from YOU to SAN:", nx.shortest_path_length(graph.to_undirected(), 'YOU', 'SAN')-2)
