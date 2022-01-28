# problem on p.384 Grokking Algorithm
#graph in hashtable
graph = {}
# nest "start" graph in original graph 
graph["start"] = {}

#keys and values for Start position
graph['start']['a'] = 6
graph['start']['b'] = 2

# nest "a" graph within original graph 
graph["a"] = {}
graph["a"]["fin"] = 1

#nest "b" graph within original graph 
graph["b"] = {}
graph["a"]["fin"] = 1

print(graph['start']["b"])

