
class TreeNode:

    data = None
    parent = None
    children = None
    min_max_value = 0

    def __init__(self, data=None, parent=None, children=None): 
        self.data = data
        self.parent = parent
        self.children = []

        
    def insertChild(self, child):

        child.parent = self
        self.children.append(child)

    def getHeight(self):
        height = 1
        current = self

        while(current.parent):

            height += 1
            current = current.parent

        return height
    
