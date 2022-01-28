# Problem on page 424 of Grokking's Algorithm

# “Suppose you’re starting a radio show. You want to reach listeners in all 50 states. You have to decide what stations to play on to reach all those listeners. It costs money to be on each station, so you’re trying to minimize the number of stations you play on. You have a list of stations.” --> with some states over lapping 

# “How do you figure out the smallest set of stations you can play on to cover all 50 states?”



listOfStates = ["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]
states_needed = set(listOfStates)

#list of stations

#create hashtable
stations = {}
stations["2fm"] = set(["id", "nv", "ut"])
stations["BBC"] = set(["wa", "id", "mt"])
stations["Today"] = set(["or", "nv", "ca"])
stations["Pulse"] = set(["nv", "ut"])
stations["CapitalXtra"] = set(["ca", "az"])

# final set of stations placeholder
final_stations = set()

#station that covers the most uncovered state
best_station = None

#init placeholder set of all states stations covers that haven't been covered yet
states_covered = set()

# loop through keys and values in stations hashmap
for station, states_for_station in stations.items():
    # covered = states that intertwine in states_needed and states_for_station sets
    covered = states_needed & states_for_station

    if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered
        # get difference between states_needed set and states_covered set
    states_needed -= states_covered
    # append best_station to final_station set
    final_stations.add(best_station)

print(final_stations)