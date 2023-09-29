from search import *

# state by a set of characters, {F,G} implies wolf and cabbage on right
# An action in this puzzle is 1-2 objects crossing  {STUFF CROSSING}
# WINNING STATES IN ORDER
# [{'G', 'F'},
# {'F'},
# {'W', 'F'},
# {'G', 'F'},
# {'C', 'F'},
# {'F'},
# {'G', 'F'}]


class WolfGoatCabbage(Problem):
    
    def __init__(self, initial, goal=({})): #goal is empty, because that's what is on the left
        super().__init__(initial, goal)

    def actions(self, state):

        possible_actions = ['LEFT', 'RIGHT']

        # find the possible actions given the state

        return possible_actions

    def result(self, state, action):
        new_state = None

        # find the best new state

        return tuple(new_state)

    def goal_test(self, state):
        return state == self.goal


if __name__ == '__main__':

    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
