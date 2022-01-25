#this only implements BFS 
#doesn't "do" or return anything with the code


graph = {
    'alice': ["Kamran", "Pete", "Jalinka"],
    "Levina": ["Celine", "Danitsja", "Laura"],
    "Dorian": ["Remmol"],
    "Rosa": ["Kamran", "Canadian Girl"]
}

searched = [] #list for visited nodes
queue = [] #init queue

def amsterdam_connect(searched, graph, node): #function for bfs
    searched.append(node) #add node to searched list
    queue.append(node) #add node to queue

    while queue: #loop to visit each node
        current_search = queue.pop(0) #traverse first item on list
        print (current_search, end=" ")

        for neighbour in graph[current_search]: #loop to search connected neighbours
            if neighbour not in searched:
                searched.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth-First Search")

amsterdam_connect(searched, graph, "alice")