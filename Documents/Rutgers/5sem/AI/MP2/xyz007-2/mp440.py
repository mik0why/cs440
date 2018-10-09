import random

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
BFS add to queue 
'''
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
     return

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    # Your code here
    return False

'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    return

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    # Your code here
    return False

'''
DFS pop from queue
'''
def pop_front_DFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

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
    print('Current state', state, 'length', len(state))
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






