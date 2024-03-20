"""
This class is responsible for storing all the information about current state of the chess game. It will also be
responsible for determining valid moves at the current state. It will also keep a move log.
"""

class GameState():
    def __init__(self):
        # board is a 8*8 2d list . each element has 2 character.
        # first character means color. 2nd character piece name.
        # for example: bQ = black Queen
        # "--" represents empty space with no piece

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

        self.whiteMove = True
        self.moveLog = []