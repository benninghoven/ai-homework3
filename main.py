from search import *

# code goes here

class WolfGoatCabbage:
    def __init__(self):
        self.test = "test"
    def solution(self):
        return "solution"



# code ends here

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)

