graph = {}
graph["you"] = ["alice", "rolake", "adil"]
graph["alice"] = ["brymom", "deeta", "elsa"]
graph["kamil"] = ["moshood", "damipe", "elizabeth"]

#print(graph["kamil"][1])


from collections import deque

def person_is_developer(name):
    return name[-1] == "m"


def looking_for_dev(name):
    #creates new queue
    search_queue = deque()
    search_queue += graph["you"]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        #check if person has been searched already
        if not person in searched:
            if person_is_developer(person):
                print(person + " is a dev")
                return True
        else:
            #add person's connection to queue
            search_queue += graph[person]
            searched.append(person)
    return False

looking_for_dev("you")


