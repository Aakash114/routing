from search import *
from getgraph import *
import json

with open("bikes.json", "r") as fh:
    json_string = fh.read()
    
json_obj = json.loads(json_string)
(nodes, edges) = get_graph_from_json_string(json_obj, mode="bike")

# # print(nodes)
# # print(edges)

bike_graph = UndirectedGraph(edges)
bike_graph.locations = nodes

bike_problem = GraphProblem("83", "21", bike_graph)

solution = iterative_deepening_search(bike_problem).solution()
print(solution)




with open("buses.json", "r", encoding="utf8") as fh:
    json_string = fh.read()
    
json_obj = json.loads(json_string)
(nodes, edges) = get_graph_from_json_string(json_obj["results"], mode="bus")

with open("bus_objs.pickle", "wb") as fh:
    pickle.dump((nodes, edges), fh)

# print(nodes)
# print(edges)

# bike_graph = UndirectedGraph(edges)
# bike_graph.locations = nodes

# bike_problem = GraphProblem("83", "21", bike_graph)

# solution = iterative_deepening_search(bike_problem).solution()
# print(solution)



# HYPER PARAMETERS
DIST_FROM_PREV_LOC = 12 # upper bound for retrieving nodes, so as to constrain graph

# COMPUTED/GIVEN PARAMETERS
DIST_START_TO_DESTINATION = 20
DIST_TO_DESTINATION = 8

# STEPS
# create graph with only DIST_FROM_PREV_LOC or fewer metres from previous location
# AND DIST_TO_DESTINATION/DIST_FROM_START < 1

# JSON INPUT FORMAT
# can store in Firebase database/Firestore
"""
{
    {user_id}: 
    {
        "id": _,
        "start":_,
        "destination":_,
        "current_location": (lat, long),
        "params": {
                "pollution": _,
                :
                :
            },
        "preferred_mode": Car/Bus/Bike/Any
        "nodes": 
        {
            {node_id}:
                {
                    "id": _
                    "location": (lat, long),
                }
        }
        "edges": 
        {
            {edge_id}:
            {
                "id": _
                "source": {node_id},
                "dest": {node_id},
                "mode": Car/Bus/Bike/etc,
                "params":
                {
                    //depend on mode, separate edge for each mode
                    "estimated_duration": _ mins, 
                    "pollution": _,
                    :
                    :
                }
            }
        }
    }
}
"""

# ALGORITHMS
# if preferred_mode not ANY -> use default/OSRM?
# => ITERATIVE DEEPENING SEARCH
# calculate weights from current location to furthest node using params in user_priorities and params in 
# corresponding user's graph json

# OUTPUT
# Ordered List of node ids representing path till chosen node (closer to destination)

# for reference

""" [Figure 3.2]
Simplified road map of Romania
"""
romania_map2 = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))
romania_map2.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))
		
# basic testing

romania_problem = GraphProblem('Arad', 'Bucharest', romania_map2)
solution = iterative_deepening_search(romania_problem).solution()
# print(solution)


australia_map = UndirectedGraph(dict(
    T=dict(),
    SA=dict(WA=1, NT=1, Q=1, NSW=1, V=1),
    NT=dict(WA=1, Q=1),
    NSW=dict(Q=1, V=1)))
australia_map.locations = dict(WA=(120, 24), NT=(135, 20), SA=(135, 30),
                               Q=(145, 20), NSW=(145, 32), T=(145, 42),
                               V=(145, 37))
australia_prob = GraphProblem("SA", "WA", australia_map)
solution = iterative_deepening_search(australia_prob).solution()
print(solution)