from wordle import Wordle

def run_game():
    game = Wordle()
    game.start()
    game.loop_phases()
    x = input("want to play again? YES/NO: ").upper()
    if x == "YES":
        run_game()
    else:
        print("okay, bye!")


if __name__ == "__main__":
    run_game()
    #game.result() #nothing in here yet
