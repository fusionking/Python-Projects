####################################################################################

import math, cmath

################# CAN ARSOY 18076 ######################

class Problem(object):
    """The abstract class for a formal problem."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal."""
        self.initial = []
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. """
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state."""
        raise NotImplementedError

    def goal_test(self, key):
        """Return True if the state is a goal. """
        if key == 'G':
            return True
        else:
            return False

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1."""
        return c + 1

    def value(self, state):

        raise NotImplementedError

    def calculate_path_cost(self, x1, y1, x2, y2, x1d, y1d, x2d, y2d):
        """Calculates the distance between two points."""
        distance = abs(x1 - x1d) + abs(y1 - y1d) + abs(x2 - x2d) + abs(y2 - y2d)
        if distance == 1:
            return distance
        else:
            if x1 == x1d and x2 == x2d and y1 == y2 and y1d == y2d and y1d == y1+1:
                return 1
            else:
                return distance

    def heuristic(self, x2, y2, x2d, y2d):
        """The heuristic function of A*. It calculates the hypotenuse between two given points"""
        h_distance = math.sqrt(math.pow((x2d - x2), 2) + math.pow((y2d - y2), 2))
        print "Hypotenuse of " + str(x2) + " " + str(y2) + " " + str(x2d) + " " + str(y2d) + " = " + str(h_distance)
        return h_distance

# ______________________________________________________________________________
