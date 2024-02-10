import os
from menu import menu
from resources import resources

def report_ingredients():
  """Funkcia na zistenie stavu zásob ingrediencií"""
  print(f"Voda: {resources['water']}")
  print(f"Mlieko: {resources['milk']}")
  print(f"Káva: {resources['coffee']}")

  lets_continue()

def add_ingredients(): 
  """Funkcia na pridanie ingrediencií do kávovaru"""
  add_water = int(input("Vložte vodu: "))
  add_milk = int(input("Vložte mlieko: "))
  add_coffee = int(input("Vložte kávu: "))

  resources['water'] += add_water
  resources['milk'] += add_milk
  resources['coffee'] += add_coffee

  report_ingredients()
  lets_continue()

def remove_ingredients(): 
  """Funkcia na odobranie ingrediencií v kávovare"""
  remove_water = int(input("Odoborte vodu: "))
  remove_milk = int(input("Odoborte mlieko: "))
  remove_coffee = int(input("Odoborte kávu: "))

  resources['water'] -= remove_water
  resources['milk'] -= remove_milk
  resources['coffee'] -= remove_coffee

  report_ingredients()
  lets_continue()

def reduction_ingredients(user_choice):  
  """Funkcia, ktorá zníži stav ingrediencií po objednávke zákazníka"""
  resources["water"] -= menu[user_choice]["ingredients"]["water"]
  resources["milk"] -= menu[user_choice]["ingredients"]["milk"]
  resources["coffee"] -= menu[user_choice]["ingredients"]["coffee"]
  
def check_ingredients(user_choice):
  """Funkcia, ktorá overí, či je možné vydať nápoj na základe stavu zásob ingrediencií"""
  water = resources["water"] - menu[user_choice]["ingredients"]["water"]
  milk = resources["milk"] - menu[user_choice]["ingredients"]["milk"]
  coffee = resources["coffee"] - menu[user_choice]["ingredients"]["coffee"]
  
  if water < 0 or milk < 0 or coffee < 0:
    print("Nie sú zásoby na prípravu tohto nápoja.")
    lets_continue()

def check_coins(coins_list):
  """Funkcia, ktorá overí, či užívateľ vhodil správne mince"""
  valid_coins = ["1","2","5","10","20","50"]
  not_valid_coins = []

  for coin in coins_list:
    if coin not in valid_coins:
      print(f"Vložili ste chybnú mincu. {coin}")
      not_valid_coins.append(coin)
  
  for coin in not_valid_coins:
    coins_list.remove(coin)

  return coins_list

def insert_coins():
  """Funkcia, ktorá vráti sumu v Kč, ktorú užívateľ hodil pomocou mincí."""
  print("Prosím vložte mince: 1, 2, 5, 10, 20, 50")
  coins = (input("Vložte mince (čísla oddelené medzerou): "))
  coins_list = coins.split(" ")

  final_list = check_coins(coins_list)

  sum = 0
  for coin in final_list:
    sum += int(coin)
  
  return sum

def payment_by_card():
  """Funkcia, ktorá slúži na zaplatenie kávy pomocou užívateľovej platobnej karty."""
  card_input = input("Priložte prosím kartu (napíšte ano alebo nie): ")
  if card_input == "nie":
    print("Platba kartou nezrealizovaná.")
    lets_continue()

def payment_by_coins(product_price):
  """Funkcia, ktorá slúži na zaplatenie kávy pomocou mincí."""
  user_price = 0
  
  while user_price < product_price:
    user_price += insert_coins()
    if user_price < product_price:
      print(f"Vložili ste len {user_price} Kč. Treba ešte doplatiť {product_price - user_price} Kč.")
  
  print(f"Vložili ste za nápoj: {user_price} Kč\nČiastka k vráteniu: {user_price - product_price} Kč")

def check_payment(product_price):
  """Funkcia na overenie, či užívateľ chce platiť kartou alebo mincou."""
  card_payment = input("Chcete platiť bezhotovostnou platbou (ano alebo nie): ")
  
  if card_payment == "nie":
    payment_by_coins(product_price)
  elif card_payment == "ano":
    payment_by_card()
  else:
    print("Neplatná odpoveď.")
    lets_continue()
  
  print("Váš nápoj sa pripravuje.")

def lets_continue():
  """Funkcia, ktorá slúži na to, či si chce užívateľ vybrať ďalší produkt."""
  lets_continue = input("Chcete si vybrať ďalší nápoj? ano alebo nie: ")

  while lets_continue == "ano":
    os.system("clear")
    main_func()
  
  if lets_continue == "nie":
    exit()

def make_coffee(user_choice):
  """Funkcia, ktorá prípravy kávu."""
  product_price = menu[user_choice]["cost"]

  check_ingredients(user_choice)
  print(f"Cena kávy je: {product_price}")
  check_payment(product_price)
  reduction_ingredients(user_choice)

def main_func():
  """Funkcia, ktorá spúšťa celý proces prípravy kávy."""
  row_1 = ["espresso", "cappuccino", "latte"]

  print("Dajte si skvelu kávu a buďte svieži počas zvyšku dňa.\nVyberte si z našej skvelej ponuky")
  print(f"{row_1}")

  user_choice = input("Vyberte si prosím nápoj: ")

  if user_choice == "report":
    report_ingredients()
  elif user_choice == "add":
    add_ingredients()
  elif user_choice == "remove":
    remove_ingredients()
  elif user_choice in menu: 
    make_coffee(user_choice)
  else:
    print("Daný nápoj nemáme.")
  
  lets_continue()

main_func()