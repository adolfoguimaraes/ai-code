
from .tictactoe_tree import TicTacToeTree
from random import randrange


class MinMax():


    def __init__(self):

        self.tree = TicTacToeTree().tree
        self.generateMinMaxTree(self.tree)


    def generateMinMaxTree(self, tree):

        value = self.maxValue(tree.root)

        tree.root.data.point = value

    def maxValue(self, node):

        if(node.data.is_final):

            if(node.data.winner == 1): node.data.point = 10
            elif(node.data.winner == 2):
                node.data.point = -10
            else: node.data.point = 0

            return node.data.point

        
        value = float("-inf")

        
        for children in node.children:
            value = max(value, self.minValue(children))

        node.data.point = value

        return value

    def minValue(self, node):

        if(node.data.is_final):

            if(node.data.winner == 1): node.data.point = 10
            elif(node.data.winner == 2): node.data.point = -10
            else: node.data.point = 0

            return node.data.point

        value = float("inf")

        
        for children in node.children:

            value = min(value, self.maxValue(children))

        node.data.point = value

        return value 

    def getMove(self, configuration):

        node = self.searchNode(self.tree.root, configuration)

        if node is None:
            return None

        children = node.children

        count = 0

        if(children):

            move = self.searchMove(children)

            move_id = -1


            for c in configuration:
                
                if(c != move.data.getConfiguration()[count]):

                    move_id = count
                    break

                count += 1

            
            if(move_id == 0): return (0, 0)
            elif(move_id == 1): return (0, 1)
            elif(move_id == 2): return (0, 2)
            elif(move_id == 3): return (1, 0)
            elif(move_id == 4): return (1, 1)
            elif(move_id == 5): return (1, 2)
            elif(move_id == 6): return (2, 0)
            elif(move_id == 7): return (2, 1)
            elif(move_id == 8): return (2, 2)


        return None

    def searchMove(self, list_):
        

        for element in list_:
            if(element.data.point == 10):
                return element


        list_zero = []
        for element in list_:
            if(element.data.point == 0):
                list_zero.append(element)
        

        if len(list_zero) > 0:
            return list_zero[randrange(len(list_zero))]
        else:
            return list_[0]

                
    def searchNode(self, node, configuration):

        

        if(node.data.table_configuration == configuration):

            return node 

        if(node.children):
            for child in node.children:

                search_node = self.searchNode(child, configuration)

                if(search_node):
                    return search_node

        
        return None 





        

