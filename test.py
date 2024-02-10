# print("Vitaj v aplikácii vtipných mien.")
# name = input("Napíš tvoje krstné meno:\n")
# description = input("Napíš tvoju typickú vlastnosť:\n")
# print("Tvoje meno je " + name + " " + description)

# String

# age = 40
# print(type(age))
# print("Som Samuel a mám " + str(age))

# number = input("Napíšte dvojmiestne číslo:\n")
# print(int(number[0])+int(number[1]))

# height = input("Zadaj svoju výšku:\n")
# weight = input("Zadaj svoju váhu:\n")
# bmi = int(weight) / float(height)**2
# print("Tvoje BMI je " + str(bmi));

# F-string
# x = 5
# print(f"Premenna je: {x}")

# age = input("Zadaj svoj vek:\n")
# remain = 90 - int(age)
# months = 12 * remain
# weeks = 52 * remain
# days = 365 * remain
# print(f"Zostáva ti {remain} rokov, {months} mesiacov, {weeks} týždňov a {days} dní")

# print("Kalkulačka na výpočet platieb.")
# price = float(input("Koľko máte zaplatiť? "))
# additional = float(input("Koľko chcete nechať sprepitné (v %)? "))
# people = int(input("Medzi koľko ľudí chcete platbu rozdeliť? "))
# payment = (price + (price * additional / 100)) / people
# payment_format = "{:.2f}"
# final_payment = payment_format.format(payment)
# print(f"Každý musí zaplatiť {final_payment}")

# height = int(input("Zadaj vek: "))

# if height < 18:
#   print("Nie si dospelý")
# else:
#   print("Si dospelý.")

# price = 150
# price_discount = 120
# student = input("Ste študentom? (napíšte áno/nie) ")

# if student == "áno":
#   print(f"Cena lístku je {price_discount}")
# elif student == "nie":
#   print(f"Cena lístku je {price}")
# else:
#   print("Zadali ste zlú hodnotu")

# type = input("Aký typ mobilu chcete? Normal, smart alebo extrasmart?\n")

# BMI

# height = float(input("Vložte svoju výšku v metroch: "))
# weight = float(input("Vložte svoju váhu v kilogramoch: "))

# bmi = weight / (height*height)

# print(round(bmi,1))

# if bmi < 18.5:
#   print("Podvýživený") 
# elif bmi < 25:
#   print("Normálny")
# elif bmi < 30:
#   print("Nadvýživený")
# elif bmi < 35:
#   print("Obézny")
# else:
#   print("Extrémne obázby")

# year = int(input("Zadaj rok: "))

# condition1 = (year % 4 == 0 & year % 100 != 0) 
# condition2 = (year % 4 == 0 & year % 100 == 0 & year % 400 == 0)

# if condition1 | condition2:
#   print("Jedná sa o prestupný rok.")
# else:
#   print("Nejedná sa o prestupný rok.")
  
# year = int(input("Zadaj rok: "))

# print("Objednávka pizze.")

# size = input("Akú veľkosť pizze chcete? S, M alebo L ")
# pepperoni = input("Chcete feferónky? A alebo N ")
# cheese = input("Chcete sýr? A alebo N ")

# bill = 0

# if size == "S":
#   bill += 100
# elif size == "M":
#   bill += 150
# elif size == "L":
#   bill += 200
# else:
#   print("Daná veľkosť neexistuje.")
  
# if pepperoni == "A":
#   if size != "S":
#     bill += 30
#   else:
#     bill += 20
  
# if cheese == "A":
#   bill += 15

# print(f"Treba zaplatiť: {bill} Kč")
  
# print("Vítajte na horskej dráhe.")
# height = int(input("Aká je vaša výška v cm? "))

