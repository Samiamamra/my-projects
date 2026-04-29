from os import system
from random import choice

class Player:
	WIN_SITUATIONS =  [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
	PLAYERS = ["X","O"]

	def __init__(self):
		pass

	def get_names(self):
		name1,name2 = input(f"Player {Player.PLAYERS[0]}, enter your name: "), input(f"Player {Player.PLAYERS[1]}, enter your name: ")
		return {Player.PLAYERS[0] : name1, Player.PLAYERS[1] : name2}

class Game:
	def __init__(self, play, player):
		self.cells = ["1","2","3","4","5","6","7","8","9"]
		self.current_turn = choice(Player.PLAYERS)
		self.play = play
		self.player = player

	def playing(self, names):	
		result = self.is_win(names)
		if result[0]:
			self.play.win(result)
			return False
		if self.is_draw():
			self.play.draw()
			return False
		else:
			return True

	def is_win(self, names):
		for player in self.player.PLAYERS:
			for win_situation in self.player.WIN_SITUATIONS:
				if self.cells[win_situation[0]] == player and self.cells[win_situation[1]] == player and self.cells[win_situation[2]] == player:
					return [True, player, names.get(player)]
		return [False]
		
	def is_draw(self):
		for cell in self.cells:
			if cell not in self.player.PLAYERS:
				return False
		return True
		# or we can use:
	    #return all(cell in self.player.PLAYERS for cell in self.cells)

	def mplay(self):
		names = self.player.get_names()
		self.play.cls()
		self.update_board()
		while self.playing(names):
			self.update_board(self.play.get_choice(names, self))
			self.flip_turn()

	def flip_turn(self):
		if self.current_turn == "X":
			self.current_turn = "O"
		else:
			self.current_turn = "X"

	def update_board(self, cell_choice=None):
		if cell_choice != None:
			self.play.cls()
			self.cells[int(cell_choice)-1] = self.current_turn	
		board = f"{self.cells[0]} | {self.cells[1]} | {self.cells[2]}\n_________\n{self.cells[3]} | {self.cells[4]} | {self.cells[5]}\n_________\n{self.cells[6]} | {self.cells[7]} | {self.cells[8]}"
		print(board)
	
	def start(self,choice):
		if choice == "1":
			self.mplay()
		elif choice == "2":
			exit()

class Play:
	def __init__(self):
		pass

	def main_menu(self):
		self.cls()
		choice = input("1-new game.\n2-exit.\nenter yor choice(1 or 2): ")
		if choice == "":
			input("You've not entered anything.\npress enter to go back...")
			return self.main_menu()
			
		if choice not in ["1","2"]:
			input("please enter 1 or 2 only.\npress enter to go back...")
			return self.main_menu()
		
		else:
			return choice

	def greeting(self):
		input("welcome in this simple XO game!\npress enter to continue...")

	def get_choice(self, names, game):
		while True:
				cell_choice = input(f"{names.get(game.current_turn)} \"player {game.current_turn}\", enter your choice (1-9): ")
				if cell_choice not in ["1","2","3","4","5","6","7","8","9"]:
					input("The value you entered is can't be a cel number.\nyour choice must be one of the folwing numbers(1,2,3,4,5,6,7,8,9).\npress enter to go back...")
					self.cls()
				elif game.cells[int(cell_choice)-1] in ["O","X"]:
					input("the cel you choosed is already taken so you must choose an other one.\npress enter to go back...")
					self.cls()
				else:
					break
		return cell_choice
	
	def cls(self):
		system("cls")
			
	def draw(self):
		self.cls()
		input("_"*37+"Draw!"+"_"*38)
		
	def win(self,winer):
		self.cls()
		print(f"{'_'*24}{winer[2]} \"player {winer[1]} \", is the winer!{'_'*24}")

play = Play()
player = Player()
game = Game(play, player)

def run():
	play.greeting()
	play.cls()
	game.start(play.main_menu())

run()

