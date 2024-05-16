# TicTacToe-AI
This is a Tic Tac Toe AI that uses Minimax Algorithm. I had used pygame to display the game. After the player picks their move, the recursive minimax algorithm goes through all possible moves or at least till it hits a recursive limit, which is crucial with games with more squares, and builds a tree of rewards. It then selects a random move from the list of moves that gives the  maximum reward for the computer. The game is built in a way that it can adapt to different screen sizes, number of squares (like 4x4 or 5x5), or colors. Using this as a base, we can make other variations of tic-tac-toe like Misere (where the player loses when they make n-in-a-row)

Game.py -> Main Tic Tac Toe game against AI

Misere.py -> Misere Tic Tac Toe game against AI

Circle.png and Cross.png -> Images

Controls:
Use mouse to click, and 'r' to restart the game at any point.
Number of squares for the game can be changed within the code in the beginning of the code with the integer variable "SQUARES". Same for other specific parameters.
