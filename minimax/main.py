
from minimax import MinMax



minmax_ = MinMax()
minmax_tree = minmax_.tree

move = minmax_.getMove([1, 2, 0, 0, 1, 0, 0, 0, 0])
print(move)
move = minmax_.getMove([1, 2, 2, 0, 1, 0, 0, 0, 0])
print(move)