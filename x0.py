from board import *

# did not substract 1 from position, size and goal... they are counted from 1!
def main():
    player_names = [input("First challenger, name yourself!\n"), input("Their opponent is known as the mighty...:\n")]
    for player in player_names: 
        if player == "":
            player_names[player_names.index(player)] = f"Player{player_names.index(player)+1}"
    size = input("Set up the arena size: ")
    if size != "": size = abs(int(size))
    icon = input("And the terrain: ")
    goal = input("Set the win condition (length of uninterrupted repeating player symbols): ")
    if goal != "": goal = abs(int(goal))
    if goal > size: goal = size
    
    play_again = "y"
    

    
    score_board = {}
    recorded_games = []
    
    game = Board(size, goal, icon)
    round_count = 1
    
    while play_again == "y":
        play_again = "n"
        game.play_game(game, player_names)
        play_again = input("Rematch? (y/n): ")
        if play_again != "y" and play_again != "n":
            print(f"You've played for {round_count} rounds. But now it's...")
            print("Game over...")
            break
        if play_again == "y":
            round_count += 1
            game = Board(size, goal, icon)
        else:
            print(f"You've played for {round_count} rounds. We await your return.")
            
            

main()
                
            
    
        
    