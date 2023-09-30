from search import Problem, depth_first_graph_search, breadth_first_graph_search

class WolfGoatCabbage(Problem):
    def __init__(self, initial='CGWF', goal=''):
        super().__init__(initial, goal)
        self.possible_actions = [
            'GF',
            'CF',
            'WF',
            'F'
        ]
        self.states = {
            'CGWF': [0, 1, 2, 3],
            'CGW': [3],
            'CGF': [0, 1, 3],
            'GF': [0, 3],
            'WF': [2, 3],
            'CW': [3],
            'F': [3]
        }

    def actions(self, state):
        print("actions called")
        print("STATE", state)
        actionIndexes = self.states[state]
        print("ACTION INDEXES", actionIndexes)
        result = list()
        for index in actionIndexes:
            result.append(self.possible_actions[index])
        return result

    def result(self, state, action):
        print("result called")
        new_state = list(state)

        if action == 'GF' and 'G' in state and 'F' in state:
            new_state.remove('G')
            new_state.remove('F')
        elif action == 'CF' and 'C' in state and 'F' in state:
            new_state.remove('C')
            new_state.remove('F')
        elif action == 'WF' and 'W' in state and 'F' in state:
            new_state.remove('W')
            new_state.remove('F')
        elif action == 'F' and 'F' in state:
            new_state.remove('F')
        result = ""
        for char in new_state:
            result += char
        return result

    def goal_test(self, state):
        print("goal_test called")
        return state == self.goal


if __name__ == '__main__':
    initial_state = 'CGWF'
    goal_state = ''
    wgc = WolfGoatCabbage(initial=initial_state, goal=goal_state)
    solution = depth_first_graph_search(wgc).solution()
    print("Solution using Depth-First Search:", solution)
    solution = breadth_first_graph_search(wgc).solution()
    print("Solution using Breadth-First Search:", solution)

