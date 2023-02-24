class MinMax():

    def __init__(self, tree):

        self.tree = tree
        self.generateMinMaxTree(self.tree)

    def generateMinMaxTree(self, tree):

        value = self.maxValue(tree.root)

        tree.root.data.point = value

    def maxValue(self, node):

        if(node.data.is_final):

            self.setPoints(node)

            return node.data.point

        
        value = float("-inf")

        
        for children in node.children:
            value = max(value, self.minValue(children))

        node.data.point = value

        return value

    def minValue(self, node):

        if(node.data.is_final):

            self.setPoints(node)

            return node.data.point

        value = float("inf")

        
        for children in node.children:

            value = min(value, self.maxValue(children))

        node.data.point = value

        return value 


    # TO IMPLEMENT 
    def setPoints(self, node):
        pass 

    def getMove(self, node):
        pass 