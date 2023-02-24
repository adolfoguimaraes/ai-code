from flask import Flask
from flask_cors import CORS

from flask import jsonify, request

from minimax import minmax_tictactoe
from minimax.tictactoe_tree import TicTacToeTree


app = Flask(__name__)
CORS(app)

tree_ = TicTacToeTree().tree
minmax_ = minmax_tictactoe.TicTacToeProblem(tree_)


@app.route('/')
def home():

    return "use endpoint /minimax/play/ to get a game move"



@app.route('/minimax/play/', methods=['POST'])
def minmax_play():

    data_json = request.get_json() or None
    
    if data_json is None:
        return {
            'status': 500,
            'msg': 'Please pass a json like described in API documentation.'
        }

    
    data_game = data_json.get('game', None)

    if data_game is None:
        return {
            'status': 500,
            'msg': 'Please pass a json with a key game with a board game information. See documentation.'
        }

    move = minmax_.getMove(data_game)

    if move is None: 
        return {
            'status': 500,
            'msg': 'Invalid move'
        }
    
    return_  = {
        'status': 200,
        'move': move
    }

    return jsonify(return_)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5001, debug=True)