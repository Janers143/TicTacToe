class Board:

    """
    A class used to represent a Board

    Attributes
    ----------
    nb_rows : int -
        The number of rows and columns of the board (can be 3, 4, ...)

    board : matrix -
        The actual board with the plays by every player

    Methods
    -------
    getWinner()
        Gets the winner (if there is one) of the current board

    getMoves()
        Gets the moves from each of the players

    isComplete()
        Tells if the board is complete (i.e. there's no more empty squares)
    """

    def __init__(self, rows = 0, play_x = [], play_o = []):
        '''
        Constructor for the Board object 

        Parameters
        ----------
        rows : int, optional -
            The number of rows and columns of the board (can be 3, 4, ...)

        play_x : list, optional -
            A list of plays made by the player with crosses

        play_o : list, optional -
            A list of plays made by the player with circles

        Returns
        -------
        Board - The Board     
        '''
        super().__init__()

        if ((len(play_x) > len(play_o) + 1) or (len(play_o) > len(play_x))):
            raise Exception("Invalid arguments for play_x or play_o")
        if (len(play_x) > (rows*rows/2) + 1 or len(play_o) > (rows*rows/2) + 1):
            raise Exception("Too many plays made by one player")

        self.nb_rows = rows
        self.board = [[None for _ in range(self.nb_rows)] for _ in range(self.nb_rows)] 
        
        for move in play_x:
            x, y = move
            if ((x < 0 or x >= self.nb_rows) or (y < 0 or y >= self.nb_rows)):
                raise Exception("The move " + str(move) + " for player X is not possible.")
            elif (self.board[x][y] != None):
                raise Exception("There's already something in the square")
            else:
                self.board[x][y] = 'X'
                    
        for move in play_o:
            x, y = move
            if ((x < 0 or x >= self.nb_rows) or (y < 0 or y >= self.nb_rows)):
                raise Exception("The move " + str(move) + " for player O is not possible.")
            elif (self.board[x][y] != None):
                raise Exception("There's already something in the square")
            else:
                self.board[x][y] = 'O'

    def getWinner(self):
        '''
        Gets the winner (if there is one) of the current board

        Parameters
        ----------
        None

        Returns
        -------
        'X' if the X player has won, 'O' if the O player has won, None if no one has won yet
        '''
        x_wins = [True for _ in range(self.nb_rows * 2 + 2)]
        o_wins = [True for _ in range(self.nb_rows * 2 + 2)]
        for i, line in enumerate(self.board):
            for j, square in enumerate(line):
                # * Check for the lines
                x_wins[i] = (x_wins[i] and (square == 'X'))
                o_wins[i] = (o_wins[i] and (square == 'O'))
                # * Check for the columns
                x_wins[j+self.nb_rows] = (x_wins[j+self.nb_rows] and (square == 'X'))
                o_wins[j+self.nb_rows] = (o_wins[j+self.nb_rows] and (square == 'O'))
                # * Check for the diagonals
                if (i == j):
                    # * The square is in the left - right diagonal
                    x_wins[-2] = (x_wins[-2] and (square == 'X'))
                    o_wins[-2] = (o_wins[-2] and (square == 'O'))
                if (i + j == self.nb_rows - 1):
                    # * The square is in the right - left diagonal
                    x_wins[-1] = (x_wins[-1] and (square == 'X'))
                    o_wins[-1] = (o_wins[-1] and (square == 'O'))
        
        res = None
        if True in x_wins:
            res = 'X'
        if True in o_wins:
            res = 'O'
        return res

    def getMoves(self):
        '''
        Gets the moves from each of the players

        Parameters
        ----------
        None

        Returns
        -------
        A tuple with an array with x player's moves and an array with o player's move
        '''
        x_moves = []
        o_moves = []
        for i in range(self.nb_rows):
            for j in range(self.nb_rows):
                if (self.board[i][j] == 'X'):
                    x_moves.append((i,j))
                elif (self.board[i][j] == 'O'):
                    o_moves.append((i,j))
        return (x_moves, o_moves)

    def isComplete(self):
        '''
        Tells if the board is complete (i.e. there's no more empty squares)
        
        Parameters
        ----------
        None

        Returns
        -------
        A boolean value telling whether the board is complete or not
        '''
        complete = True
        for line in self.board:
            for square in line:
                if square == None:
                    complete = False
        return complete

    def __str__(self):
        '''
        Gives a string representing the board (useful for not using pygame)
        
        Parameters
        ----------
        None

        Returns
        -------
        A string representing the board
        '''
        res = ""
        for i, line in enumerate(self.board):
            for j, square in enumerate(line):
                if (square == None):
                    res += '   '
                else:
                    res += ' ' + square + ' '
                
                if j < self.nb_rows - 1:
                    res += '|'
                else:
                    res += '\n'
            
            if i < self.nb_rows - 1:
                for _ in range(self.nb_rows*4 - 1):
                    res += '-'
                res += '\n'

        return res

    def __repr__(self):
        return self.__str__()

    def __eq__(self, value):
        return (self.board == value.board and self.nb_rows == value.nb_rows)