import random
from accounts import data

def rand_func(accounts):
  account_a_index = random.randint(0, len(accounts) - 1)
  account_b_index = random.randint(0, len(accounts) - 1)

  if account_a_index == account_b_index:
    account_b_index -= 1
  
  return [account_a_index, account_b_index]
  
def result_func(account_a, account_b):
  print(f"Porovnajte A: {account_a['name']}, {account_a['description']}, {account_a['country']}")
  print(f"Porovnajte B: {account_b['name']}, {account_b['description']}, {account_b['country']}")

  print(account_a['follower_count'])
  print(account_b['follower_count'])
  
  if account_a['follower_count'] > account_b['follower_count']:
    result = "A"
  elif account_a['follower_count'] < account_b['follower_count']:
    result = "B"

  return result

def game_func():
  
  score = 0
  lets_continue = True
  while lets_continue:
    indexes = rand_func(data)

    account_a = data[indexes[0]]
    account_b = data[indexes[1]]

    result = result_func(account_a, account_b)
    guess = input("Kto má viac sledujúcich?: ")

    if guess == result:
      score += 1
      print(f"Uhádli ste, pokračujeme ďalej v hre. Vaše skóre je: {score} \n")
    else:
      print("Neuhádli ste, hra končí")
      lets_continue == False
      break

game_func() 