
from .state import State
from .tree_node import TreeNode
from .tree import Tree

class TicTacToeTree():

    count_move = 0

    def __init__(self):
        initial_configuration = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        initial_state = State(initial_configuration, 0)


        node = TreeNode(data=initial_state, parent=None, children=[])

        self.tree = Tree(root=node)

        self.generateGameTree(self.tree)


    def generateGameTree(self, tree):

        currentNode = tree.root

        self.updateChildren(currentNode)

    
    def updateChildren(self, node):

        if(node.parent == None):
            self.count_move = 1
        else:
            if(node.min_max_value == 1):
                self.count_move = 2
            elif(node.min_max_value == 2):
                self.count_move = 1

        if(node.children == None):
            return

        root_configuration = node.data.getConfiguration()
        winner = self.checkIfWin(root_configuration)

        if(winner != 0):

            node.data.is_final = True
            node.data.winner = winner
            return


        possible_configuration = self.generatePossibleConfiguration(root_configuration, self.count_move)

        if(len(possible_configuration) == 0):
            node.children = None
            node.data.is_final = True
        else:

            for move in possible_configuration:

                state = State(move, 0)
                temp_node = TreeNode(data=state, parent=node, children=None)
                temp_node.min_max_value = self.count_move
                node.children.append(temp_node)

                

            
            for child_node in node.children:

                self.updateChildren(child_node)


    def generatePossibleConfiguration(self, source, marca):

        all_configuration = []
        count = 0

        for value in source:

            if(value == 0):

                new_configuration = [v for v in source]
                new_configuration[count] = self.count_move
                all_configuration.append(new_configuration)

            count += 1

        return all_configuration


    def checkIfWin(self, configuration):

        if (configuration[0] == 1 and configuration[1] == 1 and configuration[2] == 1): return 1
        elif (configuration[0] == 2 and configuration[1] == 2 and configuration[2] == 2): return 2
        elif (configuration[3] == 1 and configuration[4] == 1 and configuration[5] == 1): return 1
        elif (configuration[3] == 2 and configuration[4] == 2 and configuration[5] == 2): return 2
        elif (configuration[6] == 1 and configuration[7] == 1 and configuration[8] == 1): return 1
        elif (configuration[6] == 2 and configuration[7] == 2 and configuration[8] == 2): return 2
        elif (configuration[0] == 1 and configuration[3] == 1 and configuration[6] == 1): return 1
        elif (configuration[0] == 2 and configuration[3] == 2 and configuration[6] == 2): return 2
        elif (configuration[1] == 1 and configuration[4] == 1 and configuration[7] == 1): return 1
        elif (configuration[1] == 2 and configuration[4] == 2 and configuration[7] == 2): return 2
        elif (configuration[2] == 1 and configuration[5] == 1 and configuration[8] == 1): return 1
        elif (configuration[2] == 2 and configuration[5] == 2 and configuration[8] == 2): return 2
        elif (configuration[0] == 1 and configuration[4] == 1 and configuration[8] == 1): return 1
        elif (configuration[0] == 2 and configuration[4] == 2 and configuration[8] == 2): return 2
        elif (configuration[2] == 1 and configuration[4] == 1 and configuration[6] == 1): return 1
        elif (configuration[2] == 2 and configuration[4] == 2 and configuration[6] == 2): return 2
        else: return 0




