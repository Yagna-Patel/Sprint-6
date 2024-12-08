from tkinter import *
from tkinter import messagebox
import random
import llm


#from tkmacosx import Button

# the game board class to handle the board logic like player switching, new game/restart. 
class board:
    def __init__(self, board_size = 8, game_mode = "Simple"):
        self.board_size = board_size
        self.board = [['' for _ in range(board_size)] for _ in range(board_size)]
        self.game_mode = game_mode
        self.player = "blue"
        self.blue_symbol = "S"
        self.red_symbol = "S"
        self.blue_points = 0
        self.red_points = 0

    def reset_game(self):

        self.game_mode.set(self.game_mode.get())
        self.blue_symbol.set("S")
        self.red_symbol.set("S")

        self.board = [[''for _ in range (self.board_size)] for _ in range(self.board_size)]
        self.player = "blue"

        self.blue_points = 0
        self.red_points = 0

    def switch(self): # this will simply switch players based on the current (red or blue) player.
        if self.player == "blue":
            self.player = "red"
        else:
            self.player = "blue"
            
    
# this will act as class fro win conditions and to solve my hiearchy problem.
class game_win_draw(board):
    
    def __init__(self, board_size = 8, game_mode = "Simple"):
        super().__init__(board_size, game_mode)
        
    def is_sos(self, row, col, board, buttons):
        self.board_size = len(board)
        symbol = board[row][col]
        sos_count = 0
        
        color = "green"

        # in this I couldn't figure out how to draw lines. I used a hihglighting method
        # source for this methic is codemy.com, sepcifically this video: Tic Tac Toe Game - Python Tkinter GUI Tutorial #113
        # Ik this needs to be reconfitured becaue it has so many reeating lines that can be made into functions that are dynamic
        if symbol == 'S':
            # check right and then it create the hihglihted to indicate lines.
            if col <= self.board_size - 3:
                if board[row][col+1] == 'O' and board[row][col+2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row][col+1].config(disabledforeground=color)
                    buttons[row][col+2].config(disabledforeground=color)
            
            # check left and then it create the hihglihted to indicate lines.
            if col >= 2:
                if board[row][col-1] == 'O' and board[row][col-2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row][col-1].config(disabledforeground=color)
                    buttons[row][col-2].config(disabledforeground=color)
            
            # check down and then it create the hihglihted to indicate lines.
            if row <= self.board_size - 3:
                if board[row+1][col] == 'O' and board[row+2][col] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col].config(disabledforeground=color)
                    buttons[row+2][col].config(disabledforeground=color)
            
            # check up and then it create the hihglihted to indicate lines.
            if row >= 2:
                if board[row-1][col] == 'O' and board[row-2][col] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row-1][col].config(disabledforeground=color)
                    buttons[row-2][col].config(disabledforeground=color)
                    
            # check to see if diagonal down-right
            if row <= self.board_size - 3 and col <= self.board_size - 3:
                if board[row+1][col+1] == 'O' and board[row+2][col+2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col+1].config(disabledforeground=color)
                    buttons[row+2][col+2].config(disabledforeground=color)
                    
            # check to see if diag right dwon
            if row >= 2 and col >= 2:
                if board[row-1][col-1] == 'O' and board[row-2][col-2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row-1][col-1].config(disabledforeground=color)
                    buttons[row-2][col-2].config(disabledforeground=color)
                    
            # check to see if diag down left
            if row <= self.board_size - 3 and col >= 2:
                if board[row+1][col-1] == 'O' and board[row+2][col-2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col-1].config(disabledforeground=color)
                    buttons[row+2][col-2].config(disabledforeground=color)
                    
            # check to see if diag up right
            if row >= 2 and col <= self.board_size - 3:
                if board[row-1][col+1] == 'O' and board[row-2][col+2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row-1][col+1].config(disabledforeground=color)
                    buttons[row-2][col+2].config(disabledforeground=color)
                    
        elif symbol == 'O':
            # look for the horizontal
            if col >= 1 and col <= self.board_size - 2:
                if board[row][col-1] == 'S' and board[row][col+1] == 'S':
                    sos_count += 1
                    buttons[row][col-1].config(disabledforeground=color)
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row][col+1].config(disabledforeground=color)
            
            # thi is for verticla
            if row >= 1 and row <= self.board_size - 2:
                if board[row-1][col] == 'S' and board[row+1][col] == 'S':
                    sos_count += 1
                    buttons[row-1][col].config(disabledforeground=color)
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col].config(disabledforeground=color)
            
            # check the diagonal
            if row >= 1 and row <= self.board_size - 2 and col >= 1 and col <= self.board_size - 2:
                if board[row-1][col-1] == 'S' and board[row+1][col+1] == 'S':
                    sos_count += 1
                    buttons[row-1][col-1].config(disabledforeground=color)
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col+1].config(disabledforeground=color)
            
            # check the diagonal
            if row >= 1 and row <= self.board_size - 2 and col >= 1 and col <= self.board_size - 2:
                if board[row-1][col+1] == 'S' and board[row+1][col-1] == 'S':
                    sos_count += 1
                    buttons[row-1][col+1].config(disabledforeground=color)
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col-1].config(disabledforeground=color)

        return sos_count

    def is_draw(self, board): # simple draw function checks for emptiness
        for row in board:
            if '' in row:
                return False
        return True    

    
