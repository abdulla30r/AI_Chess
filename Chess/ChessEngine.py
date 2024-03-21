"""
This class is responsible for storing all the information about current state of the chess game. It will also be
responsible for determining valid moves at the current state. It will also keep a move log.
"""


class GameState():
    def __init__(self):
        # board is an 8*8 2d list . each element has 2 character.
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

    '''
    move a piece using move parameter. this will not work for pawn promotion, castling, en-passant
    '''
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"     # make blank in source
        self.board[move.endRow][move.endCol] = move.pieceMoved  # put piece in destination
        self.moveLog.append(move)   # log the move, so we can see history or undo move
        self.whiteMove = not self.whiteMove     # swap players

    '''
      undo the last move
    '''
    def undoMove(self):
        if len(self.moveLog) > 0:   # make sure there is a move to undo
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteMove = not self.whiteMove     # swap players


class Move():
    # maps keys to value
    # key : value
    # normally chess e vertical e 0-7 numbering kora. starting from white.
    # horizontal e a-h. called files. our board orders are not same. hence, mapping.
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}  # mapping dictionary
    rowsToRanks = {v: k for k, v in ranksToRows.items()}    # reverse a dictionary

    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}  # mapping dictionary
    colsToFiles = {v: k for k, v in filesToCols.items()}    # reverse a dictionary

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
