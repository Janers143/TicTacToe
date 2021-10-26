from board import Board
from game  import Game

if __name__=="__main__":

    g = Game()
    move = g.get_move_text('X')
    print("The move received is: " + str(move))