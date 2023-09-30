from search import *
# YOUR CODE GOES HERE


def frozen_helper(frznset):
    result = ""
    for x in frznset:
        result += x
    return result


class WolfGoatCabbage(Problem):
    def __init__(self, initial=frozenset(["W", "F", "G", "C"]), goal={}):
        super().__init__(initial, goal)

        self.possible_actions = [
                'GF',
                'CF',
                'WF',
                'F'
                ]
        # cw, fcw, c, w, fgw, fcg, g,
        self.states = {
                'CFGW': [0],
                'CFG': [1,2],
                'FGW': [0, 2],
                'FG': [0, 3],
                'CW': [0,3],
                'W': [0, 1],
                'G': [1, 2, 3],
                'C': [0, 2],
                '': [0, 1, 2, 3],
                }

    def actions(self, state):
        stringSet = frozen_helper(state)
        actionIndexes = self.states[''.join(sorted(stringSet))]
        result = list()
        for index in actionIndexes:
            result.append(self.possible_actions[index])
        return frozenset(result)

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        print("STATE",state)
        print("ACTION",state)
        print("TYPE",type(action))
        return frozenset(action) # turn into frozenset

    def goal_test(self, state):
        return state == self.goal

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
