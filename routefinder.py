from queue import PriorityQueue
from Graph import Graph
from Graph import Node
from Graph import Edge

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
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


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    ## you do the rest.


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    sqt(a^ + b2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):

    try :
        map_file = open(filename)
        mars_graph = Graph()
        for line in map_file:
            node_string = line.split(":")[0]
            node = Node(val = node_string)
            edge_array = line.split(" ")
            edge_array.pop(0)
            mars_graph.add_node(node_string)
            for edge_string in edge_array:
                edge = Edge(src = node_string, dest = edge_string, val = 1)
                mars_graph.add_edge(edge)
        map_file.close()
        return map_state(mars_graph = mars_graph)
    except :
        print("Invalid Map File")
        return None

mars_map_state = map_state(mars_graph = read_mars_graph("MarsMap.txt"))