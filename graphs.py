#building graphs with hashmaps

graph = {}
graph["you"] = ["alice", "rolakem", "adil"]
graph["alice"] = ["brymom", "deeta", "elsa"]
graph["kamil"] = ["moshood", "damipe", "elizabeth"]

#print(graph["kamil"][1])


from collections import deque



def looking_for_dev():

    #creates new queue
    search_queue = deque()
    search_queue += graph["you"]

    while search_queue: #while queue isn't empty
        #take first item on queue
        person = search_queue.popleft()
    
    if person_is_developer(person):
        print (person + " is a developer")
        return True
    else: 
        search_queue += graph[person] #person isn't a developer so add all their friends to queue
    return False #no one in queue is a developer

def person_is_developer(name):
    return name[-1] == "m"

print (looking_for_dev())