from queue import PriorityQueue
from Graph import Graph
from Graph import Node
from Graph import Edge
import math

class map_state() :

    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    ## location = "1,1" means charger, the start point
    ## location = "8,8" means sample, the destination
    def __init__(self, location = "", mars_graph = None, prev_state = None, g = 0, h = 0) :
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :

    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    next_state = search_queue.get()
    states_generated = 0

    if use_closed_list :
        closed_list[start_state] = True
    # while the next_state is a valid state. If not, then the priority queue is empty
    while next_state :
        if goal_test(next_state) :
            print("[Goal Found]")
            ptr = next_state
            print("Steps Taken:")
            while ptr :
                print(ptr)
                ptr = ptr.prev_state
            print("States Generated: " + str(states_generated))
            return next_state
        else :
            # Every state after the current one has a cost of the current one + 1
            for edge in next_state.mars_graph.get_edges(next_state.location) :
                state_to_enqueue = map_state(location = edge.dest, mars_graph = next_state.mars_graph,
                                             prev_state = next_state, g = 1,
                                             h = heuristic_fn(edge.dest))
                # If there is no entry for the state in the closed_list, then it has been gone over already
                if use_closed_list :
                    try :
                        closed_list[state_to_enqueue]
                    except :
                        closed_list[state_to_enqueue] = True
                        search_queue.put(state_to_enqueue)
                        states_generated += 1
                else :
                    search_queue.put(state_to_enqueue)
                    states_generated += 1
        next_state = search_queue.get()
    print("goal not found")
    print("States Generated: " + str(states_generated))

## default heuristic - we can use this to implement uniform cost search
def h1(state) :

    return 0

## a_star heuristic - return the straight-line distance between the state and the target, (8,8)
def sld(location) :

    p2_x = int(location[0])
    p2_y = int(location[2])
    return (((8 - p2_x) ** 2) + ((8 - p2_y) ** 2)) ** 0.5

def read_mars_graph(filename) :

    try :
        map_file = open(filename)
        mars_graph = Graph()
        for line in map_file :
            node_string = line.split(":")[0]
            node = Node(val = node_string)
            edge_array = line.split(" ")
            edge_array.pop(0)
            mars_graph.add_node(node.value)
            for edge_string in edge_array :
                edge = Edge(src = node.value, dest = edge_string.strip(), val = 1)
                mars_graph.add_edge(edge)
        map_file.close()
        return mars_graph
    except :
        print("Invalid Map File")
        return None

def mission_complete(state, sub_problem = False) :

    return state.location == "8,8"

if __name__=="__main__" :

    mars_map_state = map_state(location="1,1", mars_graph = read_mars_graph("MarsMap.txt"))
    print("a*: ")
    a_star(mars_map_state, sld, mission_complete)
    print("")
    print("uniform cost search: ")
    a_star(mars_map_state, h1, mission_complete)