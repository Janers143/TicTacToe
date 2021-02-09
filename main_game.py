import board
import game

if __name__=="__main__":

    g = game.Game()
    move = g.get_move_text('X')
    print("The move received is: " + str(move))