# bill = 0
# if height > 86:
#   print("Môžete ísť na horskú dráhu!")
#   age = int(input("Aký je váš vek? "))
#   if age < 12:
#     bill += 50
#     print("Cena lístku je 50 Kč")
#   elif age < 18:
#     bill += 100
#     print("Cena lístku je 100 Kč")
#   elif age >= 40 and age <= 50:
#     bill += 0
#     print("Lístok je zadarmo") 
#   else:
#     bill += 150
#     print("Cena lístku je 150 kč")
#   photo = input("Chcete sa nechať vyfotiť? Napíšte áno alebo nie ")
#   if photo == "áno":
#     bill += 40
  
#   print(f"Vaša cena je: {bill} kč")
# else:
#   print("Nemôžete ísť na horskú dráhu!") 

# print(''' _                                       _   _            
# | |                                     | | | |           
# | |__   __ _ _ __ _ __ _   _ _ __   ___ | |_| |_ ___ _ __ 
# | '_ \ / _` | '__| '__| | | | '_ \ / _ \| __| __/ _ \ '__|
# | | | | (_| | |  | |  | |_| | |_) | (_) | |_| ||  __/ |   
# |_| |_|\__,_|_|  |_|   \__, | .__/ \___/ \__|\__\___|_|   
#                         __/ | |                           
#                        |___/|_|                           ''')

# print("Vítajte na Rockforde.\n Školník vás zavedie na vaše internáty.")
# classmates = input("Chceš následovať svojich spolužiakov na Chrabromilský internát? A alebo N ").lower()

# import random

# print(random.randint(10,18))
# print(random.random())
# print(random.randrange(15,25,2))

# import random

# coin = ["Hlava", "Orol"]

# print(random.choice(coin))

# # List
# employees = ["Samuel", "Ondrej"]
# print(employees)
# employees.append("Martin")
# print(employees)
# employees[1] = "Adam"
# print(employees)
# employees.extend(["Ondrej", "Ivan"])
# print(employees)
# employees.remove("Ondrej")
# print(employees)

# import random

# names = input("Napíš mi mená všetkých ľudí oddelených čiarkou\n")

# print(names)

# list_names = names.split(", ")

# print(list_names)

# print(random.choice(list_names))

# random_number = random.randint(0, len(list_names)-1)

# print(list_names[random_number])

## Index error
# snv = ["Rapáč", "Ališauskas", "Melicherčík"]
# poprad = ["Záborsky", "Brejčák", "Rabčan"]

# number = len(snv)
# print(snv(number))

# Nested list

# snv = ["Rapáč", "Ališauskas", "Melicherčík"]
# poprad = ["Záborsky", "Brejčák", "Rabčan"]

# teams = [snv, poprad]
# print(teams[0][2])

# set1 = ["| |", "| |", "| |"]
# set2 = ["| |", "| |", "| |"]
# set3 = ["| |", "| |", "| |"]

# all_sets = [set1, set2, set3]
# print(f"{set1}\n{set2}\n{set3}")

# position = input("Zadaj súradnice\n")

# num1=int(position[0])
# num2=int(position[1])

# all_sets[num1][num2] = "|X|"
# print(f"{set1}\n{set2}\n{set3}")

# Papier, nožky, kameň

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''


# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''


# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# list = [rock, paper, scissors]

# user_choose = int(input("Napíšte 0 pre kameň, 1 pre papier alebo 2 pre nožnice \n"))
# user_choice = list[user_choose]

# pc_choose = random.randint(0, len(list)-1)
# pc_choice = list[pc_choose]

# print(f"Vybral si si: \n {user_choice} ")
# print(f"Počítač si vybral: {pc_choice}")

# user_pc_choice = [user_choice, pc_choice]
# user_win = [[list[0],list[2]], [list[1],list[0]], [list[2],list[1]]]

# if user_pc_choice in user_win:
#   print("Vyhral si, gratulujem")
# elif user_choice == pc_choice:
#   print("Remíza")
# else:
#   print("Bohužiaľ, počítač vyhral")

# heights = input("Zadajte výšky ľudí oddelené čiarkou a medzerou\n")

