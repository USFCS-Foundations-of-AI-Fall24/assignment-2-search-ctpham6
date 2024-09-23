from collections import deque

## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True, subproblem=False) :

    search_queue = deque()
    closed_list = {}
    states_generated = 0
    search_queue.append((startState,""))

    # closed_list removes duplicate states
    if use_closed_list :
        closed_list[startState] = True
    # while an answer could potentially be reachable...
    while len(search_queue) > 0 :
        # this is a (state, "action") tuple
        next_state = search_queue.popleft()
        if goal_test(next_state[0], subproblem) :
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                print("----------")
                print(ptr)
                ptr = ptr.prev
            print("----------")
            print("States Generated: " + str(states_generated))
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    states_generated += 1
                    closed_list[s[0]] = True
            search_queue.extend(successors)
    print("States Generated: " + str(states_generated))
### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True,limit=0,subproblem=False) :

    search_queue = deque()
    closed_list = {}
    states_generated = 0
    check_depth_limit_reached = False

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    if limit > 0 :
        check_depth_limit_reached = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        if not check_depth_limit_reached or next_state[0].depth <= limit :
            if goal_test(next_state[0], subproblem):
                print("Goal found")
                print(next_state)
                ptr = next_state[0]
                while ptr is not None :
                    print("----------")
                    print(ptr)
                    ptr = ptr.prev
                print("----------")
                print("Depth: " + str(next_state[0].depth))
                print("States Generated: " + str(states_generated))
                return next_state
            else :
                successors = next_state[0].successors(action_list)
                if use_closed_list :
                    successors = [item for item in successors
                                        if item[0] not in closed_list]
                    for s in successors :
                        states_generated += 1
                        closed_list[s[0]] = True
                search_queue.extend(successors)
    print("Goal not found")
    print("Depth limit: " + str(limit))
    print("States Generated: " + str(states_generated))
