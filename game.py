import board

class Game:

    """
    A class used to represent a Game

    Attributes
    ----------
    board : Board -
        The current board in the game

    moves : list -
        The list of all the moves played

    Methods
    -------
    
    """

    def __init__(self, board_size = 3):
        '''
        Constructor for the Game object

        Parameters
        ----------
        board_size : int, optional -
            The number of rows and columns of the board (can be 3, 4, ...)

        Returns
        -------
        Game - The Game 
        '''
        super().__init__()

        self.board = board.Board(board_size, [], [])
        self.moves = []

    def get_move_text(self, player):
        print("Player " + player + " turn to move...")
        
        line = input("Enter the line you want to play (and press Enter) : ")
        try:
            line = int(line) - 1
        except:
            line = -1
        
        valid = (line >= 0 and line < self.board.nb_rows)
        while (not valid):
            print("You should enter a number between 1 and " + str(self.board.nb_rows))
            line = input("Enter the line you want to play (and press Enter) : ")
            try:
                line = int(line) - 1
            except:
                line = -1
        
            valid = (line >= 0 and line < self.board.nb_rows)
        
        column = input("Enter the column you want to play (and press Enter) : ")
        try:
            column = int(column) - 1
        except:
            column = -1
        
        valid = (column >= 0 and column < self.board.nb_rows)
        while (not valid):
            print("You should enter a number between 1 and " + str(self.board.nb_rows))
            column = input("Enter the column you want to play (and press Enter) : ")
            try:
                column = int(column) - 1
            except:
                column = -1
        
            valid = (column >= 0 and column < self.board.nb_rows)

        print("The player " + str(player) + " has chosen to play (" + str(line+1) + ", " + str(column+1) + ")")
        return (line,column)
