from search import *


class WolfGoatCabbage(Problem):

    def __init__(self, initial={'C', 'G', 'W', 'F'}, goal={}): #goal is empty, because that's what is on the left
        super().__init__(initial, goal)

    def actions(self, state):
        possible_actions = [
                {'G', 'F'},
                {'C', 'F'},
                {'W', 'F'},
                {'F'}
                ]

        states = {
                frozenset({'C', 'G', 'W', 'F'}): {0, 1, 2, 3},
                frozenset({'C', 'W', 'F'}): {1, 2, 3},
                frozenset({'C', 'G', 'F'}): {0, 1, 3},
                frozenset({'G', 'W', 'F'}): {0, 2, 3},
                frozenset({'G', 'F'}): {0, 3},
                frozenset({'W', 'F'}): {2, 3},
                frozenset({'C', 'F'}): {1, 3},
                frozenset({'C', 'W'}): {3}
                }

        actionIndexes = states[frozenset(state)]
        result = [possible_actions[i] for i in actionIndexes]
        return result

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