class simple(game_win_draw):
    def __init__(self, board_size = 8):
        super().__init__(board_size, "Simple")
        self.simple_win = False
        self.all_draw = False
    def simple_game(self, row, col, board_placements, buttons, current_player):
        if self.is_sos(row, col, board_placements, buttons):
            self.simple_win = True
            return True  # return the True if there's a win
        if self.is_draw(board_placements):
            self.all_draw = True
            return "Draw"
        return None


class general(game_win_draw):
    def __init__(self, board_size=8):
        super().__init__(board_size, "General")
        self.blue_points = 0
        self.red_points = 0

    def general_game(self, row, col, board_placements, buttons, current_player):
        sos_formed = self.is_sos(row, col, board_placements, buttons)

        #simple function add up scoring
        if current_player == "blue":
            self.blue_points += sos_formed
        else:
            self.red_points += sos_formed

        # looking for the win
        if self.is_draw(board_placements):
            if self.blue_points > self.red_points:
                return "Blue Wins!"
            elif self.red_points > self.blue_points:
                return "Red Wins!"
            else:
                return "Draw"
        # this is helping with keeping the same player acutally kind of clever lol
        if sos_formed > 0:
            return True
        
        return False
    
#this here is just to add the class strcuture we discussed in class. it doesn't really serve a purpose.
class player:
    def __init__(self, symbol="S", color="blue"):
        self.symbol = symbol
        self.color = color
        
# this also doesn't serve a puporse it is to just show the class sstructure discussed in class. 
class human(player):
    def __init__(self, symbol="S", color="blue"):
        super().__init__(symbol, color)
            
class Computer(player):
    def __init__(self, symbol="S", color="blue"):
        super().__init__(symbol, color)
        self.game_file = 'game.txt'
        
        #this is where I set the ai model. You can have any model really.
        # chose gpt because easy to get key and is smart.
        model = llm.get_model("gpt-3.5-turbo")
        model.key = "insert key here"
        self.model = model
        
    def get_move(self, board):
        size = len(board)
        empty_cells = []
        
        # goes through row and col to check if posiont is empty
        for row in range(size):
            for col in range(size):
                if board[row][col] == '':
                    empty_cells.append((row, col))
        
        if not empty_cells:
            return None

        # open file
        with open(self.game_file, 'r') as file:
                game_history = file.read()
        
        # this is the prompt
        # i put the entire file in the because LLMs are smart
        the_ai = f"""
        
        This is an SOS game. 
        - blue and red are players
        - S and O are the symbols
        - 1, 1 are the rows and columns.
        - You must choose from these empty positions (row, col): {empty_cells}
        
        Grid Size: 
        {size} x {size}
        Game history is as follows:
        {game_history} 
        
        
        Respond ONLY with row, column, and symbol (e.g. 1, 2, S)
        Use 0 based index (0 to {size - 1})
        What is the next best move?
        """
        
        try:
            # this is the variable to hold the answer form prompt
            response = self.model.prompt(the_ai)
            
            response_text = response.text().strip()
            
            # spliting the response text by commas
            parts = response_text.split(',')
        
            # getting three parts the row, col, and symbol
            if len(parts) == 3:
                row = int(parts[0])
                col = int(parts[1])
                symbol = parts[2].strip()
                
                # return the move if the position is empty other wise we use out fallback.
                if (row, col) in empty_cells and board[row][col] == '':
                    return (row, col, symbol)
        except (ValueError, IndexError):
            pass
        
        # fallback mechanism for when LLM gives an invalid output.
        if empty_cells:
            row, col = random.choice(empty_cells)
            return (row, col, random.choice(['S', 'O']))
        return None

