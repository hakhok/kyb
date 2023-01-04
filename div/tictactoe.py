class TicTacToe:
  def __init__(self):
    # Initialize game state
    self.current_player = 'X'
    self.grid = [
      [None, None, None],
      [None, None, None],
      [None, None, None]
    ]
    self.game_status = 'ongoing'

  def play(self, row, col):
    # Check if the move is within the bounds of the grid
    if not (0 <= row < 3 and 0 <= col < 3):
      print('Invalid move! Please choose a row and column between 0 and 2.')
      return

    # Check if the chosen cell is already occupied
    if self.grid[row][col] is not None:
      print('Invalid move! That cell is already occupied.')
      return

    # Update the grid with the player's move
    self.grid[row][col] = self.current_player

    # Check if the game has ended
    self.check_game_status()

    # Switch the current player
    self.current_player = 'O' if self.current_player == 'X' else 'X'

  def check_game_status(self):
    # Check if the game is a draw
    if all(all(cell is not None for cell in row) for row in self.grid):
      self.game_status = 'draw'

    # Check if one of the players has won
    for row in self.grid:
      if row[0] == row[1] == row[2] and row[0] is not None:
        self.game_status = f'{row[0]} wins'

    for col in range(3):
      if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] is not None:
        self.game_status = f'{self.grid[0][col]} wins'

    if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] is not None:
      self.game_status = f'{self.grid[0][0]} wins'

    if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] is not None:
      self.game_status = f'{self.grid[0][2]} wins'

  def print_grid(self):
    # Print the current state of the game grid
    print('+---+---+---+')
    for row in self.grid:
      print('|', end='')
      for cell in row:
        if cell is None:
          print('   |', end='')
        else:
          print(f' {cell} |', end='')
      print()
      print('+---+---+---+')

# Create a TicTacToe game
game = TicTacToe()

# Loop through time steps and play the game
# Loop through time steps and play the game
while game.game_status == 'ongoing':
  # Print the current state of the game grid
  game.print_grid()

  # Prompt the player for their move
  row = int(input('Enter row: '))
  col = int(input('Enter col: '))

  # Play the game
  game.play(row, col)

# Print the final game status
print(game.game_status)

