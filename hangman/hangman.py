# Hangman
import random
from stages import stages

words = ["samuel", "pavel", "martin", "ondra", "vojta", "robert"]
word_index = random.randint(0, len(words)-1)
word = words[word_index]

# Generating _
word_hidden = []

for random_letter in word:
  word_hidden.append("_")

printed_word = ""
for one_letter in word_hidden:
  printed_word += one_letter
print(printed_word)

# test = ""

# for one_letter in word_hidden:
#   test += one_letter

# print(test)

lives = 3

while "_" in word_hidden: 
  guess = input("Zadajte hádané písmeno: ").lower()

  for index in range(0, len(word)):
    if guess == word[index]:
      word_hidden[index] = guess
      
  if guess not in word_hidden:
    lives -= 1
    print(stages[lives])
  print(f"Počet vašich životov je: {lives}")
  if lives == 0:
    print("Prehrali ste!")
    break
  
  printed_word = ""
  for one_letter in word_hidden:
    printed_word += one_letter
  print(printed_word)

  if "_" not in word_hidden:
    print("Vyhrali ste")