from jug_operations import operations
import constants as const

graph = {}
child_count = 0
search_result = []

def add_new_node(i, parent_id, x, y):
    '''
    Populate the graph global variable dictionary with key value pairs.
    The key is the parent node, and value is a list of child nodes directly attached.
    The graph is populated in a Breadth First approach
    '''
    global child_count
    parent_node = [x, y]
    child_nodes = set()

    node_id = i

    # Generateing the nodes
    child_nodes.add(operator.fillA(parent_node[0], parent_node[1]))
    child_nodes.add(operator.fillB(parent_node[0], parent_node[1]))
    child_nodes.add(operator.pourFromBtoA(parent_node[0], parent_node[1]))
    child_nodes.add(operator.pourFromAtoB(parent_node[0], parent_node[1]))
    child_nodes.add(operator.emptyA(parent_node[0], parent_node[1]))
    child_nodes.add(operator.emptyB(parent_node[0], parent_node[1]))

    # Removing parent node and (0,0) nodes from child_nodes list
    if (0, 0) in child_nodes:
        child_nodes.remove((0, 0))
    if (parent_node[0], parent_node[1]) in child_nodes:
        child_nodes.remove((parent_node[0], parent_node[1]))

    parent_node = [node_id, parent_id, x, y]

    # Reformat each node to have a id and a parent_id (node_id)
    formatted_child_node_list = list()
    for node in child_nodes:
        node = list(node)
        i = i + 1
        child_count = child_count + 1
        node.insert(0, child_count)
        node.insert(1, node_id)
        formatted_child_node_list.append(node)

    # Adding to the Graph as a Key Value Pair
    graph[str(list(parent_node))] = formatted_child_node_list

def populate_graph(x, y):
    add_new_node(0, 'root', x, y)
    current_node = str([0, 'root', x, y])
    visited_keys = list()
    visited_keys.append(current_node)
    k = 0
    for node in visited_keys:
        for states in graph[node]:
            add_new_node(states[0], states[1], states[2], states[3])
            new_node = str([states[0], states[1], states[2], states[3]])
            if new_node not in visited_keys:
                visited_keys.append(str([states[0], states[1], states[2], states[3]]))
        if k == const.MAX_ITERATIONS:
            break
        k = k + 1


def search_graph():
    print("\nThe solutions are printed in (x, y) format where x is the state of Jug A "
          "and y is the state of Jug B. \nOn each line, the state change is indicated from left to right.", end="\n\n")
    solution_count = 0
    for key_node in graph:
        for child_node in graph[key_node]:
            if child_node[2] == 2 and child_node[3] == 0:
                global search_result
                search_result = []
                search_result[:0] = [(child_node[2], child_node[3])]
                find_parents(child_node[1])
                search_result[:0] = [(0, 0)]
                solution_count = solution_count + 1
                print(search_result)

    print("\nNumber of Solutions where x=2 are", solution_count, "in", const.MAX_ITERATIONS," iterations.\n"
        "Increase MAX_ITERATIONS in constants to increasee depth of graph.")

def find_parents(parent_id):
    for x in graph:
        for x in graph[x]:
            if x[0] is parent_id:
                search_result[:0] = [(x[2], x[3])]
                find_parents(x[1])
_name_="_main_"
if _name_ == "_main_":

    A = const.JUG_A_MAX_CAPACITY     # Maximum volume of Jug A
    B = const.JUG_B_MAX_CAPACITY     # Maximum volume of Jug B
    x = const.JUG_A_START_STATE      # Start volume of Jug A
    y = const.JUG_A_START_STATE      # Start volume of Jug B

    operator = operations(A, B)
    populate_graph(x, y)
    search_graph()
