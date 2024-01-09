#STUDENT NAME: Tiago Silva Pereira
#STUDENT NUMBER: 98360

#DISCUSSED TPI-1 WITH: (names and numbers):


from tree_search import *
import math

class OrderDelivery(SearchDomain):

    def __init__(self,connections, coordinates):
        self.connections = connections
        self.coordinates = coordinates
        # ANY NEEDED CODE CAN BE ADDED HERE
        
    def actions(self,state):
        city = state[0]
        actlist = []
        for (C1,C2,D) in self.connections:
            if (C1==city):
                actlist += [(C1,C2)]
            elif (C2==city):
               actlist += [(C2,C1)]
        return actlist 

    def result(self,state,action):
        if state == action[0]:
            return  action[1] 
        

    def satisfies(self, state, goal):
        return state[0] == goal  
        

    def cost(self, state, action):
        if state != action[0]:
            return float('inf')
        for (C1, C2, D) in self.connections:
            if (C1 == state and C2 == action[1]) or (C2 == state and C1 == action[1]):
                return D  
        return float('inf')  


    def heuristic(self, state, goal):
 
        if state != None:
            a = self.coordinates.get(state)
            b = self.coordinates.get(goal)
            x1, y1 = a
            x2, y2 = b
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        


 
class MyNode(SearchNode):

    def __init__(self,state,parent = None,heuristic = None,cost = 0,depth = 0):
        super().__init__(state,parent)
        self.state = state
        self.heuristic =heuristic
        self.cost = 0
        self.eval = 0
        self.depth = 0
        self.parent = parent
        self.marked_for_deletion = False
        

class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth',maxsize=None):
        super().__init__(problem,strategy)
        #ADD HERE ANY CODE YOU NEED
        self.terminals = 0
        self.non_terminals = 0
        self.depth = 0
        self.solution = None
        root_heuristic = problem.domain.heuristic(problem.initial, problem.goal)
        root = MyNode(problem.initial, None, root_heuristic, 0)
        self.open_nodes = [root]
        self.maxsize = maxsize

    def astar_add_to_open(self,a):
        #IMPLEMENT HERE
        self.open_nodes.extend(a)
        return sorted(self.open_nodes, key=lambda node: node.cost + node.heuristic)

    def search2(self):
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)

            if self.problem.goal_test(node.state):
                self.solution = node
                self.terminals = len(self.open_nodes) + 1
                return self.get_path(node)
            
            self.non_terminals += 1
            lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state, a)
                if newstate not in self.get_path(node) and newstate != None:
                    newnode = MyNode(newstate,node, node.heuristic)
                    newnode.cost = node.cost + self.problem.domain.cost(node.state, a)
                    newnode.heuristic = self.problem.domain.heuristic(newstate, self.problem.goal)
                    newnode.depth = node.depth + 1
                    newnode.eval = newnode.cost + newnode.heuristic
                    #print(node.eval)
                    lnewnodes.append(newnode)
                # print('op',len(self.open_nodes))
            self.add_to_open(lnewnodes)
            print('len1', len(self.open_nodes))
            print('lennewnodes', len(lnewnodes))
            if self.strategy == 'A*' and self.maxsize is not None and (self.non_terminals + 1 + len(self.open_nodes)) > self.maxsize:
                    print('a')
                    self.open_nodes = self.manage_memory()
                    print('len2', len(self.open_nodes))

        return None
        
                 
    def manage_memory(self):
        #IMPLEMENT HERE
        parents = []
        marked_nodes = []

        for node in reversed(self.open_nodes):
            print('a')
            if node not in marked_nodes and node.parent is not None:
                siblings = [n for n in self.open_nodes if n.parent == node.parent]
                node_eval = min([n.eval for n in siblings])
                node.parent.eval = node_eval
                parents.append(node.parent)
                marked_nodes.extend(siblings)

 
        for node in marked_nodes:
            self.open_nodes.remove(node)   

        for parent in parents:
            self.open_nodes.append(parent)  

        return self.open_nodes
         
    # if needed, auxiliary methods can be added here

def orderdelivery_search(domain,city,targetcities,strategy='breadth',maxsize=None):
# (self, domain, initial, goal)
    targetcities.append(city)
    n = []
    path = []
    for a in targetcities:
        problem = SearchProblem(domain,city, a)
        tree = MyTree(problem, strategy=strategy, maxsize=maxsize)
        path.extend(tree.search2())
        n.append(tree.solution)
        city = a

    
    return (tree,path)
 

# If needed, auxiliary functions can be added here



