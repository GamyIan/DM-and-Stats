edges = c('A','B',
          'A','C',
          'A','D',
          'B','C',
          'C','D',
          'C','F',
          'D','F',
          'D','E',
          'E','F',
          'E','G',
          'F','G')

adj_mat = matrix(c(0,6,4,5,0,0,0,
                   6,0,5,0,0,0,0,
                   4,5,0,6,0,6,0,
                   5,0,6,0,5,8,0,
                   0,0,0,5,0,4,6,
                   0,0,6,8,4,0,7,
                   0,0,0,0,6,7,0), nrow=7, byrow=TRUE)

row.names(adj_mat) = colnames(adj_mat) = c('A','B','C','D','E','F','G')
library(igraph)

g = graph(edges, directed=FALSE)

plot(g, vertex.size=40, edge.width=2, vertex.label.cex=1.2, edge.color = 'red')

gr = graph_from_adjacency_matrix(adj_mat, mode='undirected',weighted=TRUE)


tree = mst(gr)

plot(vertex.size = 40, edge.width = 5, edge.color = 'black', tree, edge.label = E(tree)$weight)
