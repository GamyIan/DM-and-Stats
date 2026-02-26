library(igraph)

edges = c(
  "A","B",
  "A","C",
  "B","D",
  "C","D",
  "C","E",
  "D","E"
)

g=graph(edges, directed=FALSE)

degree(g)

plot(g, vertex.size=100, edge.width=5, edge.color='red')

E(g)$weight = c(10,15,20,25,30,35)

plot(g, vertex.size=50, edge.label=E(g)$weight, edge.width=5, edge.color='red')

mstree = mst(g)

plot(mstree, vertex.size=50, edge.label=E(mstree)$weight, edge.width=5, edge.color='red')

# Graph using Adjacency Matrix
adj_mat = matrix(c(
  0,1,1,0,0,
  1,0,0,1,0,
  1,0,0,1,1,
  0,1,1,0,1,
  0,0,1,1,0
), nrow=5, byrow=TRUE)

rownames(adj_mat) = colnames(adj_mat) = c("A","B","C","D","E")
adj_mat

gr=graph_from_adjacency_matrix(adj_mat, mode="undirected")
gr

plot(gr, vertex.size=50, edge.width=5, edge.color='red')


E(gr)$weight = c(10,15,20,25,30,35)
amst = mst(gr)

plot(amst, edge.label=E(amst)$weight,vertex.size=50, edge.width=5, edge.color='red')

