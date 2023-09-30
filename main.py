
from search import *

class WolfGoatCabbage(Problem):
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial = "WGCF", goal=""):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        super().__init__(initial, goal)
  
    
    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""

        validActions = []
        
        #create temp set because sets are not mutable during iteration.
        tempSet = state

        # Farmer is on the left side of the river
        if 'F' in state:
            tempSet = tempSet.replace('F', "")
            state = state.replace('F', "")         
            for char in state:
                tempSet = tempSet.replace(char, "")    
                if self.validState(tempSet) and char != 'F': 
                    
                    validActions.append(tempSet)
                tempSet+=char
                


        # Farmer is on the right side of the river
        else:
            differenceStates = "GCW"
            if len(differenceStates)>len(state): 
                res=''.join(differenceStates.split(state))             #get diff
            else: 
                res=''.join(state.split(differenceStates))             #get diff
            
            tempSet+='F'
            for char in res:
                res = res.replace(char, "")
                tempSet+=char
                if self.validState(tempSet) and self.validState(res):
                     
                    
                    validActions.append(tempSet)
                tempSet = tempSet.replace(char, "")
                res += char 
            tempSet+= 'F'


            #test case for moving only the farmer
       
            if self.validState(tempSet) and self.validState(res):
                tempSet = tempSet[:-1] 
                validActions.append(tempSet)

        #printing out the valid actions 
        #print(validActions)
        return validActions

    def result(self, state, action):
        return action

    def validState(self, state):
        if 'W' in state and 'G' in state:
            if 'F' in state: 
                return True
            else:
                return False 
        if 'G' in state and 'C' in state: 
            if 'F' in state: 
                return True
            else:
                return False
        return True

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""

        return state == self.goal
if __name__ == '__main__':

    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)


