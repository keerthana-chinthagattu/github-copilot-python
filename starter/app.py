from flask import Flask, jsonify, render_template, request
import sudoku_logic

app = Flask(__name__)

game_state = {
    "puzzle": None,
    "solution": None
}


def start_new_game(clues):
    puzzle, solution = sudoku_logic.generate_puzzle(clues)
    game_state["puzzle"] = puzzle
    game_state["solution"] = solution
    return puzzle


def compare_with_solution(board, solution):
    wrong_cells = []

    for row_index, row in enumerate(board):
        for col_index, value in enumerate(row):
            if value != solution[row_index][col_index]:
                wrong_cells.append([row_index, col_index])

    return wrong_cells


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/new")
def create_game():
    try:
        clues = int(request.args.get("clues", 35))

        if not 17 <= clues <= 81:
            return jsonify({
                "error": "Clues must be between 17 and 81."
            }), 400

        puzzle = start_new_game(clues)

        return jsonify({"puzzle": puzzle})

    except (TypeError, ValueError):
        return jsonify({
            "error": "Invalid puzzle settings."
        }), 400


@app.route("/check", methods=["POST"])
def verify_game():
    if game_state["solution"] is None:
        return jsonify({
            "error": "Start a new game before checking the solution."
        }), 400

    payload = request.get_json(silent=True)

    if not payload or "board" not in payload:
        return jsonify({
            "error": "No Sudoku board was provided."
        }), 400

    board = payload["board"]

    if not isinstance(board, list) or len(board) != sudoku_logic.SIZE:
        return jsonify({
            "error": "Invalid Sudoku board."
        }), 400

    try:
        for row in board:
            if not isinstance(row, list) or len(row) != sudoku_logic.SIZE:
                raise ValueError

        wrong_cells = compare_with_solution(
            board,
            game_state["solution"]
        )

        return jsonify({"incorrect": wrong_cells})

    except (TypeError, ValueError):
        return jsonify({
            "error": "The submitted Sudoku board is invalid."
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
