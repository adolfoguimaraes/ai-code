
from .minmax_tictactoe import TicTacToeProblem
from .tictactoe_tree import TicTacToeTree



tree_ = TicTacToeTree().tree

minmax_ = TicTacToeProblem(tree_)

move = minmax_.getMove([1, 2, 0, 0, 1, 0, 0, 0, 0])
print(move)
move = minmax_.getMove([1, 2, 2, 0, 1, 0, 0, 0, 0])
print(move)