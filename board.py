class Board:
    
    common_commands = [
        "scoreboard", 
        "show board", 
        "rules"
        ]
    
    
    
    def __init__(self, size, goal, icon):
        if size != "": self.size = abs(int(size)) 
        else: self.size = 3
        if goal != "": self.goal = abs(int(goal))
        else: self.goal = 3
        if icon == "":
            self.icon = "🚩"
        else: self.icon = icon 
        if self.icon == "X" or self.icon == "0": 
            self.icon = "😈" 
            print(f'\033[1;91m{"You scoundrel!"}\033[0m')
        self.board = [[[self.icon] for i in range (self.size)] for k in range(self.size)]
        
        self.turn_counter = 1
        self.player_symbol = {}
        self.end = False       
        
        
        
    def rules(self):
        print(f"Board size is {self.size}x{self.size}.\nThe goal is to paint {self.goal} consecutive panels in your symbol!")
        print(f"Take turns until one of you succeeds. If you run out of space, it's a draw. Good luck!")
        pass    
    
    def show_board(self):
        for item in self.board:
            print(item, sep="\n")
        
    def get_board(self):
        return(self.board)
    
    def check_victory(self, symbol):
        if self.turn_counter > 2:
            match symbol:
                case "X"|"0":
                    #vertical check
                    for row in self.board:
                        new_row = "".join(map("".join, row))
                        if self.goal * symbol in new_row:
                            return True
                    #horizontal check
                    transpose_board = [[self.board[j][i] for i in range(self.size)] for j in range(self.size)]
                    for row in transpose_board:
                        new_row = "".join(map("".join, row))
                        if self.goal * symbol in new_row:
                            return True
                    for i in range(self.size):
                        for j in range(self.size):
                            target = [1, 1]
                            if self.board[i][j][0] == symbol:
                                if self.size - i >= self.goal and self.size - j >= self.goal:
                                    for k in range(self.goal - 1):
                                        if self.board[i+k+1][j+k+1][0] == symbol:
                                            target[0] += 1    
                                    if target[0] == self.goal:
                                        return True
                                    target[0] = 1
            
                                if i - self.size >= self.goal and self.size - j >= self.goal:
                                    for k in range(self.goal - 1):
                                        if self.board[i-k-1][j+k+1][0] == symbol:
                                            target[1] += 1    
                                    if target[1] == self.goal:
                                        return True
                                    target[1] = 1 
                            
                case _:
                    raise NameError("Wrong input")
                
        return False
    
    def victory(self, player):
        print(f"Congrats on winning the round in {self.turn_counter} turns, mighty {player}!")
        #write stats into scoreboard, record game
        self.turn_counter = 1
        self.player_symbol = {}
        self.show_board()
        self.end = True
        
        
    def conditional_reverse(self, list_of_players:list, player: str) -> list : 
        if player == list_of_players[1]:
            return list_of_players[::-1]
        return list_of_players

    
    def put(self, symbol, position : tuple):
        if len(position) == 2:
            match symbol:
                case "X" | "0":
                    if self.board[position[0] - 1][position[1] - 1][0] == self.icon:
                        self.board[position[0] - 1][position[1] - 1][0] = symbol
                        print(f"Move successful, position {position} successfully painted {symbol}")
                        if self.check_victory(symbol):
                            self.victory(self.player)
                        
                    elif self.board[position[0] - 1][position[1] - 1][0] == symbol:
                        print(f"You already claimed this panel. Choose more wisely!")
                        self.play_game(self.game, self.conditional_reverse(self.player_names, self.player))
                    else:
                        print(f"This position is already claimed by your opponent! Think again!")
                        self.play_game(self.game, self.conditional_reverse(self.player_names, self.player))
                        
    
    def play_game(self, game: object , player_names: list):
        global common_commands
        self.game = game
        self.player_names = player_names
        
        while self.end == False:
            if self.player_symbol == {}:
                self.player_symbol = {player_names[0] : "X", player_names[1] : "0"}
            for player in player_names:
                self.player = player
                print(f"{player} chooses position:")
                position = (int(input("Row: ")), int(input("Column: ")))
                
                #self.check_commands(position)
        
                if type(position[0]) != int or type(position[1]) != int :
                    print(f"For position placement of your flag, you should pick integers from 1 to {self.size}!")
                    self.play_game(game, self.conditional_reverse(player_names, player))
                
                if abs(position[0]) > game.size or abs(position[1]) > game.size:
                    print("The position you've chosen is out of bounds, choose again!")
                    self.play_game(game, self.conditional_reverse(player_names, player))
                
                self.put(self.player_symbol[player], position)
                if self.end == True:
                    break
            self.turn_counter += 1
            
                    
                    

