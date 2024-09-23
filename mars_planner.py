## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
from search_algorithms import breadth_first_search
from search_algorithms import depth_first_search

class RoverState :

    def __init__(self, loc = "station", sample_extracted = False, holding_sample = False, charged = False,
                 holding_tool = False, prev = None, sample_dropped_off = False, depth = 0) :
        self.loc = loc
        self.sample_extracted = sample_extracted
        self.holding_sample = holding_sample
        self.charged = charged
        self.prev = prev
        self.holding_tool = holding_tool
        self.sample_dropped_off = sample_dropped_off
        self.depth = depth

    def __eq__(self, other) :
        return (self.loc == other.loc and self.sample_extracted == other.sample_extracted and
                self.holding_sample == other.holding_sample and self.charged == other.charged and
                self.holding_tool == other.holding_tool and self.sample_dropped_off == other.sample_dropped_off)

    def __repr__(self) :
        return (f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n"+
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Charged? {self.charged}\n" +
                f"Holding Tool?: {self.holding_tool}\n" +
                f"Sample Dropped Off?: {self.sample_dropped_off}")

    def __hash__(self) :
        return self.__repr__().__hash__()

    def successors(self, list_of_actions) :

        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also
        succ = [(item(self), item.__name__) for item in list_of_actions]
        ## remove actions that have no effect
        succ = [item for item in succ if not item[0] == self]
        for s in succ:
            s[0].depth += 1
        return succ

## our actions will be functions that return a new state.

def move_to_sample(state) :
    r2 = deepcopy(state)
    r2.loc = "sample"
    r2.prev = state
    return r2

def move_to_station(state) :
    r2 = deepcopy(state)
    r2.loc = "station"
    r2.prev = state
    return r2

def move_to_battery(state) :
    r2 = deepcopy(state)
    r2.loc = "battery"
    r2.prev = state
    return r2

def pick_up_tool(state) :
    r2 = deepcopy(state)
    r2.holding_tool = True
    r2.prev = state
    return r2

def drop_tool(state) :
    r2 = deepcopy(state)
    r2.holding_tool = False
    r2.prev = state
    return r2

def use_tool(state) :
    r2 = deepcopy(state)
    if state.holding_tool and state.loc == "sample":
        r2.sample_extracted = True
    r2.prev = state
    return r2

def pick_up_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.holding_sample = True
    r2.prev = state
    return r2

def drop_sample(state) :
    r2 = deepcopy(state)
    if state.holding_sample and state.loc == "station":
        r2.holding_sample = False
        r2.sample_dropped_off = True
    r2.prev = state
    return r2

def charge(state) :
    r2 = deepcopy(state)
    if state.sample_dropped_off and state.loc == "battery":
        r2.charged = True
    r2.prev = state
    return r2

action_list = [charge, drop_sample, pick_up_sample,
               move_to_sample, move_to_battery, move_to_station, pick_up_tool, drop_tool, use_tool]

def battery_goal(state) :
    return state.loc == "battery"

def station_goal(state) :
    return state.loc == "station"

def sample_goal(state) :
    return state.loc == "sample"

def mission_complete(state, sub_problem = False) :
    if sub_problem :
        if sub_problem == "move_to_sample" :
            return state.loc == "sample"
        elif sub_problem == "remove_sample" :
            return state.sample_extracted
        elif sub_problem == "return_to_charger" :
            return state.loc == "battery" and state.sample_dropped_off
    else :
        return (state.charged == True and state.loc == "battery" and state.holding_sample == False and
                state.sample_extracted == True)


if __name__=="__main__" :

    s = RoverState()
    # These conditions force the search to solve a specific sub problem
    # This is done by eliminating all the work to do except for one
    s_move_sample_goal = RoverState()
    s_remove_sample_goal = RoverState(loc = "sample")
    s_return_charger_goal = RoverState(loc = "sample", sample_extracted = True)

    print("Default Condition Breadth")
    result_breadth = breadth_first_search(s, action_list, mission_complete)
    print("--------------------------------------------")
    print("Move To Sample Goal Breadth")
    move_sample_goal_breadth = breadth_first_search(s_move_sample_goal, action_list, mission_complete,
                                                    subproblem = "move_to_sample")
    print("--------------------------------------------")
    print("Remove Sample Goal Breadth")
    remove_sample_goal_breadth = breadth_first_search(s_remove_sample_goal, action_list, mission_complete,
                                                      subproblem = "remove_sample")
    print("--------------------------------------------")
    print("Move To Battery Goal Breadth")
    return_to_charger_goal_breadth = breadth_first_search(s_return_charger_goal, action_list, mission_complete,
                                                          subproblem = "return_to_charger")
    print("--------------------------------------------")

    print("Default Condition Depth")
    result_depth = depth_first_search(s, action_list, mission_complete)
    print("--------------------------------------------")
    print("Move To Sample Goal Depth")
    move_sample_goal_depth = depth_first_search(s_move_sample_goal, action_list, mission_complete,
                                                  subproblem = "move_to_sample")
    print("--------------------------------------------")
    print("Remove Sample Goal Depth")
    remove_sample_goal_depth = depth_first_search(s_remove_sample_goal, action_list, mission_complete,
                                                      subproblem = "remove_sample")
    print("--------------------------------------------")
    print("Move To Battery Goal Depth")
    return_to_charger_goal_depth = depth_first_search(s_return_charger_goal, action_list, mission_complete,
                                                  subproblem = "return_to_charger")
