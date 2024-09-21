from queue import PriorityQueue
from Graph import Graph
from Graph import Node
from Graph import Edge

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    ## location = "1,1" means charger, the start point
    ## location = "8,8" means sample, the destination
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
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


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True, ucs = False) :

    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    next_state = search_queue.get()
    states_generated = 0
    while next_state :
        states_generated += 1
        if goal_test(next_state) :
            print("goal found")
            print("States Generated: " + str(states_generated))
            return next_state[0]
        else :
            for edge in next_state.mars_graph.get_edges:
                if ucs :
                    state_to_enqueue = map_state(location=edge, mars_graph=next_state.mars_graph, prev_state=next_state,
                                                 g=next_state.g + 1, h=h1(next_state))
                else :
                    state_to_enqueue = map_state(location=edge, mars_graph=next_state.mars_graph, prev_state=next_state,
                                                 g=next_state.g + 1, h=sld(next_state))
                search_queue.put(state_to_enqueue)
                if use_closed_list:
                    closed_list[startState] = True
        next_state = search_queue.get()
    print("goal not found")
    print("States Generated: " + str(states_generated))

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    p1_x = int(state.location[0])
    p1_y = int(state.location[2])
    return sqrt((p1_x - 1)^2 + (p1_y - 1)^2)

def read_mars_graph(filename):

    try :
        map_file = open(filename)
        mars_graph = Graph()
        for line in map_file:
            node_string = line.split(":")[0]
            node = Node(val = node_string)
            edge_array = line.split(" ")
            edge_array.pop(0)
            mars_graph.add_node(node.value)
            for edge_string in edge_array:
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
    print(mars_map_state.mars_graph.get_edges("1,1"))
    # a_star(mars_map_state, sld, mission_complete)