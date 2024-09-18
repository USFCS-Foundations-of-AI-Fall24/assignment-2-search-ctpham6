from collections import deque



## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True, subproblem=False) :
    search_queue = deque()
    closed_list = {}
    states_generated = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        states_generated += 1
        if goal_test(next_state[0], subproblem):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
    print("States Generated: " + str(states_generated))
### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True,limit=0) :
    search_queue = deque()
    closed_list = {}
    states_generated = 0
    check_depth_limit_reached = False
    depth = 1

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    if limit > 0 :
        check_depth_limit_reached = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        states_generated += 1
        depth += 1
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
            print("States Generated: " + str(states_generated))
            return next_state
        else :
            if check_depth_limit_reached :
                # Checks to see if going another depth is within the limit
                if depth + 1 <= limit:
                    successors = next_state[0].successors(action_list)
                    if use_closed_list:
                        successors = [item for item in successors
                                      if item[0] not in closed_list]
                        for s in successors:
                            closed_list[s[0]] = True
                    search_queue.extend(successors)
            else :
                successors = next_state[0].successors(action_list)
                if use_closed_list :
                    successors = [item for item in successors
                                        if item[0] not in closed_list]
                    for s in successors :
                        closed_list[s[0]] = True
                search_queue.extend(successors)
    print("States Generated: " + str(states_generated))
