# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    # Start State or the Start Coordinate in the Maze
    start_state = problem.getStartState()

    # Dictionary of {Key: Visited Hashed States, Value: True(Boolean)}
    visited = dict()

    # Using Stack Datastructure from util.py
    stack_func = util.Stack()
    
    #Start Node, with No Parent and No Action
    start_node = {}
    start_node['parent'] = None
    start_node['action'] = None
    start_node['state'] = start_state

    stack_func.push(start_node)


    while not stack_func.isEmpty():
    	
    	node = stack_func.pop()
    	state = node['state']

    	# If True, already visited - returns the control to the beginning of the while loop
    	if visited.has_key(hash(state)):
    		continue

    	visited[hash(state)] = True


    	if problem.isGoalState(state) == True:
    		break

    	successorsList = problem.getSuccessors(state)

    	for successor in successorsList:
    		if not visited.has_key(hash(successor[0])):
    			sub_node = {}
    			sub_node['parent'] = node
    			sub_node['action'] = successor[1]
    			sub_node['state'] = successor[0]
    			stack_func.push(sub_node)

	# List of actions to be returned by the definition DFS
    actionsList = []

    # Loop till node reaches to the start_node, where start_node['action'] = None
    while node['action'] != None:
        # Adding the action to the begining of the List
        actionsList.insert(0, node['action'])
        # Back-tracking the parent nodes
        node = node['parent']

    return actionsList

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Start State or the Start Coordinate in the Maze
    start_state = problem.getStartState()
    
    # Dictionary of {Key: Visited Hashed States, Value: True(Boolean)}
    visited = dict()

    # Using Queue Datastructure from util.py
    queue_func = util.Queue()
    
    #Start Node, with No Parent and No Action
    start_node = {}
    start_node['parent'] = None
    start_node['action'] = None
    start_node['state'] = start_state

    queue_func.push(start_node)


    while not queue_func.isEmpty():
    	
    	node = queue_func.pop()
    	state = node['state']

    	# If True, already visited - returns the control to the beginning of the while loop
    	if visited.has_key(hash(state)):
    		continue

    	visited[hash(state)] = True


    	if problem.isGoalState(state) == True:
    		break

    	successorsList = problem.getSuccessors(state)

    	for successor in successorsList:
    		if not visited.has_key(hash(successor[0])):
    			sub_node = {}
    			sub_node['parent'] = node
    			sub_node['action'] = successor[1]
    			sub_node['state'] = successor[0]
    			queue_func.push(sub_node)

	# List of actions to be returned by the definition DFS
    actionsList = []

    # Loop till node reaches to the start_node, where start_node['action'] = None
    while node['action'] != None:
        # Adding the action to the begining of the List
        actionsList.insert(0, node['action'])
        # Back-tracking the parent nodes
        node = node['parent']

    return actionsList

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # Start State or the Start Coordinate in the Maze
    start_state = problem.getStartState()
    
    # Dictionary of {Key: Visited Hashed States, Value: True(Boolean)}
    visited = dict()

    # Using Queue Datastructure from util.py
    priorityQueue_func = util.PriorityQueue()
    
    #Start Node, with No Parent and No Action
    start_node = {}
    start_node['parent'] = None
    start_node['action'] = None
    start_node['state'] = start_state
    start_node['cost'] = 0

    priorityQueue_func.push(start_node, start_node['cost'])


    while not priorityQueue_func.isEmpty():
    	
    	node = priorityQueue_func.pop()
    	state = node['state']
    	cost = node['cost']

    	# If True, already visited - returns the control to the beginning of the while loop
    	if visited.has_key(hash(state)):
    		continue

    	visited[hash(state)] = True


    	if problem.isGoalState(state) == True:
    		break

    	successorsList = problem.getSuccessors(state)

    	for successor in successorsList:
    		if not visited.has_key(hash(successor[0])):
    			sub_node = {}
    			sub_node['parent'] = node
    			sub_node['action'] = successor[1]
    			sub_node['state'] = successor[0]
    			sub_node['cost'] = cost + successor[2]

    			priorityQueue_func.push(sub_node, sub_node['cost'])

	# List of actions to be returned by the definition DFS
    actionsList = []

    # Loop till node reaches to the start_node, where start_node['action'] = None
    while node['action'] != None:
        # Adding the action to the begining of the List
        actionsList.insert(0, node['action'])
        # Back-tracking the parent nodes
        node = node['parent']

    return actionsList

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # Start State or the Start Coordinate in the Maze
    start_state = problem.getStartState()
    
    # Dictionary of {Key: Visited Hashed States, Value: True(Boolean)}
    visited = dict()

    # Using Queue Datastructure from util.py
    priorityQueue_func = util.PriorityQueue()
    
    #Start Node, with No Parent and No Action
    start_node = {}
    start_node['parent'] = None
    start_node['action'] = None
    start_node['state'] = start_state
    start_node['cost'] = 0
    start_node['heur_eval'] = heuristic(start_state, problem)

    # Adding the total cost = start_node cost + start_node heuristic cost
    priorityQueue_func.push(start_node, start_node['cost'] + start_node['heur_eval'])


    while not priorityQueue_func.isEmpty():
    	
    	node = priorityQueue_func.pop()
    	state = node['state']
    	cost = node['cost']
    	heur_eval = node['heur_eval']

    	# If True, already visited - returns the control to the beginning of the while loop
    	if visited.has_key(hash(state)):
    		continue

    	visited[hash(state)] = True


    	if problem.isGoalState(state) == True:
    		break

    	successorsList = problem.getSuccessors(state)

    	for successor in successorsList:
    		if not visited.has_key(hash(successor[0])):
    			sub_node = {}
    			sub_node['parent'] = node
    			sub_node['action'] = successor[1]
    			sub_node['state'] = successor[0]
    			sub_node['cost'] = cost + successor[2]
    			sub_node['heur_eval'] = heuristic(sub_node['state'], problem)

    			priorityQueue_func.push(sub_node, sub_node['cost'] + sub_node['heur_eval'])

	# List of actions to be returned by the definition DFS
    actionsList = []

    # Loop till node reaches to the start_node, where start_node['action'] = None
    while node['action'] != None:
        # Adding the action to the begining of the List
        actionsList.insert(0, node['action'])
        # Back-tracking the parent nodes
        node = node['parent']

    return actionsList
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