# list_heights = heights.split(", ")

# count_people = len(list_heights)

# sum = 0

# for height in list_heights:
#   sum += int(height)

# average = sum / count_people

# print(f"Priemerná výška je: {average}")

# score = input("Zadajte skóre z testov.\n")

# list_score = score.split(", ")
# list_score_number = []

# minimum = int(list_score[0])
# maximum = int(list_score[0])

# for one_score in list_score:
#   list_score_number.append(int(one_score))

# for one_score in list_score:
#   if one_score < minimum:
#     minimum = one_score
  
#   if one_score > maximum:
#     maximum = one_score

# print(minimum)
# print(maximum)

# sum = 0

# # for one_number in range(1, 101, 2):
# #   sum += one_number

# for one_number in range(1, 101):
#   if one_number % 2 == 0:
#     sum += one_number

# print(sum)

# for one_number in range(1, 101):
#   if one_number % 3 == 0 and one_number % 5 == 0:
#     print("Fizz Buzz")
#   elif one_number % 3 == 0:
#     print("Fizz")
#   elif one_number % 5 == 0:
#     print("Buzz")
#   else:
#     print(one_number)

# myName = "Samuel"
# myList = [5, 10, 15, True]

# for one_letter in myName:
#   print(one_letter)
  
# for one_character in myList:
#   print(one_character)

# x = 0

# while x<=10:
#   print(f"Test: {x}")
#   # Bez toho nekonečný cyklus
#   x += 1
# import random

# characters = ["Samuel", "Robert", "Ivan", "Ondrej"]

# character_index = random.randint(0, len(characters) - 1)
# character = characters[character_index]
# guess = ""
# guess_count = 2

# while character != guess:
#   if guess_count != 0:
#     guess = input("Uhadnite meno postavy: ")
#     guess_count -= 1
#   else:
#     print("Počet pokusov vyčerpaný.")
#     break
#   if character == guess: 
#     print(f"Uhadli ste, hádané slovo bolo {character}")

# Funkcie
# def my_function(name, location):
#   print(f"Som {name} a bývam v meste {location}")
# my_function("Samuel", "Praha")
# my_function(location = "Praha", name= "Samuel")

# import math

# height = int(input("Výška steny: "))
# width = int(input("Šírka steny: "))
# coverage = 5

# def paint_calculator(width, height, cover):
#   area = width * height
#   number_can = math.ceil(area / cover)
#   print(f"Potrebujete {number_can} plechovky farby.")

# paint_calculator(height, width, coverage)

# number = int(input("Zadajte číslo: "))

# def prime_number(num):
#   result = "Jedná sa o prvočíslo"
#   for x in range(2, num):
#     if num % x == 0:
#       result = "Nejedná sa o prvočíslo"
  
#   print(result)

# prime_number(number)

# dictionary - key: value
# it_dictionary = {
#   "String": "Text",
#   "Integer": "Celé číslo",
#   "Float": "Desatinné číslo",
#   "Boolean": "Pravda nepravda"
# }

# print(it_dictionary["String"])
# print(it_dictionary["Integer"])

# it_dictionary_2 = {
#   0: "Celé číslo",
#   1: "Text",
#   2: "Desatinné číslo",
#   3: "Pravda nepravda"
# }

# print(it_dictionary_2[0])
# print(it_dictionary_2[1])

# it_dictionary_2[4] = "Uloženie viacerých hodnôt"
# print(it_dictionary_2)

# # vyprázdnenie

# it_dictionary = {}

# it_dictionary_2[1] = "Textová hodnota"
# print(it_dictionary_2)

# for key in it_dictionary_2:
#   # print(key)
#   print(it_dictionary_2[key])

# student_results = {
#   "Samuel": 95,
#   "Robert": 70,
#   "Martin": 85
# }
  
# description_results = {}

# for key in student_results:
#   score = student_results[key]
  
