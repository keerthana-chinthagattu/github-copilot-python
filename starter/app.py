from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from sudoku_logic import generate_sudoku, check_solution

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/new", methods=["GET"])
def new_game():
    difficulty = request.args.get("difficulty", default=40, type=int)

    game = generate_sudoku(difficulty)

    return jsonify(
        {
            "board": game["board"],
            "solution": game["solution"],
        }
    )


@app.route("/check", methods=["POST"])
def verify_board():
    data = request.get_json()

    board = data.get("board", [])

    solved = check_solution(board)

    return jsonify(
        {
            "valid": solved,
            "message": "Correct solution" if solved else "Incorrect solution",
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