'''
# make the game more fun by adding a timer. Like chess. 
class timer:
    def __init__(self):
        pass
'''

# using the class structure from class. features jsut really is a placeholder class for now. 
class features():
    def __init__(self):
        self.filename = 'game.txt'
        
class record(features):
    def __init__(self):
        super().__init__()
    
    # we simply place the game in the file when we click record radio button
    def recorder(self, player, symbol, row, col):
        with open(self.filename, 'a') as file:
            file.write(f"{player},{symbol},{row},{col}\n")
            
    # I am wiping the data b/c if I didn't then I would have to search for the game I want replay.
    def data_wipe(self):
        with open(self.filename, 'w') as file:
            pass
        
class replay(features): 
    def __init__(self):
        super().__init__()
        
    # what we can do here is just use queue
    # the reason queue is good because its FIFO. so first move that is saved is replayed.
    # allows for mulitple replays becaue not deleting every line.
    def replayer(self):
        queue = []
        with open(self.filename, 'r') as file:
            for i in file:
                player, symbol, row, col, = i.strip().split(',')
                queue.append([player, symbol, int(row), int(col)])
        return queue


# GUI class for the game interface
class gui (board): # this will make it so inhertis the board for access.
    def __init__(self, display):
        self.display = display
        self.display.title("S.O.S")
        super().__init__() # this applies the intial setting.

        self.game_mode = StringVar(value = self.game_mode) # intital starting game mode
        self.player = StringVar(value = "blue") # initial starting player
        self.blue_symbol = StringVar(value = "S") # initial starting plater symbol
        self.red_symbol = StringVar(value = "S") # intial second player symbol
        self.blue_player_type = StringVar(value = "human")
        self.red_player_type = StringVar(value = "human")

        self.labels()
        self.buttons()
        self.grid()
        self.reset_game()
        
        #instances for features
        self.recorder = record()
        self.replayer = replay()  
        #self.is_recording = False
        #self.is_replaying = False
        
        self.score = general(self.board_size) #creating instance
        #self.computer_player = computer(self.board_size, self.game_mode)
        #self.game_handler = game_type_and_conditions(self.game_mode.get()) # works here because it is an instance variable.

    def start_new_game(self):

        new_board_size = int(self.board_size_entry.get())

        if new_board_size < 3 or new_board_size > 12:
            messagebox.showerror("Invalid Input", "Size in between 3 and 12.")
            return

        if new_board_size != self.board_size:
            self.board_size = new_board_size
            self.grid_frame.destroy()
            self.grid()

        else:
            # clear the existing grid if size hasn't changed
            for row_buttons in self.buttons:
                for button in row_buttons:
                    button.config(text=" ", state = NORMAL)

        super().reset_game()
         
        self.score = general(self.board_size)
        
        
        # this code is really just placeholder code
        if self.blue_player_type.get() == "computer":
            self.blue_player = Computer(symbol="S", color="blue")
        else:
            self.blue_player = human(symbol="S", color="blue")
            
        # automatically record game start with grid size
        self.recorder.data_wipe()
        self.recorder.recorder("Initial", f"Grid Size: {self.board_size}", -1, -1)

        
        if self.red_player_type.get() == "computer":
            self.red_player = Computer(symbol="S", color="red")
        else:
            self.red_player = human(symbol="S", color="red")
        
        self.reset_game()
        self.status_label.config(text = "")  # cleaing the label o
        self.blue_score.config(text="Score: 0") 
        self.red_score.config(text="Score: 0")
        
    
        self.recorder.data_wipe()
        
        if isinstance(self.blue_player, Computer): # the function isinstance is built into python as well.
            #learned it from mcoding youtuber.
            self.display.after(500, self.computer_turn) #this is like a funcition built into tkinter. 
            #if I wanted I could use time to delay the inputs but why add extra fluff.
    
    
        
    def labels(self): # referenced W3schools and stackoverflow to create the frame.
        self.game_type_frame = Frame(self.display)
        self.game_type_frame.pack(side=TOP, fill=X)

        self.place_left_frame = Frame(self.game_type_frame)
        self.place_left_frame.pack(side = LEFT)

        self.place_right_frame = Frame(self.game_type_frame)
        self.place_right_frame.pack(side=RIGHT)
        Label(self.place_right_frame, text="Board size").pack(side=LEFT)
        self.board_size_entry = Entry(self.place_right_frame, width = 3)
        self.board_size_entry.insert(0, "8")
        self.board_size_entry.pack(side=LEFT)

        self.control_frame_blue = Frame(self.display)
        self.control_frame_blue.pack(side = LEFT)
        Label(self.control_frame_blue, text="Blue Player", fg = "cyan").grid(row = 0, column = 0)
        self.blue_score = Label(self.control_frame_blue, text = f"Score: 0")
        self.blue_score.grid(row = 5, column = 0)

        self.control_frame_red = Frame(self.display)
        self.control_frame_red.pack(side=RIGHT)
        Label(self.control_frame_red, text="Red Player", fg = "red").grid(row = 0, column = 0)
        self.red_score = Label(self.control_frame_red, text = f"Score: 0")
        self.red_score.grid(row = 8, column = 0) # this makes it so the valye isn't None. Solution found through stackoverflow

        self.turn_label = Label(self.display, text="Current Player: Blue")
        self.turn_label.pack(side=BOTTOM)

        self.status_label = Label(self.display, text = "", fg = "green")
        self.status_label.pack(side=BOTTOM)

    def buttons(self): # utilized geeksforgeeks examples to implement this.
        #buttons for the game selection
        Radiobutton(self.place_left_frame, text="Simple", variable = self.game_mode, value = "Simple").pack(side=LEFT)
        Radiobutton(self.place_left_frame, text="General", variable = self.game_mode, value = "General").pack(side=LEFT)

        # human plaer buttons.
        Radiobutton(self.control_frame_blue, text="human", fg="cyan", variable = self.blue_player_type, value = "human").grid(row = 1, column = 0)
        Radiobutton(self.control_frame_red, text="human", fg="red", variable = self.red_player_type, value = "human").grid(row = 4, column = 0)
        
         #buttons for the blue player's S or O selection
        Radiobutton(self.control_frame_blue, text = "S", fg = "cyan", variable = self.blue_symbol, value = "S").grid(row = 2, column = 0)
        Radiobutton(self.control_frame_blue, text = "O", fg = "cyan", variable = self.blue_symbol, value = "O").grid(row = 3, column = 0)

        #Red Player
        #buttons for the red player's S or O selection
        Radiobutton(self.control_frame_red, text = "S", fg = "red", variable = self.red_symbol, value = "S").grid(row = 5, column = 0)
        Radiobutton(self.control_frame_red, text = "O", fg = "red", variable = self.red_symbol, value = "O").grid(row = 6, column = 0)
        
        #computer player  buttons. 
        Radiobutton(self.control_frame_blue, text = "Computer", fg = "cyan", variable = self.blue_player_type, value = "computer").grid(row = 4, column = 0)
        Radiobutton(self.control_frame_red, text = "Computer", fg = "red", variable = self.red_player_type, value = "computer").grid(row = 7, column = 0)

        # IK this is a ceneted but it makes sense.
        Button(self.display, text = "New Game", command = self.start_new_game).pack(side = BOTTOM)
        
        #feature buttons I think I will add a timer later. 
        #Button(self.place_left_frame, text="Record", command=self.start_recording).pack(side=LEFT)
        Button(self.place_left_frame, text="Replay", command=self.replay_game).pack(side=LEFT)
    
    
    # this will help us start recording. its like a swithc.
    def start_recording(self):
        self.is_recording = not self.is_recording 
        if self.is_recording:
            self.recorder.data_wipe() #also\ wipes it out when we do a new recording.
            
    #this gets the moves that have been recorded in the file.
    def replay_game(self):
        self.replay_moves = self.replayer.replayer() #this one
        self.replay_index = 0
        self.is_replaying = True
        self.start_new_game()
        self.replay_move()
    
    # function replas the moves.
    def replay_move(self):
        if self.replay_index < len(self.replay_moves): # checking moves left basically 
            player, symbol, row, col = self.replay_moves[self.replay_index] #get the queue daya
            
            #setting varibles based on the recorded move. 
            self.player = player
            if player == "blue":
                self.blue_symbol.set(symbol)
            else:
                self.red_symbol.set(symbol)
            self.SOS_button(row, col) #making the move
            self.replay_index += 1
            self.display.after(500, self.replay_move)#adding little time delay so we can see moves being filled like computer
        else:
            self.is_replaying = False #ending the replay basically.

    def SOS_button(self, row, col):
        # this here determines the sos color based on the player
        # also what the player places down is based on this. 
        if self.player == "blue":
            self.sos_symbol = self.blue_symbol.get()
            color = "cyan"
        else:  # red player
            self.sos_symbol = self.red_symbol.get()
            color = "red"

        self.buttons[row][col].config(text=self.sos_symbol, state = DISABLED, disabledforeground = color)
        self.board[row][col] = self.sos_symbol

        # recording moves if the game isn't replaying AND recording the game currently.
        #if not self.is_replaying and self.is_recording:
        self.recorder.recorder(self.player, self.sos_symbol, row, col) #calling recorder to record move..
 
        
        if self.game_mode.get() == "Simple":
            result = simple(self.board_size).simple_game(row, col, self.board, self.buttons, self.player)
            if result == True:
                self.status_label.config(text = f"{self.player} Wins!")
                return
            elif result == "Draw":
                self.status_label.config(text = f"{result}")
                return
            else:
                self.switch()
        
        else:  # tjis is General mode
            #result = general(self.board_size).general_game(row, col, self.board, self.buttons, self.player)
            result = self.score.general_game(row, col, self.board, self.buttons, self.player) # this is beter becuase uses existing instance
            if result == "Blue Wins!" or result == "Red Wins!":
                self.blue_score.config(text = f"Score: {self.score.blue_points}")
                self.red_score.config(text = f"Score: {self.score.red_points}")
                self.status_label.config(text = f"{result}")
                return
            elif result == "Draw":
                self.blue_score.config(text = f"Score: {self.score.blue_points}")
                self.red_score.config(text = f"Score: {self.score.red_points}")
                self.status_label.config(text = f"{result}")
            elif not result:
                self.blue_score.config(text = f"Score: {self.score.blue_points}")
                self.red_score.config(text = f"Score: {self.score.red_points}")
                self.switch()
            else:
                self.blue_score.config(text = f"Score: {self.score.blue_points}")
                self.red_score.config(text = f"Score: {self.score.red_points}")


        self.turn_label.config(text=f"Current Player: {'Blue' if self.player == 'blue' else 'Red'}")
        next_player_type = self.blue_player_type.get() if self.player == "blue" else self.red_player_type.get()
        if next_player_type == "computer":
            self.display.after(500, self.computer_turn)  # the delay system I learned from Stakcoverflow
            # the reason we need delay is because otherwise the game is instant
            
    def computer_turn(self):

        current_player = self.blue_player if self.player == "blue" else self.red_player
        
        if not isinstance(current_player, Computer): #isinstance is a python function. Source: mcoding1
            current_player = Computer(symbol = self.blue_symbol.get() if self.player == "blue" else self.red_symbol.get(), color=self.player)
        
        move = current_player.get_move(self.board)
        if move:
            row, col, symbol = move
            if self.player == "blue":
                self.blue_symbol.set(symbol)
            else:
                self.red_symbol.set(symbol)
            self.SOS_button(row, col)
            
    def grid(self):
        self.grid_frame = Frame(self.display)
        self.grid_frame.pack()
        self.buttons = []
        for r in range(self.board_size):
            button_r = []
            for c in range(self.board_size):
                #, width = 1, height = 1
                SOS_buttons = Button(self.grid_frame, text = " ", command = lambda row = r, col = c: self.SOS_button(row, col))
                SOS_buttons.grid(row = r, column = c)
                button_r.append(SOS_buttons)
            self.buttons.append(button_r)


# Main function to start the application
class main(board):
    def __init__(self):
        #board.__init__(self, board_size = 8, game_mode = "Simple")
        display = Tk()
        app = gui(display)
        display.geometry("1000x500")

        display.mainloop()

# this helps with indicating that this file is to executed. (Source: M1Coding)
if __name__ == "__main__":
    main()