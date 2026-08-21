# Sudoku Solver Web Application

A web-based Sudoku application built with **Python**, **Flask**, **HTML**, **CSS**, and **JavaScript**. The application generates playable Sudoku puzzles, lets users solve them interactively, and verifies whether the solution is correct.

## Project Overview

This project demonstrates how a Sudoku puzzle can be generated and solved using a backtracking algorithm. The backend is responsible for creating valid puzzles and checking solutions, while the frontend provides an interactive interface for players.

## Features

- Generate a new Sudoku puzzle
- Interactive 9×9 Sudoku board
- Validate completed solutions
- Randomized puzzle generation
- Responsive browser interface

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python     | Core programming language |
| Flask      | Backend web framework |
| JavaScript | Frontend interaction |
| HTML/CSS   | User interface |
| GitHub Copilot | Development assistance |

## Project Structure

```text
starter/
├── app.py                 # Flask application
├── sudoku_logic.py        # Puzzle generation and solving logic
├── templates/
│   └── index.html
├── static/
│   ├── main.js
│   └── style.css
└── requirements.txt
```

## How It Works

1. The Flask server creates a valid Sudoku board.
2. Numbers are removed to create a playable puzzle.
3. The puzzle is displayed in the browser.
4. The player fills the empty cells.
5. The solution is sent to the backend for validation.

## Installation

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Move into the project folder.

```bash
cd github-copilot-python
```

3. Install the required packages.

```bash
pip install -r starter/requirements.txt
```

4. Start the application.

```bash
cd starter
python app.py
```

5. Open your browser and visit:

```text
http://localhost:5000
```

## Learning Outcomes

Through this project I practiced:

- Building REST endpoints with Flask
- Implementing recursive backtracking algorithms
- Managing frontend and backend communication
- Creating an interactive web application
- Organizing a Python project using Git and GitHub

## Future Improvements

- Multiple difficulty levels
- Timer and scoring system
- Hint functionality
- Save and resume unfinished games

## Author

**Nikhitha Mateti**

Python | Flask | Web Development
