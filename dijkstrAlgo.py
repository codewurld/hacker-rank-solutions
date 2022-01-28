# problem on p.384 Grokking Algorithm

#SET UP

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
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

#nest empty "fin" graph within original graph 
graph["fin"] = {}


#cost hashtable
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#parents hashtable
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None



#find value of edge b
print(graph['start']["b"])
#find key values of start graph
print(graph['start'].keys())

#IMPLEMENTATION

def find_lowest_cost_node(costs):
    # start with infinity
    lowest_cost = float("inf")
    lowest_cost_node = None
    # iterate each node
    for node in costs:
        cost = costs[node]
        # if lowest cost is greater than cost and not already processed
        if lowest_cost > cost and node not in processed:
            # reassign values
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


#keep track of processed nodes
processed = []

#find the lowest cost node not processed
node = find_lowest_cost_node(costs)
# while loop complete if all node = processed
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    # for each neighbours of this node
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        # if new_cost cheaper 
        if costs[n] > new_cost:
            #update cost to new cost and maake node new parent for neighbour n
            costs[n] = new_cost
            parents[n] = node
    # add node to processed
    processed.append(node)
    # recurse next node
    node = find_lowest_cost_node(costs)

