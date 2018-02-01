from graph import *
from numpy import matrix
from problem import *
from queue import *
from memory_profiler import profile
import time
from functools import wraps

################# CAN ARSOY 18076 ######################

def fn_timer(function):
    """Calculates the running time of a function"""
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
               (function.func_name, str(t1 - t0))
               )
        print ""
        return result

    return function_timer


def matrix_generation():
    """Forms the game matrix"""
    bloxorz_map = [
        ['()', '()', '()', 'X', '()', 'X', 'X', 'X'],
        ['()', '()', '()', '()', '()', '()', 'G', 'X'],
        ['X', 'X', '()', 'X', '()', '()', '()', '()'],
        ['S', 'S', '()', 'X', 'X', 'X', '()', '()']]
    return bloxorz_map


def add_pos_to_graph(graph, element, bloxorz_map):
    """Adds matrix points to the graph.
        It iterates over the whole game matrix.
        For each point, it inspects whether it is reachable.
        If it is labeled as X, its reachable field in the graph constructor becomes false
        Otherwise, we add 3 possible orientations of the block to the graph:
        1) i,k i,k means that the block stands in a vertical orientation
        2) i,k i+1 k means that the block stands horizontal in north-south orientation
        3) i,k i, k+1 means that the block stands horizontal in east-west orientation
        This means that all possible orientations of the block are added as nodes to the graph."""
    for i, j in enumerate(bloxorz_map):
        for k, l in enumerate(j):
            if l == element:
                if l == 'X':
                    graph.addNode(element, i, k, i, k, 0, False)

                else:
                    graph.addNode(element, i, k, i, k, 0, True)
                    graph.addNode(element, i, k, i + 1, k, 0, True)  # horizontal NORTH-SOUTH orientation
                    graph.addNode(element, i, k, i, k + 1, 0, True)  # horizontal east-west orientation


def return_block_points(block_points):
    """Returns the starting points of our block.
        It iterates over the whole game matrix to find an entry labeled 'S' and returns its coordinates"""
    for i, j in enumerate(bloxorz_map):
        for k, l in enumerate(j):
            if l == 'S':
                block_points.append(i)
                block_points.append(k)
    return block_points


@fn_timer
def astar_search(problem, frontier_list):
    """
        This implementation is the clone of A* search.
        Search the nodes with the lowest g+h scores first.
        F here is node.path_cost since we are trying to optimize the cost
        to get to the goal node.
        For each child of our block, we iterate over them one by one
        and add each one at a time to the frontier.
        If the current inspected node has a lower path cost than its parent,
        the parent is discarded from the frontier and the child is added.
        """
    node = Node(problem.initial[0], problem.initial[1], problem.initial[2], problem.initial[3], problem.initial[4], 0,
                True)
    if problem.goal_test(node.key):
        return node
    frontier = PriorityQueue(min, f=lambda x: x)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        frontier_list.append(node)
        if problem.goal_test(node.key):
            return node
        explored.add(node)
        for child in graph.nodes[
            problem.initial[0], problem.initial[1], problem.initial[2], problem.initial[3], problem.initial[
                4], 0, True].successors:
            if child not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if child.path_cost < incumbent.path_cost:
                    del frontier[incumbent]
                    frontier.append(child)
    return None


if __name__ == '__main__':

    bloxorz_map = matrix_generation()
    frontier_list = []

    problem = Problem(None, None)
    graph = Graph()
    node = Node(None, None, None, None, None, 0, False)

    block_points = []
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0

    posX = 0
    posY = 0
    posX2 = 0
    posY2 = 0

    key_dest = None
    reachable = False

    node_info = []

    for i, j in enumerate(bloxorz_map):
        for k, l in enumerate(j):
            add_pos_to_graph(graph, l, bloxorz_map)

    block_points = return_block_points(block_points)
    start_x = block_points[0]
    start_y = block_points[1]
    if (block_points == 4):
        end_x = block_points[2]
        end_y = block_points[3]
    else:
        end_x = start_x
        end_y = start_y

    problem.initial = ['S', start_x, start_y, end_x, end_y, 0, True]

    for n in graph.getNodes():

        key_dest = n[0]
        posX = n[1]
        posY = n[2]
        posX2 = n[3]
        posY2 = n[4]
        reachable = n[6]

        distance = problem.calculate_path_cost(start_x, start_y, end_x, end_y,
                                               posX, posY, posX2, posY2)
        h_distance = problem.heuristic(end_x, end_y, posX2, posY2)
        total_distance = distance + h_distance

        if reachable == True:
            graph.connect('S', start_x, start_y, end_x, end_y,
                          key_dest, posX, posY, posX2, posY2)

        graph.updateGraph(graph, key_dest, posX, posY, posX2, posY2, 0, reachable, total_distance)

    result_node = astar_search(problem, frontier_list)
    print "Most efficient path... "
    print str(result_node.key) + " " + str(result_node.posX) + " " + str(result_node.posY) + " " + str(
        result_node.posX2) + \
          " " + str(result_node.posY2) + " " + str(result_node.path_cost)

    print ""
    for item in frontier_list:
        print str(item.key) + " " + str(item.posX) + " " + str(item.posY) + " " + str(item.posX2) + " " + str(
            item.posY2) + " COST: " + str(item.path_cost)
        print ">>>"
