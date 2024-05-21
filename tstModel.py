import model.model as model

mymodel = model.Model()
mymodel.buildGraph()
print(F"The graph has {mymodel.getNumNodes()} nodes." )
print(F"The graph has {mymodel.getNumEdges()} edges." )