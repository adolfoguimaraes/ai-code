

class State():

    table_configuration = []
    point = 0
    is_final = False
    winner = 0

    def __init__(self, configuration, point):

        self.table_configuration = configuration
        self.point = point

    def setMove(self, position, value):

        self.table_configuration[position] = value

    def getConfiguration(self):
        
        return self.table_configuration




