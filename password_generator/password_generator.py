import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

num_letters = int(input("Zadaj počet písmen: "))
num_numbers = int(input("Zadaj počet čísiel: "))
num_special_char = int(input("Zadaj počet špecialných znakov: "))

len_letters = len(letters)
len_numbers = len(numbers)
len_special_char = len(special_char)

result = []

for index in range(0, num_letters):
  rand_number = random.randint(0, len_letters-1)
  result.append(letters[rand_number])
  
for index in range(0, num_numbers):
  rand_number = random.randint(0, len_numbers-1)
  result.append(numbers[rand_number])

for index in range(0, num_special_char):
  rand_number = random.randint(0, len_special_char-1)
  result.append(special_char[rand_number])

print(result)

tmp = ""

for index in range(0,10):
  rand_index_1 = random.randint(0, len(result)-1)
  rand_index_2 = random.randint(0, len(result)-1)

  tmp = result[rand_index_2]
  result[rand_index_2] = result[rand_index_1]
  result[rand_index_1] = tmp

print(result)

random.shuffle(result)

print(result)

password = ""

for x in result:
  password += x

print(password)