#   if score > 90:
#     description_results[key] = "Excelentný"
#   elif score > 80:
#     description_results[key] = "Vynikajúci"
#   elif score > 70:
#     description_results[key] = "Splnen0"
#   else:
#     description_results[key] = "Nesplnené"

# print(description_results)

# cities = {
#   "Spain": "Madrid",
#   "France": "Paris"
# }

# print(cities)

# travel_diary = {
#   "Spain": ["Madrid", "Barcelona", "Valencia"],
#   "France": ["Paris", "Marseille", "Lyon"]
# }

# print(travel_diary["France"][0])

# travel_diary_2 = {
#   "Spain": {
#     "visited_cities": ["Madrid", "Barcelona", "Valencia"], 
#     "visits": 5
#   },
#   "France": {
#     "visited_cities": ["Paris", "Marseille", "Lyon"],
#     "visits": 1
#   }
# }

# print(travel_diary_2["France"]["visited_cities"][0])

# travel_diary_3 = [
#   {
#     "country": "Spain",
#     "visited_cities": ["Madrid", "Barcelona", "Valencia"], 
#     "visits": 5
#   },
#   {
#     "country": "France",
#     "visited_cities": ["Paris", "Marseille", "Lyon"],
#     "visits": 1
#   }
# ]

# def add_country(country, visited_cities, visits):
#   dictionary = {}
#   dictionary["country"] = country
#   dictionary["visited_cities"] = visited_cities
#   dictionary["visits"] = visits
#   travel_diary_3.append(dictionary)

# add_country("Slovakia", ["Bratislava", "Trnava", "Zvolen"], 2)

# print(travel_diary_3)

# def better_name(first_name, second_name):
#   if first_name == "" or second_name == "":
#     return "Nevyplnili ste meno alebo priezvisko."
#   full_name = first_name + " " + second_name
#   return full_name.title()

# result = better_name(input("Vaše meno: "), input("Vaše priezvisko: "))
# print(result)

# def leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False  

# def days(year, month):
#   days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   leap_result = leap(year)
  
#   if leap_result and month == 2:
#     return 29
#   else:
#     return days_in_month[month - 1]

# year = int(input("Zadaj rok: "))
# month_input = input("Zadaj mesiac: ").lower()

# months = ["január", "február", "marec", "apríl", "máj", "jún", "júl", "august", "september", "október", "november", "december"]
# month = months.index(month_input)+1

# result = days(year, month)
# print(f"Počet dní v zvolenom mesiaci je: {result}")

# Docstring

# def sum(num1, num2):
#   # Popis, čo robí funkcia robí
#   """Vráti súčet dvoch čísiel"""
#   return num1 + num2

# result = sum(5,3)
# print(result)

# student1 = "Sam"


# # Ak chcem vypisat premennu z funkcie, musim dat return
# def test():
#   student1 = "Rob"
  
#   return student1
# result = test()
# print(student1)
# print(result)

# Block scope v Pythone nie je 

# number = 5

# if number < 10:
#   new_number = 30

# print(new_number)

# number1 = 5

# def create_number():
#   if number1 < 5:
#     new_number_1 = 30
    
# print(new_number_1)

# Global variable

# def test():
#   global my_name
#   my_name = "Samuel"
#   print(my_name)

# test()
# print(my_name)
# Constants -velke pismena
# def calculator():
#   PI = 3.14159
#   print(PI)

# def test_function():
#   for number in range(1,10):
#     print(number)
#     if number == 10:
#       print("Všetko v poriadku")
# test_function()

# def change(x_list):
#   result_list = []
#   for item in x_list:
#     item += 10
#     result_list.append(item)
#   print(result_list)

# change([1,2,3,4,5])

# for number in range(1,101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)

# Oproti listu rozdiel v tom, že nemôžem meniť hodnoty
my_tuple = (1,4,7)

print(my_tuple)
print(my_tuple[0])

tuple_to_list = list(my_tuple)

tuple_to_list[0] = 2
print(tuple_to_list)