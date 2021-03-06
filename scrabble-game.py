letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# assigning each letter a corresponding value
letter_to_points={key:value for key, value in zip(letters, points)}
#print(letter_to_points)
letter_to_points[""] = 0

# a function calculating the word score:
def score_word(word):
  point_total=0
  for letter, value in letter_to_points.items():
    for i in word:
      if i.upper() == letter:
        point_total+=value
      else:
        continue
  return point_total
#print(score_word("bbb"))

# testing score_word function:
brownie_points = score_word("BROWNIE")
#print(brownie_points)

# calculating points for each player:
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points={}
for player, words in player_to_words.items():
  player_points=0
  for word in words:
    player_points+=score_word(word)
    #print(player_points)
  player_to_points[player]=player_points
  print(player_to_points)
