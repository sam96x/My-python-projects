import random
import os

def difficulty_func():
  """Funkcia, na základe ktorej sa vyberie, koľko má hráč životov"""
  difficulty = input("Vyberte obtiažnosť. Napíšte 'easy, 'medium', 'hard' alebo 'legend': ")
  return difficulty

def lives_func(difficulty):
  """Funkcia, v ktorej sa na základe obtiažnosti vypočíta počet životov"""
  lives = 0
  
  if difficulty == "easy":
    lives = 10
  elif difficulty == "medium":
    lives = 7
  elif difficulty == "hard":
    lives = 4
  elif difficulty == "legend":
    lives = 1
  
  return lives

def guess_func(number):
  """Funkcia, kde sa porovnáva vstup užívateľa s číslom, ktoré má hádať"""
  guess = int(input("Tipnete si číslo: "))

  if guess < number:
    print("Číslo je príliš nízke")
  elif guess > number:
    print("Číslo je príliš vysoké")
  elif guess == number:
    print("Gratulujeme, vyhtali ste")
    game_again_func()
    
  
def game_again_func():
  """Funkcia na vypísanie inputu pre pokračovanie hry"""
  game_again = input("Ak chcete hrať znova, napíšte 'ano', ak nie, tak napíšte 'nie'.: ")
  
  if game_again == "ano":
    os.system("clear")
    game_func()
  elif game_again == "nie":
    os.system("clear")
    quit()

def game_func():
  """Funkcia, ktorou sa spúšťa hra"""
  number = random.randint(1, 100)

  print("Myslím si číslo od 1 do 100")
  
  difficulty = difficulty_func()
  lives = lives_func(difficulty)
  
  while lives != 0:
    print(f"Počet zostávajúcich pokusov je: {lives}")
    guess_func(number)
    lives -= 1
    
    if lives == 0:
      print(f"Prehrali ste! Hádané číslo bolo {number}.")
      game_again_func()
    
game_func()