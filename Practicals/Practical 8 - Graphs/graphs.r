library(igraph)
edges = c('A','B','A','C','B','C','A','D','C','D','D','E','C','E')
g = graph(edges, directed=FALSE)
gr = graph(edges, directed=TRUE) # Directed Graph

#Finding Degree
degree(g)
degree(g, mode='in')
degree(g, mode='out')

# Plotting the graph
plot(g, vertex.size=10, vertex.label.cex=1.2, edge.width=2, edge.color = 'red')
plot(gr, vertex.size=10, vertex.label.cex=1.2, edge.width=2, edge.color = 'red')

# Assigning Weight
E(g)$weight = c(30,50,25,20,40,19,20)
plot(gr, vertex.size=10, vertex.label.cex=1.2, edge.width=2, edge.color = 'red', edge.label=E(g)$weight)

# Graph from Adjacency Matrix
adj_mat = matrix(c(0,1,1,1,0,
                   1,0,1,0,0,
                   1,1,0,1,1,
                   1,0,1,0,1,
                   0,0,1,1,0), nrow=5,byrow=TRUE)
rownames(adj_mat) = colnames(adj_mat) = c('A','B','C','D','E')
adj_mat
agr = graph_from_adjacency_matrix(adj_mat, mode='undirected')
agr
plot(agr, vertex.size=10, vertex.label.cex=1.2, edge.width=2, edge.color = 'red')
# Adding Weights again
E(g)$weight = c(30,25,50,20,40,19,20)
plot(agr, vertex.size=10, vertex.label.cex=1.2, edge.width=2, edge.color = 'red', edge.label=E(g)$weight)

# Minimal Spanning Tree
g2 = mst(agr)
#plot(g2, vertex.size=10, vertex.label.cex=1.2, edge.width=2, edge.color = 'red', edge.label=E(g)$weight)
plot(g2)


