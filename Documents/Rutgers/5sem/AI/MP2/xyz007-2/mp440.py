import random


class Node(object):
    def __init__(self, node_id = None, visited = False, parent_node_id = None,  ctc = None, neighbors = [], id_cost = []):
        self.id = node_id
        self.vis = visited 
        self.parent = parent_node_id
        self.ctc = ctc
        self.neighbors = neighbors 
        self.id_cost = id_cost 


class Queue:
#    from collections import deque
    def __init__ (self):
        self.values =[]

    def isEmpty(self):
        if not self.values:
            return True
        return false

    def enqueue(self, node):
        self.values.insert(0, node)
        #self.values.

    def dequeue(self):
        return self.values.pop(0)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

# comment out later - trying to figure out how graph is defined
    #graph[n] = [node_id, visited, parent after CTC final, CTC, neighbors, id-cost-tuple]
'''
    _graph[1] = [1, False, 0, 0, 7, [(2, 1), (3, 4)], {2:1, 3:4}]
    _graph[2] = [2, False, 0, 0, 6, [(3, 2), (4, 5), (5, 12)], {3:2, 4:5, 5:12}]
    _graph[3] = [3, False, 0, 0, 4, [(4, 2)], {4:2}]
    _graph[4] = [4, False, 0, 0, 2, [(5, 3)], {5:3}]
    _graph[5] = [5, False, 0, 0, 0, [], {}]

'''
'''
BFS add to queue 
'''
# i'm figuring out how to implement Queue as a LL bc the nodes in it need to have all those properties

queue_BFS = Queue()
queue_DFS = Queue()
queue_UC = Queue()
queue_ASTAR = Queue()


def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
     return

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    # Your code here
    if not queue_BFS:
        return True #need to define queue_BFS as a global variable
    return False

'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)
'''
********************************************************************************************part2: 
'''
'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    dfs_node = Node()
    dfs_node.id = node_id
    dfs_node.parent = parent_node_id
    dfs_node.ctc = cost
    dfs_node.vis = initialize #not sure if visited is the best name for this

    #print("adding these values to queue", dfs_node.id)
    queue_DFS.enqueue(dfs_node)
    # Your code here
    return

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    # Your code here
    if not queue_DFS:
        return True #need to define queue_DFS as a global variable
    return False

'''
DFS pop from queue
'''
def pop_front_DFS():
    (node_id, parent_node_id) = (0, 0) #what is this?
    # Your code here
    deq_node = queue_DFS.dequeue() #need to dequeue a node, not an integer
    #print("deq node is: ", deq_node)
    (node_id, parent_node_id) = (deq_node.id, deq_node.parent)
    return (node_id, parent_node_id)
'''
********************************************************************************************part2: 

'''
'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    return

'''
UC add to queue 
'''
def is_queue_empty_UC():
    # Your code here
    if not queue_UC:
        return True #need to define queue_UC as a global variable
    return False

'''
UC pop from queue
'''
def pop_front_UC():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    return

'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    # Your code here
    if not queue_ASTAR:
        return True #need to define queue as a global variable
    return False

'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
    state = []
    # i = 0:
    for i in range(0, n):
        i = random.randint(i, n) #shouldn't this be some more complex function
        state.append(i)

    # Your code here 
    return state

get_random_state(7)
'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    #print('Current state', state, 'length', len(state))
    number_attacking_pairs = 0
    existing_els = [] # occupied spots
    matrix_rep = [[0 for x in range(len(state))] for x in range(len(state))] #representation of the matrix, initialized to 0
    for i in range(0, len(state)):
       #print(state[i])
        if (state[i]) in existing_els:
            number_attacking_pairs+=1
        existing_els.append(state[i])
        #print("i", i, "state i", state[i]) 
        matrix_rep[i][(state[i] - 1)] = "X" #denoting that the spot is taken
        if(matrix_rep[i][(state[i]-1)] == matrix_rep[(state[i]-1)][i]):
         #   print("diagonal")
            number_attacking_pairs+=1
    #print("number of pairs", number_attacking_pairs)
    return number_attacking_pairs

compute_attacking_pairs(get_random_state(7))

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
    final_state = []
    # Your code here
    return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = []
    # Your code here
    return final_state






