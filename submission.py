import mars_planner
import routefinder
import mapcoloring

# This will run the mains of mars_planner, routefinder, and mapcoloring
# The results are in the console, which isn't ideal, but the comments will help you go interpret it
#
# First will be mars_planner.py
# The searches ran include (in order), BFS, BFS subproblems (3), DFS, DFS subproblems
# DLS is also available, but I wanted to only include the searches with no constraints
# The output of mars_planner.py is as such:
#     Search name (like Default Condition BFS)
#     Whether a goal was found or not
#     The end state along with its previous states
#     The states generated (and depth if DFS)
#
# The second is the routefinder.py
# A* will run first, tell you if the goal has been found, and prints the steps taken, and finally the states
# Uniform cost search is after this and the same
#
# Lastly is mapcoloring.py
# It will only print out the results of the antenna problem

print("\nDone :D")